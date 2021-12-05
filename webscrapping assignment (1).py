#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


html = urlopen('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


bs = BeautifulSoup(html, "html.parser")


# In[5]:


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])


# In[6]:


print('List all the header tags :', *titles, sep='\n\n')


# In[9]:


url = 'http://www.imdb.com/chart/top'


# In[22]:



from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[23]:


response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
 


# In[24]:


movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
 
ratings = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]


# In[25]:


list = []
for index in range(0, len(movies)):
     

    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"movie_title": movie_title,
            "year": year,
            "rating": ratings[index],
            "link": links[index]}
    list.append(data)
 


# In[55]:


for movie in list:
    print( movie['movie_title'], '('+movie['year'] +
          ') -', movie['rating'])


# In[33]:


df = pd.DataFrame({'movie_title':movie_title,'year':year})
df


# In[30]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[31]:


df = pd.DataFrame(data, columns = ['Name','Rating','Year of Release'])


# In[34]:


url2 = 'https://www.imdb.com/india/top-rated-indian-movies/'


# In[38]:


responses = requests.get(url2)
soup = BeautifulSoup(responses.text, 'lxml')


# In[39]:


movies2 = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
 
ratings = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]


# In[40]:


for movies2 in list:
    print( movies2['movie_title'], '('+movies2['year'] +
          ') -', movies2['rating'])


# In[63]:


urlcrick = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }


# In[64]:


final_result_file_name = "All Ranking List.csv"
final_column_names = ["Ranking Type", "Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
pd.DataFrame(columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, encoding="utf-8")

for url in urlcrick:
    request_object = requests.get(urlcrick, headers=headers)
    html_content = request_object.text
    print(request_object.status_code, "->", urlcrick)
    soup_object = BeautifulSoup(html_content, "lxml")
    for element in soup_object.select('[class="ranking-pos up"], [class="ranking-pos down"]'):
        element.replace_with(BeautifulSoup("<" + element.name + "></" + element.name + ">", "html.parser"))

    ranking_type = soup_object.select_one(".rankings-block__title-container > h4").text

    result_file_name = ranking_type + ".csv"
    column_names = ["Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
    pd.DataFrame(columns=column_names).to_csv(result_file_name, sep="\t", index=False, encoding="utf-8")

    for element in soup_object.select('table[class="table rankings-table"] tr'):
        if(element.find("th")):
            continue
        data_dict = dict()
        data_dict["Crawl URL"] = urlcrick
        data_dict["Ranking Type"] = ranking_type
        if(element.select_one('[class*="position"]')):
            data_dict["Position"] = element.select_one('[class*="position"]').text
        for player_name in (element.select('a[href*="/player-rankings"]')):
            if(player_name.text.strip()):
                 data_dict["Player Name"] = player_name.text
        if(element.select_one('[class^="flag-15"]')):
            data_dict["Team Name"] = element.select_one('[class^="flag-15"]')["class"][-1]
        if(element.select_one('[class$="rating"]')):
            data_dict["Rating"] = element.select_one('[class$="rating"]').text
        if(element.select_one('td.u-hide-phablet')):
            data_dict["Career Best Rating"] = element.select_one('td.u-hide-phablet').text
        for key in data_dict.keys():
            data_dict[key] = re.sub(r"\s+", " ", data_dict[key])
            data_dict[key] = data_dict[key].strip()
        pd.DataFrame([data_dict], columns=column_names).to_csv(result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")
        pd.DataFrame([data_dict], columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")


# In[41]:


urlcrick2 = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
page3 = requests.get(urlcrick2)


# In[66]:


final_result_file_name = "All Ranking List.csv"
final_column_names = ["Ranking Type", "Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
pd.DataFrame(columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, encoding="utf-8")

for url in urlcrick2:
    request_object = requests.get(urlcrick2, headers=headers)
    html_content = request_object.text
    print(request_object.status_code, "->", urlcrick)
    soup_object = BeautifulSoup(html_content, "lxml")
    for element in soup_object.select('[class="ranking-pos up"], [class="ranking-pos down"]'):
        element.replace_with(BeautifulSoup("<" + element.name + "></" + element.name + ">", "html.parser"))

    ranking_type = soup_object.select_one(".rankings-block__title-container > h4").text

    result_file_name = ranking_type + ".csv"
    column_names = ["Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
    pd.DataFrame(columns=column_names).to_csv(result_file_name, sep="\t", index=False, encoding="utf-8")

    for element in soup_object.select('table[class="table rankings-table"] tr'):
        if(element.find("th")):
            continue
        data_dict = dict()
        data_dict["Crawl URL"] = urlcrick2
        data_dict["Ranking Type"] = ranking_type
        if(element.select_one('[class*="position"]')):
            data_dict["Position"] = element.select_one('[class*="position"]').text
        for player_name in (element.select('a[href*="/player-rankings"]')):
            if(player_name.text.strip()):
                 data_dict["Player Name"] = player_name.text
        if(element.select_one('[class^="flag-15"]')):
            data_dict["Team Name"] = element.select_one('[class^="flag-15"]')["class"][-1]
        if(element.select_one('[class$="rating"]')):
            data_dict["Rating"] = element.select_one('[class$="rating"]').text
        if(element.select_one('td.u-hide-phablet')):
            data_dict["Career Best Rating"] = element.select_one('td.u-hide-phablet').text
        for key in data_dict.keys():
            data_dict[key] = re.sub(r"\s+", " ", data_dict[key])
            data_dict[key] = data_dict[key].strip()
        pd.DataFrame([data_dict], columns=column_names).to_csv(result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")
        pd.DataFrame([data_dict], columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")


# In[50]:


soup3 = BeautifulSoup(page3.content)


# womens_team = soup3.find_all("span", class_="u-hide-phablet")

# In[51]:


women_match=[]
women_points=[]
women_new_list=[]


# In[55]:


for i in soup3.find_all("span",class_="u-hide-phablet"):
                        women_new_list.append(i.text)
for i in range(0,len(women_new_list)-1,2):
                        women_match.append(women_new_list[i])
                        women_points.append(women_new_list[i+1])


# In[56]:


women_match


# In[57]:


women_points


# In[58]:


women_new_list


# In[101]:


r = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[88]:


soup = BeautifulSoup(r.content, 'html.parser')
 
titles1 = []
for i in soup.find_all('div', class_="restnt-info cursor"):
    titles1.append(i.text)
titles1


# In[ ]:





# In[92]:


soup = BeautifulSoup(r.content, 'html.parser')
 
cuisine = []
for i in soup.find_all('span', class_="double-line-ellipsis"):
    cuisine.append(i.text)
cuisine


# In[91]:


soup = BeautifulSoup(r.content, 'html.parser')
 
rating = []
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[95]:


soup = BeautifulSoup(r.content, 'html.parser')
 
images = []
for i in soup.find_all('img', class_="no-img"):
    images.append(i['data-src'])
images


# In[112]:


s = requests.get('https://en.tutiempo.net/delhi.html?data=last-24-hours')


# In[114]:


soup = BeautifulSoup(s.content,'html.parser')


# In[113]:


soup


# In[111]:


soup = BeautifulSoup(s.content, 'html.parser')
 
Hour = []
for i in soup.find_all('th', class_="thHora"):
    Hour.append(i.text)
Hour


# In[125]:


soup = BeautifulSoup(s.content,'html.parser')
 
Tem = []
for i in soup.find_all('th', class_="thTem"):
    Tem.append(i.text)
Tem


# In[126]:


r = requests.get('https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/')


# In[129]:


r


# In[130]:


soup = BeautifulSoup(r.content)


# In[59]:


soup


# In[61]:


name = []

for i in soup.find_all('strong', class_="Taj Mahal"):
    name.append(i.text)
name


# In[62]:


soup = BeautifulSoup(r.content,'html.parser')
 
image = []
for i in soup.find_all('img alt', class_="alignnone size-full wp-image-36626 lazyloaded"):
    image.append(i[data-src])
image


# In[ ]:





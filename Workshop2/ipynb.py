#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HCS Workshop 2, Web Scraping


# In[2]:


# Author: Serena Han


# In[133]:


# import requests package and set up page

import requests
page = requests.get("https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=13670&result_id=122706")
print(page.status_code)
print(page.content)


# In[12]:


# import BeautifulSoup and make a "BeautifulSoup object"
# sudo apt-get install python-bs4

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


# In[6]:


# more sources? 
# https://beautiful-soup-4.readthedocs.io/en/latest/
# https://www.dataquest.io/blog/web-scraping-tutorial-python/


# In[170]:


# tabroom scraping of the 2019 Harvard Forensics Tournament
page = requests.get('https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=13670&result_id=122706')
soup = BeautifulSoup(page.content, 'html.parser')
records = soup.find(id='122706-1')

# selects rows for top 100 teams
teams = records.find_all('tr', limit=100)[1:]


# finds team names and states from tabular data
schools = []
states = []
for team in teams:
    school = (team.find_all('td'))[1].get_text().strip()[:-3]
    schools.append(school)
#     print(school)
    state = (team.find_all('td'))[3].get_text().strip()
    states.append(state)
#     print(state)
#     print("——————————————————")
    
# finds the most common schools and states
def create_dictionary(mylist): 
    word_count = {} 
      
    for word in mylist: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
            
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Get top 10 most common
    for name in sorted_words[:10]:
        print(f"{name[0]} had {name[1]} teams in the top 100.")
    
# prints top 10 most dominant schools and states
print("Big Schools:")
create_dictionary(schools)
print("\nBig States:")
create_dictionary(states)
    


# In[ ]:





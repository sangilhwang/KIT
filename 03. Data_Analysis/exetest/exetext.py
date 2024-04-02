#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys


# In[2]:


url = "https://www.naver.com"

driver = webdriver.Chrome()

driver.get(url)


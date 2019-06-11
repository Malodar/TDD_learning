# -*- coding: UTF-8 -*-
from selenium import webdriver


browser = webdriver.Firefox(executable_path='/home/artsiom/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title

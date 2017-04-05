# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:10:03 2017
AirBnB Scrape Functions
@author: Aniket
"""
import time
import zipcode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def zipcodes_list(st_items):
    if type(st_items) == str:
        zcObjects = zipcode.islike(st_items)
        output = []
        for i in zcObjects:
            output.append(str(i).split(" ", 1)[1].split(">")[0])
    elif type(st_items) == list:
        zcObjects = []
        for i in st_items:
            zcObjects = zcObjects + zipcode.islike(i)
        output = []
        for i in zcObjects:
            output.append(str(i).split(" ", 1)[1].split(">")[0])
    else:
        raise ValueError("input 'st_items' must be of type str or list")
    return(output)

def init_driver(filepath):
    driver = webdriver.Chrome(executable_path = filepath)
    driver.wait = WebDriverWait(driver, 10)
    return(driver)

def navigate_to_website(driver, site):
    driver.get(site)

def enter_search_term(driver, search_term):
    try:
        searchBar = driver.wait.until(EC.presence_of_element_located((
                By.ID, "header-search-form-input-type")))
        button = driver.wait.until(EC.element_to_be_clickable((
                By.NAME, "location")))
        searchBar.clear()
        time.sleep(3)
        button.click()
        searchBar.send_keys(search_term)
        searchBar.send_keys(Keys.RETURN)
        time.sleep(3)
        searchBar.send_keys(Keys.ESCAPE)
        return(True)
    except (TimeoutException, NoSuchElementException):
        return(False)

def get_html(driver):
    output = []
    output.append(driver.page_source)
    return(output)

def get_listings(list_obj):
    output = []
    for i in list_obj:
        htmlSplit = i.split(':[],"id":')[1:]
        output += htmlSplit
    return(output)


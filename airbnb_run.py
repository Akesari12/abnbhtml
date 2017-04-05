# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:12:13 2017

AirBnB Run File

@author: Aniket
"""
import os
os.chdir("C:/Users/Owner/Dropbox/Homework/Spring 2017/Urban Data Science Lab/AirBnBSel")

import time
import pandas as pd
import airbnb_functions as af
import zipcode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Create a list of zip codes. The background function uses the 'zipcode' package that generates a list based 
# on zipcodes that are "like" the ones inputted.  So for example, if one typed "947" they would get all of 
# Berkeley
st = af.zipcodes_list(st_items = ['94704'])

# Initialize the webdriver.
driver = af.init_driver('C:/Users/Owner/Documents/chromedriver_win32/chromedriver.exe')

# Go to airbnb.com/search
af.navigate_to_website(driver, "http://www.airbnb.com/search")

# Unable to call this function from the other file for some reason, so defining it internally for now =/
def enter_search_term(driver, search_term):
    try:
        searchBar = driver.wait.until(EC.presence_of_element_located(( # From Selenium package, the browser waits until it finds an element
                By.ID, "input_rcy19f"))) # Looks for an element by this ID type (taken from the HTML source of the website)
        button = driver.wait.until(EC.element_to_be_clickable((
                By.NAME, "location"))) # Finds the button with this name
        searchBar.clear() # Clears the search bar
        time.sleep(3) # Waits 3 seconds
        button.click() # Clicks the button
        searchBar.send_keys(search_term) # Input the search term
        searchBar.send_keys(Keys.RETURN) # Press enter to search
        time.sleep(3) # Wait three seconds
        searchBar.send_keys(Keys.ESCAPE) # Hit "Escape" to get out of the popup window
        return(True)
    except (TimeoutException, NoSuchElementException):
        return(False)

enter_search_term(driver, "94704") # Search for Downtown Berkeley/Campus

def get_html(driver): # Pull the HTML source
    output = []
    output.append(driver.page_source) # From Selenium package
    return(output)

listob = get_html(driver) # Store the HTML
 
def get_listings(list_obj): # Separate out the HTML by this string which starts the listing entries
    output = []
    for i in list_obj:
        htmlSplit = i.split('[],"id":')
        output += htmlSplit
    return(output)

get_listings(listob) # This isn't working.  It's pulling some random HTML from the website?

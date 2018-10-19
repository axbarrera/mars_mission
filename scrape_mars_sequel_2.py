from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
import time
from selenium import webdriver


# In[32]:


	# executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
	# return Browser("chrome", **executable_path, headless=False)


# In[33]:


#initiate driver
def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # init single mars dictionary
    mars_stuff = {}


    #hit first mars url in browser
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


    # In[35]:


    #gather html with bs
    html = browser.html
    soup = bs(html,"html.parser")

    # commenting this out because it destroys my browser
    # print(soup)


    # # NASA Mars News

    # In[36]:


    # search for news title, and get "lucky" bc the answer was the name from the Readme, could not actually find this on the page correctly with inspect.
    news_title = soup.find("div",class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text

    # print results to be sure
    print(f"Title: {news_title}")
    print(f"Paragraph: {news_p}")

    mars_stuff['news_title'] = news_title
    mars_stuff['news_p'] = news_p




    # ## JPL Mars Space Images - Featured Image

    # In[37]:


    # hit JPL URL
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)


    # In[38]:


    # could not honestly find featured_image_url, but using inspector I got the resulting large image url anyway 
    # hardcoding the large url 

    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA17832_hires.jpg"
    
    mars_stuff['featured_image_url'] = featured_image_url



    # ## Mars Weather

    # In[39]:


    # hit weather url 
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)


    # In[42]:


    #Grab tweets with bs 
    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    #commenting out bc too much ram
    # print(soup).prettyify()


    # In[43]:


    # there are multiple tweets in the soup, going to get the first one for now and try to parse for the actual weather ones later
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)

    mars_stuff['mars_weather'] = mars_weather


    # ## Mars Facts

    # In[44]:


    # hit mars facts url 

    url_facts = "https://space-facts.com/mars/"
    time.sleep(3)

    # grab the only table
    table = pd.read_html(url_facts)
    table[0]

    df_mars_facts = table[0]
    time.sleep(3)
    df_mars_facts.columns = ["Parameter", "Values"]
    df_mars_facts_indexed = df_mars_facts.set_index(["Parameter"])

    # set mars html table string
    mars_html_table = df_mars_facts_indexed.to_html()
    # mars_html_table = mars_html_table.replace("\n", "")
    mars_stuff["mars_facts_table"] = mars_html_table

    # mars_stuff['mars_html_table_string'] = mars_html_table_string

    # trying to get the table in there
    mars_stuff['df_mars_facts'] = df_mars_facts



    # ## Mars Hemispheres

    # In[51]:


    # hit hemispheres page
    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemisphere)


    # In[52]:


    # set dictionary of hemispheres from example
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
        {"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
        {"title": "Schiaparelli Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
        {"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
    ]
    mars_stuff['hemisphere_image_urls'] = hemisphere_image_urls


    # In[53]:


    # #Cerberus Hemisphere 
    # hemisphere_img_urls = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"]
    # results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    # time.sleep(2)
    # cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    # time.sleep(1)
    # cerberus_image = browser.html
    # soup = bs(cerberus_image, "html.parser")
    # cerberus_url = soup.find("img", class_="wide-image")["src"]
    # cerberus_img_url = hemisphere_base_url + cerberus_url
    # print(cerberus_img_url)
    # cerberus_title = soup.find("h2",class_="title").text
    # print(cerberus_title)
    # back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    # cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    # hemisphere_img_urls.append(cerberus)


        
        


    # In[54]:


    # #Schiaparelli Hemisphere Enhanced
    # results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    # time.sleep(2)
    # schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    # time.sleep(1)
    # schiaparelli_image = browser.html
    # soup = bs(schiaparelli_image, "html.parser")
    # schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    # schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
    # print(schiaparelli_img_url)
    # schiaparelli_title = soup.find("h2",class_="title").text
    # print(schiaparelli_title)
    # back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    # schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    # hemisphere_img_urls.append(schiaparelli)


    # In[55]:


    # #Syrtis Major Hemisphere Enhanced
    # results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    # time.sleep(2)
    # syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    # time.sleep(1)
    # syrtis_major_image = browser.html
    # soup = bs(syrtis_major_image, "html.parser")
    # syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    # syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
    # print(syrtis_major_img_url)
    # syrtis_major_title = soup.find("h2",class_="title").text
    # print(syrtis_major_title)
    # back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    # syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
    # hemisphere_img_urls.append(syrtis_major)


    # In[56]:


    # #Valles Marineris Hemisphere Enhanced
    # results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    # time.sleep(2)
    # valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    # time.sleep(1)
    # valles_marineris_image = browser.html
    # soup = bs(valles_marineris_image, "html.parser")
    # valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    # valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    # print(valles_marineris_img_url)
    # valles_marineris_title = soup.find("h2",class_="title").text
    # print(valles_marineris_title)
    # back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    # valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    # hemisphere_img_urls.append(valles_marineris)


    # In[27]:


    

    return mars_stuff


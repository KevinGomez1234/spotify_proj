from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.python.org")
#elem = driver.find_element_by_name("q") in this case there is an element called q 
#elem.clear() clear the element value
#elem.send_keys("pycon") attatch your own text
#elem.send_keys(Keys.RETURN) enter key inside text element triggers submit if type="submit" button
#assert "No results found." not in driver.page_source if it is true that "no results found" is in the page then dont do anything else this is in the page source, then assertion error...


#assert "Python" in driver.title //// driver.title is <title>Python webpage<title>

#driver.close //close browser

#username = input("Enter your spotify username")
#openSpotifyURL = "https://open.spotify.com/user/" + username
#print(openSpotifyURL)

import time
from selenium import webdriver #webdriver 
from selenium.common.exceptions import NoSuchElementException #Exception to handle element that is not found
from selenium.webdriver.firefox.options import Options #option to go headless is in here

from selenium.webdriver.common.by import By #used in conjunction with expected conditions, we will wait By.id, By.class, etc
from selenium.webdriver.support.ui import WebDriverWait #Webdriver wait using in conjunction with ec
from selenium.webdriver.support import expected_conditions as EC #Conditions to wait
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
username = input("Enter your spotify username: ")
openSpotifyURL = "https://open.spotify.com/user/" + username
driver.get(openSpotifyURL)
#assert "Couldn't find that user" not in driver.page_source
#fe734d4199c79a07c0fbcfc81fb4a4b4-scss class that is in the page when user is not found...
try:
	userNotFoundElem = driver.find_element_by_class_name("fe734d4199c79a07c0fbcfc81fb4a4b4-scss")
	print("This user is not found")
except NoSuchElementException:
	try:
		parentDivToPlaylists = driver.find_element_by_class_name("c247a773eeb0d66dcd9c92d83e50c263-scss")
		#get a list of all the playlists
		aPlaylist = parentDivToPlaylists.find_elements_by_css_selector("div div div div a")
		print("You have " + str(len(aPlaylist)) + " playlist")
		x = 0
		links = []
		for i in aPlaylist:
			x = x + 1
			print( str(x) + ". " + i.text + "\n")
			links.append(i.get_attribute("href")) #this puts all links in a list
		playlistNumber = int(input("Pick a playlist: ")) - 1
		driver.get(links[playlistNumber])
		try:
			time.sleep(100)# we need to wait for all tracks to load, if not this does not work
			mainViewContainer = driver.find_elements_by_css_selector("div>div.tracklist-name")
			print("You have: " + str(len(mainViewContainer)) + " songs") #these are the number of songs
			for t in mainViewContainer:
				print(t.text + "\n")
		except NoSuchElementException:
			print("Tracklist not found")
		#print(aPlaylist[0].get_attribute("href")) to get attribute value of href which is link to another playlist
		#we can also click... js... with selenium
		#childPlaylists = parentDivToPlaylists.find_element_by_css_selector('div.*')
		#print(childPlaylists)
	except NoSuchElementException:
		print("This user does not have any playlists")
driver.close

#elem = driver.find_element_by_name("q") in this case there is an element called q 
#elem.clear() clear the element value
#elem.send_keys("pycon") attatch your own text
#elem.send_keys(Keys.RETURN) I guess submit?
#assert "No results found." not in driver.page_source if it is true that "no results found" is in the page then dont do anything else this is in the page source, then assertion error...
#assert "Python" in driver.title driver.title is <title>Python webpage<title>

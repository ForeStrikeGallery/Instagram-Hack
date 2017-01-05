'''
This is a very naive way of getting people to find you on Instagram.
Be careful, your account might get blocked.
Like mine did.
And I'm sad now :( 

'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome()
driver.get("http://www.instagram.com/")


#replace with your username and password
username = "username"
password = "password"

a = driver.find_element_by_class_name("_fcn8k")
a.click()

a = driver.find_element_by_name("username")
a.send_keys(username)
a.send_keys(Keys.TAB)
a = driver.switch_to.active_element

a.send_keys(password)
a.send_keys(Keys.RETURN)

time.sleep(5)

explore_url = "http://www.instagram.com/explore/tags/"

tags = [
	
	'picture',
	'drawing',
	'doodling',
	'illustration',
	'art',
	'sketch',
	'artist',
	'origami',
	'origamiartist',
	'pencilsketchartist'	
	]

for j in range(len(tags)):

	cur_url = explore_url + tags[j]


	driver.get(cur_url)

	a = driver.find_element_by_class_name("_1b8in")	

	for i in range(22):
		a.send_keys(Keys.TAB)
		a = driver.switch_to.active_element


	a.send_keys(Keys.RETURN)
	time.sleep(3)

	#You may want to add more comments
	comment = [
		"Wow, this is wonderful! I love it !",
		"That is some brilliant shit right there!",
		"Damn, nice!",
		"That's really cool!",
		'This is really wonderful! I love your work!',
		'You are the next picasso',
		'Are you kiddin me? Thats fucking awesome! ',
	]
	try: 
		for i in range(1000):
			try:
				a = driver.find_element_by_class_name("_tf9x3")
				b = a.find_element_by_tag_name('span')
				likes = int(b.text.replace(",",""))
			except:
				likes = 0	

			print likes 	
			if likes < 200:	
				a = driver.find_element_by_class_name("_7uiwk")
				name = driver.find_element_by_class_name("_4zhc5")
				com = "@" + name.text + " " + comment[random.randrange(len(comment))]
				print com
				a.send_keys(com)
				a.send_keys(Keys.RETURN)
				time.sleep(6)

				a = driver.switch_to.active_element
				a.click()

				time.sleep(3)

				a = driver.find_element_by_class_name("_hj98d")
				b = a.find_elements_by_tag_name("a")[1]

				b.click()
				time.sleep(3)
			else:
				a = driver.find_element_by_class_name("_hj98d")
				b = a.find_elements_by_tag_name("a")[1]

				b.click()
				time.sleep(2)
					
	except:
		continue		









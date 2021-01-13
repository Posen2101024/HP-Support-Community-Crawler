
from .service import Status
from .service import Update
from .service import UnfinishedUrls
from .parser import ParseForum
from .parser import ParseTopic
from .util import urlRequests
from .util import timeToYMDHM

from os import makedirs
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def topicUrlCrawler(path_url, item, length, id_ = 0):

	forum, url = item

	def stopCrawler(first_url):
	
		try:

			parser = ParseTopic(urlRequests(first_url))

			pages = parser.getPages()

			if pages > 1: 

				parser = ParseTopic(urlRequests("{}/page/{}".format(first_url, pages)))

			time = parser.getContent(["Time"], ["Content"]).split("\n")[-1]

			return Update().isUpdated(timeToYMDHM(time))
		
		except Exception as e:

			# print(e)

			return False

	def work():

		Status().write("{:<{}s} | ".format(forum, length), id_)

		try:

			makedirs(path_url, exist_ok = True)

			file_url = "{}/{}".format(path_url, forum)

			chrome_options = Options()
			chrome_options.add_argument("--headless")
			chrome_options.add_argument("--disable-gpu")
			chrome_options.add_argument("blink-settings=imagesEnabled=false")
			chrome_options.add_argument("--window-size=4000,1600")
			
			chromedriver = "./chromedriver"

			browser = webdriver.Chrome(chromedriver, chrome_options = chrome_options)

			browser.get(url)

			for num in range(1, 100000):

				# Wait

				WebDriverWait(browser, 60).until(
					ec.presence_of_element_located((By.XPATH, 
					"//a[@id='jp-next'][@data='{}']".format(num + 1)))
				)

				parser = ParseForum(browser.page_source)

				if stopCrawler(parser.getFirstUrl()): break

				# Save Url

				urls = parser.getUrls()

				with open(file_url, "a") as f: f.write("\n".join(urls) + "\n")

				UnfinishedUrls().addUrls(urls)

				Status().write("{:<{}s} | Page: {}".format(forum, length, num), id_)

				# Next Page

				next_page = browser.find_elements_by_xpath(
					"//a[@class='jp-next pagination-recent-post_page']")

				if len(next_page) == 0: break

				next_page = next_page[0]

				browser.execute_script("arguments[0].scrollIntoView(false);", next_page)
				browser.execute_script("window.scrollBy(0, 200)")

				sleep(1)

				next_page.click()

			with open(file_url, "r") as f: urls = set(f.read().split())
			with open(file_url, "w") as f: f.write("\n".join(sorted(urls)) + "\n")

		except Exception as e:

			# print(e)
			
			return False

		finally: browser.close()

		return True

	while not work(): 
		
		print("{:<{}s} Restart!!".format(forum, length))

	print("{:<{}s} Finished.".format(forum, length))

def topicHtmlCrawler(path_html, path_content, items, id_ = 0):

	for i, item in enumerate(items, 1):

		topic = ""

		try:

			forum, url = item

			parser = ParseTopic(urlRequests(url))

			time = parser.getContent(["Time"], ["Content"]).split("\n")[0]
			code = url.split("/")[-1]
			topic = "{}_{}.txt".format(timeToYMDHM(time).split()[0], code)

			makedirs("{}/{}".format(path_html, forum), exist_ok = True)

			file = "{}/{}/{}".format(path_html, forum, topic)

			with open(file, "w") as f:

				f.write(str(parser))
		
				for page in range(2, parser.getPages() + 1):
					parser = ParseTopic(urlRequests("{}/page/{}".format(url, page)))
					f.write("\n{}".format(str(parser)))

			topicHtmlToContent(path_html, path_content, forum, topic)

			UnfinishedUrls().delUrls([url])
		
		except Exception as e:

			# print(e)

			print(url)

		Status().write("[{:>{}d} / {}] {}"
			.format(i, len(str(len(items))), len(items), topic), id_)

def topicHtmlToContent(path_html, path_content, forum, topic):

	makedirs("{}/{}".format(path_content, forum), exist_ok = True)

	file_html    = "{}/{}/{}".format(path_html,    forum, topic)
	file_content = "{}/{}/{}".format(path_content, forum, topic)

	with open(file_html, "r") as f:

		parser = [ParseTopic(html) for html in filter(None, f.read().split("<!DOCTYPE html>"))]

	topic_url     = parser[0].getUrl()
	topic_title   = parser[0].getContent(["Title"]).split("\n")[0]
	topic_product = parser[0].getContent(["Product"]).split("\n")[0]
	topic_os      = parser[0].getContent(["Os"]).split("\n")[0]
	topic_solved  = parser[0].getContent(["Solved"])[:7]

	topic_time_first = timeToYMDHM(parser[ 0].getContent(["Time"], ["Content"]).split("\n")[ 0])
	topic_time_last  = timeToYMDHM(parser[-1].getContent(["Time"], ["Content"]).split("\n")[-1])

	topic_product = "`No Product`" if topic_product == "" else topic_product[len("Product: "):]

	topic_os = "`No Operating System`" if topic_os == "" else topic_os[len("Operating System: "):]

	with open(file_content, "w") as f:

		f.write("{}\n{}\n".format(topic_url, topic_title))
		f.write("{}\n{}\n".format(topic_product, topic_os))
		f.write("{}\n{}\n".format(topic_time_first, topic_time_last))

		if topic_solved: f.write("{}\n".format(topic_solved))

		f.write("\n")

		for i, _ in enumerate(parser):

			text = parser[i].getContent(
				["Content"], ["Time", "UserSignature", "Solved", "Blockquote"])

			if text: f.write("{}\n".format(text))

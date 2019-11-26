
from .service import Status
from .service import Update
from .service import UnfinishedUrls
from .util import getForumUrl
from .util import getTopicUrl
from .util import getTopicHtml
from .work import topicUrlCrawler
from .work import topicHtmlCrawler
from .work import topicHtmlToContent

import threading
import multiprocessing

def topicUrlCrawlerThread(path_forum, path_url):

	items = getForumUrl(path_forum)

	length = max(len(forum) for forum, _ in items)

	threads = [
		threading.Thread(
			target = topicUrlCrawler, 
			args = (path_url, item, length, id_),
		)
		for id_, item in enumerate(items)
	]

	for thread in threads: thread.start()
	for thread in threads: thread.join()

	Status().clear()

	Update().latestUpdate()

def topicHtmlCrawlerThread(path_url, path_html, path_content, num_workers = 1):

	data = getTopicUrl(path_url)

	data = [(forum, url) for forum, url in data if url in UnfinishedUrls().getUrls()]

	data_split = [[] for _ in range(num_workers)]
	for i, item in enumerate(data):
		data_split[i % num_workers].append(item)

	threads = [
		threading.Thread(
			target = topicHtmlCrawler, 
			args = (path_html, path_content, items, id_),
		) for id_, items in enumerate(data_split)
	]

	for thread in threads: thread.start()
	for thread in threads: thread.join()

	Status().clear()

def topicHtmlToContentProcess(path_html, path_content, num_workers = 1):

	def topicHtmlToContentWork(items):
		for forum, topic in items:
			topicHtmlToContent(path_html, path_content, forum, topic)
			print("{} {}".format(forum, topic))

	data = getTopicHtml(path_html)

	data_split = [[] for _ in range(num_workers)]
	for i, item in enumerate(data):
		data_split[i % num_workers].append(item)

	processes = [
		multiprocessing.Process(
			target = topicHtmlToContentWork, 
			args = (items, ),
		) for items in data_split
	]

	for process in processes: process.start()
	for process in processes: process.join()

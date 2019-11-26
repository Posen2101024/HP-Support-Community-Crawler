
from os import listdir, makedirs

def getForumUrl(path_forum):

	with open(path_forum, "r") as f:

		data = f.read().split("\n")[1:]

		data = [tuple(item.split("\t")) for item in data]

		return data

def getTopicUrl(path_url):

	data = []

	for forum in listdir(path_url):

		with open("{}/{}".format(path_url, forum), "r") as f:

			url = f.readline()

			while url:

				url = url.strip()

				if url: data.append((forum, url))

				url = f.readline()

	return data

def getTopicHtml(path_html):

	data = []

	for forum in listdir(path_html):

		for topic in listdir("{}/{}".format(path_html, forum)):

			data.append((forum, topic))

	return data

def dateToYMD(date):

	date = date.split("-")

	date = "{}-{}-{}".format(date[2], date[0], date[1])
	
	return date

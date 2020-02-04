
from os import listdir, makedirs

import requests

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

def urlRequests(url):

	return requests.get(url, timeout = 60).text

def timeToYMDHM(time):

	date, time, meridiem = time.split()

	date = [int(num) for num in date.split("-")]

	time = [int(num) for num in time.split(":")]

	if meridiem == "PM" and time[0]  < 12: time[0] += 12
	if meridiem == "AM" and time[0] == 12: time[0] -= 12
	
	return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}".format(
		date[2], date[0], date[1], time[0], time[1])

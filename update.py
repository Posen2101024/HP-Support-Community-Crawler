
from crawler import topicUrlCrawlerThread
from crawler import topicHtmlCrawlerThread
from crawler import topicHtmlToContentProcess
from crawler import serviceInit

from os import listdir

import argparse

def main(args):

	model = "model/{}".format(args.model)

	path_forum   = "{}/forum.csv".format(model)
	path_url     = "{}/url".format(model)
	path_html    = "{}/html".format(model)
	path_content = "{}/content".format(model)

	serviceInit(model)

	if args.url:

		topicUrlCrawlerThread(path_forum, path_url)

	if args.html:

		topicHtmlCrawlerThread(path_url, path_html, path_content, num_workers = 8)

	if args.content:

		topicHtmlToContentProcess(path_html, path_content, num_workers = 8)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument("model", type = str)

	parser.add_argument("--url", 
		default = False, action = "store_true")
	parser.add_argument("--html", 
		default = False, action = "store_true")
	parser.add_argument("--content", 
		default = False, action = "store_true")

	args = parser.parse_args()

	main(args)

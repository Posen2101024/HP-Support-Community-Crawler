
from bs4 import BeautifulSoup

import re

class Parser():

	def __init__(self, text):

		list_x = [0] + [word.end()   for word in re.finditer("-->",  text)]
		list_y =       [word.start() for word in re.finditer("<!--", text)] + [len(text)]
		
		text = " ".join(text[x:y].strip() for x, y in zip(list_x, list_y))

		text = "".join(text.split("\u200e"))

		self.text = BeautifulSoup(text, "lxml")

		self.parser = {}

	def addParser(self, name, attr, tag = None, label = None):

		self.parser[name] = (attr, tag, label)

	def getContent(self, names_parser = None, names_remove = None): 

		return self._search(
			names_parser if names_parser else [], 
			names_remove if names_remove else [],
		)

	def _search(self, names_parser, names_remove):

		def isRequired(element, item):

			attr, tag, label = item

			if not element.name == attr: return False

			if not tag: return True

			detail = element.get(tag)

			return detail == label or detail and detail[:len(label)] == label

		def getText(element):

			if not element.name: return element.strip()

			for name in names_remove:

				if isRequired(element, self.parser[name]):

					return None

			item = filter(None, [getText(children) for children in element.children])

			return " ".join(" ".join(text.split()) for text in item)

		def dfs(element):

			if not element.name: return None

			for name in names_remove:

				if isRequired(element, self.parser[name]):

					return None

			for name in names_parser:

				if isRequired(element, self.parser[name]):

					return getText(element)

			item = filter(None, [dfs(children) for children in element.children])

			return "\n".join(item)

		return dfs(self.text)

	def __str__(self): return self.text.prettify()

class ParseForum(Parser):

	def __init__(self, text):

		super().__init__(text)

	def _parents(self, element, num):

		return element if num == 0 else self._parents(element.parent, num - 1)

	def getUrls(self):

		return ["https://h30434.www3.hp.com" + element.get("href")
			for element in self.text.find_all("a") if
			self._parents(element, 1).get("class") == ["article-head"] and
			self._parents(element, 2).get("class") == ["article-heading"]
		]

	def getFirstUrl(self):

		return ["https://h30434.www3.hp.com" + element.get("href")
			for element in self.text.find_all("a") if
			self._parents(element, 1).get("class") == ["article-head"] and
			self._parents(element, 2).get("class") == ["article-heading"] and
			self._parents(element, 6).get("class") == ["article-topic-list", "article-all-topics"]
		][0]

class ParseTopic(Parser):

	def __init__(self, text):

		super().__init__(text)

		self.addParser(name = "Title", attr = "span", 
			tag = "class", label = ["lia-link-navigation", "lia-link-disabled"])
		self.addParser(name = "Product", attr = "div", 
			tag = "class", label = ["message_product"])
		self.addParser(name = "Os", attr = "div", 
			tag = "class", label = ["message_os"])
		self.addParser(name = "Author", attr = "span", 
			tag = "class", label = ["UserName"])
		self.addParser(name = "Time", attr = "span", 
			tag = "class", label = ["DateTime"])
		self.addParser(name = "Content", attr = "div", 
			tag = "class", label = ["lia-message-body-content"])
		self.addParser(name = "Solved", attr = "div", 
			tag = "class", label = ["lia-panel-feedback-banner-safe"])
		self.addParser(name = "UserSignature", attr = "div", 
			tag = "class", label = ["UserSignature", "lia-message-signature"])
		self.addParser(name = "Blockquote", attr = "blockquote")

	def getUrl(self):

		item = self.text.find_all("link", rel = "canonical")[0]

		return item.get("href")

	def getPages(self):

		pages = self.text.find_all("ul", class_ = "lia-paging-full-pages")

		pages = 1 if not pages else int(pages[0].text.split()[-1])

		return pages


from os import makedirs

import threading

def serviceInit(model):

	Status().init()
	Update().init(model)
	UnfinishedUrls().init(model)

class _Singleton():

	_instance = None

	def __new__(self, *args, **kwargs):

		if not self._instance:

			self._instance = super().__new__(self)

		return self._instance

class Status(_Singleton):

	def init(self, name = ".status"):

		self.lock = threading.Lock()

		self.name = name

		self.status = []

	def write(self, text, id_):

		with self.lock:

			while len(self.status) <= id_:
				self.status.append("")

			self.status[id_] = text

		with open(self.name, "w") as f:

			f.write("\n".join(self.status))

	def clear(self):

		with self.lock: self.status = []

class Update(_Singleton):

	def init(self, model, dir_ = ".service", name = "update"):

		path = "{}/{}".format(model, dir_)

		makedirs(path, exist_ok = True)

		self.lock = threading.Lock()

		self.name = "{}/{}".format(path, name)

		with open(self.name, "a+") as f:
			f.seek(0); date = f.read()

		self.date = self.latest = date if date else "0000-00-00"

	def isUpdated(self, date):

		with self.lock:

			if self.latest < date:

				self.latest = date

		return self.date > date

	def latestUpdate(self):

		with open(self.name, "w") as f:

			f.write(self.latest)

class UnfinishedUrls(_Singleton):

	def init(self, model, dir_ = ".service", name = "unfinished_urls", 
		add_urls = "add_urls", del_urls = "del_urls"):

		path = "{}/{}".format(model, dir_)

		makedirs(path, exist_ok = True)

		self.lock = threading.Lock()

		self.name = "{}/{}".format(path, name)
		self.add_urls = "{}/{}".format(path, add_urls)
		self.del_urls = "{}/{}".format(path, del_urls)

		with open(self.name, "a+") as f:
			f.seek(0); self.urls = set(f.read().split())
		with open(self.add_urls, "a+") as f:
			f.seek(0); self.urls = self.urls | set(f.read().split())
		with open(self.del_urls, "a+") as f:
			f.seek(0); self.urls = self.urls - set(f.read().split())

		with open(self.name, "w") as f: 
			f.write("\n".join(self.urls))
		with open(self.add_urls, "w") as f: pass
		with open(self.del_urls, "w") as f: pass

	def getUrls(self): return self.urls

	def addUrls(self, urls):

		with self.lock:

			urls = set(urls)

			self.urls = self.urls | urls

			with open(self.add_urls, "a") as f:
				f.write("\n".join(urls) + "\n")

	def delUrls(self, urls):

		with self.lock:

			urls = set(urls)

			self.urls = self.urls - urls

			with open(self.del_urls, "a") as f:
				f.write("\n".join(urls) + "\n")

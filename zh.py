# -*- coding: utf-8 -*-

import codecs
import sys
import re

class Word:
	def __init__(self,w):
		self.name = w
		self.afterCounter = 0
		self.beforeCounter = 0
		self.myDictAfter = {}
		self.myDictBefore = {}
	
	def after(self,pw):
		if pw in self.myDictAfter:
			self.myDictAfter[pw] = self.myDictAfter[pw] + 1
		else:
			self.myDictAfter[pw] = 1
		self.afterCounter = self.afterCounter + 1
	
	def before(self,pw):
		if pw in self.myDictBefore:
			self.myDictBefore[pw] = self.myDictBefore[pw] + 1
		else:
			self.myDictBefore[pw] = 1
		self.beforeCounter = self.beforeCounter + 1
	
	"""def statistic(self,word,isBefore,isFullWord):
		if isFullWord:
			if isBefore:
				if word in self.myDictBefore:
					return self.myDictBefore[word] / self.beforeCounter
				else
					return 0
			else:
				if word in self.myDictAfter:
					return self.myDictAfter[word] / self.afterCounter
				else:
					return 0
		else:
			if isBefore:
				if self.beforeCount != 0:
					temp = 0
					for k, v in self.myDictBefore:
						if re.search(word,k) != None:
							temp = temp + v
					return temp/self.beforeCount
			else:
				if self.afterCount != 0:	
					temp = 0
					for k,v in self.myDictAfter:
						if re.search(word,k) != None:
							temp = temp + v
					return temp/self.afterCount
		return 0"""

	def statistic(self,isBefore):
		temp = {}
		if isBefore:
			for k,v in self.myDictBefore.iteritems():
				temp[k] = (v*100)/self.beforeCounter
		else:
			#print self.myDictAfter 
			for k,v in self.myDictAfter.iteritems():
				#print v,"-",self.afterCounter
				temp[k] = (v*100)/self.afterCounter
		return temp
	
	def catenate(self,numa,numb):
		tmp = {} 
		for k,v in self.myDictAfter.iteritems():
			temp = self.name+" - "+k
			tmp[temp] = (v*10000)/numa
		for k,v in self.myDictBefore.iteritems():
			temp = k + " - "+self.name
			tmp[temp] = (v*10000)/numb
		return tmp

	def getAfterCount(self):
		return self.afterCounter

	def getBeforeCount(self):
		return self.beforeCounter

class load:
	def switch_param(self,param,index):
		if param == '-i':
			self.file_path = sys.argv[index]
			return
		elif param == '-b':
			self.option = 1 
		elif param == '-a':
			self.option = 2
		elif param == '-sb':
			self.option = 3
		elif param == '-sa':
			self.option = 4
		elif param == '-p':
			self.option = 5
			return
		else:
			return
		self.actWord = sys.argv[index]
			
	def __init__(self):
		if len(sys.argv) > 1:
			i = 1
			while i < len(sys.argv):
				self.switch_param(sys.argv[i],i+1)
				i = i+2
			tmp = codecs.open(self.file_path)
			self.words = re.split("\W+",tmp.read())
			#print self.words
			self.myDict = {}
			i = 0
			while i< len(self.words): 
				bef = None
				aft = None
				if i >= 1:
					bef = self.words[i-1]
				if i<len(self.words)-1:
					aft = self.words[i+1]
				act = self.words[i]
				if act not in self.myDict:
					self.myDict[act] = Word(act)
				if bef != None:
					self.myDict[act].before(bef)
				if aft != None:
					self.myDict[act].after(aft)
				i = i+1
	
	def printout(self,l,isBefore,isFull):
		if isFull:
			if isBefore:
				for k,v in l.iteritems():
					print k," - ",self.actWord," elofordulas aranya: ",v,"%"
			else:
				for k,v in l.iteritems():
					print self.actWord," - ",k," elofordulas aranya: ",v,"%"
		else:
			if isBefore:
				for k,v in l.iteritems():
					for key,val in v.iteritems():
						print key," - ",k," elofordulas aranya: ",val,"%"
			else:
				for key, val in l.iteritems():
					for k,v in val.iteritems():
						print key,"-",k," elofordulas aranya: ",v,"%"


	def result(self):
		if self.option == 1: # a szo elotti szavak listazasa arannyal egyutt
			if self.actWord in self.myDict:
				self.printout(self.myDict[self.actWord].statistic(True),True,True)
			else:
				print "nincs ilyen szo a megadott fajlban"
		elif self.option == 2: # a szo utani
			if self.actWord in self.myDict:
				self.printout(self.myDict[self.actWord].statistic(False),False,True)
			else:
				print "nincs ilyen szo a megadott fajlban"
		elif self.option == 3: # ha egy adott szo tertalmazza reszszokent a megadott szot akkor az az elottiek
			tmp = {}
			for k,v in self.myDict.iteritems():
				if re.search(self.actWord,k) != None:
					tmp[k] = v.statistic(True)
			self.printout(tmp,True,False)
		elif self.option == 4: # --||-- utaniak
			tmp = {}
			for k,v in self.myDict.iteritems():
				if re.search(self.actWord,k) != None:
					tmp[k] = v.statistic(False)
			self.printout(tmp,False,False)
		elif self.option == 5: # a legjobb aranyu szoparos
			tmp = {}
			numa = 0
			numb = 0
			maximum = 0
			key = ""
			for k,v in self.myDict.iteritems():
				numa += v.getAfterCount()
				numb += v.getBeforeCount()
			for k,v in self.myDict.iteritems():
				tmp = dict(tmp.items() + v.catenate(numa,numb).items())
			for k,v in tmp.iteritems():
				if v>maximum:
					maximum = v
					key = k
			#print tmp
			print "a legsurubben elofordulo paros: ",key," elofordulasuk aranya: ",maximum,"x10^(-2) %"
			
			


a = load()
a.result()


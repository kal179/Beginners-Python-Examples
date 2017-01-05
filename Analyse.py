import math


class Analysis:
	global boole_True
	global boole_False
	boole_True = True
	boole_False = False
	
	def __init__(self, data):
		self.data = data

	def count(self, to_count):
		counter = 0
		for i in self.data:
			if i == to_count:
				counter = counter + 1
		return counter		

	def add(self):
		added = 0
		for i in self.data:
			added = added + i
		return added	

	def avg(self):
		length = len(self.data)
		add = 0
		for i in self.data:
			add = add + i 
		avg_mean = add / length
		return avg_mean 	

	def mean(self):
		meaned = []
		for i in range(len(self.data) - 1):
			a = self.data[i]
			b = self.data[i + 1]
			mean = math.sqrt(a * b)
			meaned.append(mean)
		return meaned	

	def mul(self):
		mult = 1
		for i in self.data:
			mult = mult * i 
		return mult

	def enum(self):
		a = []
		index = 0
		for i in self.data:
			tup = [index, i]
			index = index + 1
			a.append(tup)

		for i in a:
			print(tuple(i))
		return None	
							
	@classmethod
	def median(cls, data):
		if len(data) % 2 != 0:
			med = (len(data) + 1) / 2
			return data[med - 1]
		else:
			med = (len(data) + 2) / 2
			med_1 = len(data) / 2
			mea = (data[med -1] + data[med_1 -1]) / 2
			return mea 	
		
	@classmethod
	def length(cls, dat):
		counter = 0 
		for i in dat:
			counter = counter + 1
		return counter		
	
	@classmethod	
	def sqre(cls, num):
		square = num ** 2
		return square

	@classmethod    
	def isdivisible(cls, divi, get):
		if (divi % get  ==  0):
			return boole_True
		else:
			return boole_False	

	@classmethod		
	def isodd(cls, num):
 		if (num % 2  !=  0):
			return(boole_True)
		elif (num % 2  ==  0):
			return(boole_False)	

	@classmethod		
	def iseven(cls, num):
		if num % 2 == 0:
    			return(boole_True)
    		elif num % 2 != 0:
    			return(boole_False)

    	@classmethod
    	def isint(cls, data):
    		if (type(data)  ==  int):
    			return(boole_True)
    		else:
    			return(boole_False)

    	@classmethod
    	def isfloat(cls, data):
    		if (type(data)  ==  float):
    			return(boole_True)
    		else:
    			return(boole_False)

    	@classmethod
    	def isalpha(cls, data):
    		if (type(data)  ==  str):
    			return(boole_True)
    		else:
    			return(boole_False)

    	@classmethod		
    	def max(cls, data):
		maxi = 0
		for i in data:
			if ( i > maxi ):
				maxi = i
			else:
				i = i + 1
		return maxi

	@classmethod		
    	def min(cls, data):
		mini = max(data)
		for i in data:
			if ( i < mini ):
				mini = i
			else:
				i = i + 1
		return mini	
	
"""	
from analysis import Analysis
dat = [23,12,32,12,34,21,32,32,2,21,3,21,32,21,12,32,12,3,21,3,21,3,21,12]
a = Analysis(dat)
a.max(dat)
"""

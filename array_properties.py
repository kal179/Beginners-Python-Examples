

class Array(object):
	
	def __init__(self, array_list):
		self.array_list = array_list
		self.f_dict = {}

	
	def kay_sort(self):
		for i in range(len(self.array_list)):
			
			for n in range(len(self.array_list) - 1):
				a = self.array_list[n]
				
				if (a > self.array_list[i]):
					temp = self.array_list[i]
					self.array_list[i] = a 
					self.array_list[n] = temp 

		self.f_dict["Sorted List : "] =  self.array_list		
	

	def difference_in_sequence(self):
		insta = []
		for i in range(len(self.array_list) - 1):
			a = self.array_list[i]
			b = self.array_list[i + 1]
			insta.append(abs(a - b))

		self.f_dict["Sequence Difference : "] = insta
		
	def list_length(self):
		res = 0
		for i in range(len(self.array_list)):
			res += 1		
		self.f_dict["Length : "] = res

	def maximum_n(self):
		max_num = 0
		for i in range(len(self.array_list)):
			prep = self.array_list[i]
			
			for i in self.array_list:
				if (prep > i):
					max_num = prep
				
				else: pass;

		self.f_dict["Maximum number : "] = max_num	

	def minimum_n(self):	
		min_num = 0
		for j in range(len(self.array_list)):
			inst = self.array_list[j]

			for n in self.array_list:
				if (inst < n):
					min_num = inst
				
				else: pass;

		self.f_dict["Minimum number : "] = min_num

	def mean_of_arr(self):
		length = len(self.array_list)
		summed = sum(self.array_list)
		mean = float(summed / length)

		self.f_dict["Mean of Array : "] = mean 

	def median_of_arr(self):
		help_here = len(self.array_list)

		if (len(self.array_list) % 2 != 0):
			med = self.array_list[(help_here + 1) / 2]
			self.f_dict["Median of Array : "] = med 

		else :
			val_x = help_here / 2
			val_y = (help_here + 2) / 2
			median_x_y = (self.array_list[val_x] + self.array_list[self.val_y]) / 2 
			self.f_dict["Median of Array : "] = median_x_y
			
	def mode_of_array(self):
		mode_dict = {}

		for i in self.array_list:
			mode_dict[i] = self.array_list.count(i)

		self.f_dict["Mode : "] = mode_dict

	def show_props(self):
		for i in self.f_dict.keys():
			print("{}{}".format(i , str(self.f_dict[i])))			

to_test = [12, 12, 54, 234, 76,3, 34, 4 ,56, 23, 12]	
instance = Array(to_test)
instance.kay_sort()
instance.difference_in_sequence()
instance.list_length()
instance.maximum_n()
instance.minimum_n()
instance.mean_of_arr()
instance.median_of_arr()
instance.mode_of_array()
print(instance.show_props())		
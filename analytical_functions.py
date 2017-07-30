
"""
After looking at the code you might've thought that
i've used too common `Exception` everywhere!
That's because i'm too lazy to find or think about every single
exception that can occur! 
"""

"""
Changes you should make to use the class on single data set;
def __init__(self, data):
	self.data

then,
change all @classmethods to the methods operating on self.data
and also change corresponding changes
"""
import math


class AnalysisFunctions:
    @classmethod
    def count(cls, to_check, n):
        if not(isinstance(to_check, str) or isinstance(to_check, list)):
            raise TypeError("Expected a string or list, but, got a {} instead!".format(type(to_check)))
        else:
            if isinstance(to_check, str):
                to_check = [str(s) for s in to_check]
            counter = 0
            for _ in to_check:
                if _ == n:
                    counter = counter + 1
            return counter

    @classmethod
    def sum(cls, *args):
        res = 0
        try:
            for i in args:
                res += i
        except Exception as e:
            return e
        else:
            return res

    @classmethod
    def mean(cls, arr):
        try:
            average = sum(arr) / len(arr)
        except Exception as e:
            return e
        else:
            return average
    
    @classmethod
    def mean_arr(cls, li):
        res = []
        try:
            for i in range(len(li) - 1):
                a = li[i]
                b = li[i + 1]
                res.append(round(math.sqrt(a * b), 2))
        except Exception as e:
            return e
        else:
            return res
    
    @classmethod
    def mult(cls, *args):
        res = 1
        try:
            for i in args:
                res *= i
        except Exception as e:
            return e
        else:
            return res
    
    @classmethod
    def enum(cls, arr):
        res = []
        try:
            for item in arr:
                tmp = (arr.index(item), item)
                res.append(tmp)
        except Exception as e:
            return e
        else:
            return res
    
    @classmethod
    def median(cls, data):
        if not(sorted(data) == data):
            data.sort()
        res = None
        try:
            if not(len(data) % 2 == 0):
                middle = int((len(data) + 1) / 2)
                res = data[middle - 1]
            else:
                middle = int((len(data) + 2) / 2)
                middle_1 = int(len(data) / 2)
                res = (data[middle - 1] + data[middle_1 - 1]) / 2
        except Exception as e:
            return e
        else:
            return res
        
    @classmethod
    def length(cls, x):
            counter = 0
            try:
                if isinstance(x, str):
                    x = list(x)
                for i in x:
                    counter = counter + 1
            except Exception as e:
                return e
            else:
                return counter
    
    @classmethod
    def factorial(cls, n):
        try:
            if n <= 1:
                return 1
            else:
                fact = n * AnalysisFunctions().factorial(n - 1)
                return fact
        except Exception as e:
            return e
    
    @classmethod
    def sort(cls, arr):
        try:
            for i in range(len(arr)):
                for n in range(len(arr) - 1):
                    x = arr[n]
                    y = arr[n + 1]
                    if y < x:
                        tmp = x
                        arr[n] = y
                        arr[n + 1] = tmp
        except Exception as e:
            return e
    
    @classmethod
    def reverse_sort(cls, arr):
        try:
            for i in range(len(arr)):
                for n in range(len(arr) - 1):
                    x = arr[n]
                    y = arr[n + 1]
                    if y > x:
                        tmp = x
                        arr[n] = y
                        arr[n + 1] = tmp
        except Exception as e:
            return e
    
    @classmethod
    def sorted(cls, arr):
        try:
            for i in range(len(arr)):
                for n in range(len(arr) - 1):
                    x = arr[n]
                    y = arr[n + 1]
                    if y < x:
                        tmp = x
                        arr[n] = y
                        arr[n + 1] = tmp
        except Exception as e:
            return e
        else:
            return arr
    
    @classmethod
    def sqre(cls, num):
            try:
                square = num ** 2
            except Exception as e:
                return e
            else:
                return square
    
    @classmethod
    def is_divisible(cls, x, y):
        try:
            return x % y == 0
        except Exception as e:
            return e
    
    @classmethod
    def is_odd(cls, n):
        try:
            return n % 2 != 0
        except Exception as e:
            return e
    
    @classmethod
    def is_even(cls, n):
        try:
            return n % 2 == 0
        except Exception as e:
            return e
    
    @classmethod
    def max(cls, arr):
        try:
            maxi = arr[0]
            for elem in arr[1:]:
                if elem > maxi:
                    maxi = elem
        except Exception as e:
            return e
        else:
            return maxi
    
    @classmethod
    def min(cls, arr):
        try:
            mini = arr[0]
            for elem in arr[1:]:
                if elem < mini:
                    mini = elem
        except Exception as e:
            return e
        else:
            return mini
    
"""
It will be so kind to report bugs
"""
# I hate indentation problems

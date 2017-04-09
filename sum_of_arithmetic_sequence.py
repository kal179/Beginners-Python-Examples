
class ArithmeticSequence():
	def __init__ (self, seq):
		self.seq = seq 
		
	def sum(self):
		summed = len(self.seq) / 2 * (self.seq[0] + self.seq[-1])
		return summed 

test_sub = [2,4,6,8,10,12,14,16]		
print(ArithmeticSequence(test_sub).sum())		
print(sum(test_sub))

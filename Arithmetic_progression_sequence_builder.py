

class Arithmetic_progression(object):

	@staticmethod
	def arithmetic_sequence_builder(a , diff = 0, limit = 0):
		if (diff <= 0 or limit <= 0):
			return "Error Invalid Arguments For Difference or Limit"

		else:
			if (limit == a):
				return [a]
			else:
				seq = []
				for i in range(0, limit, diff):
					seq.append(i + (a - 1) * 2)	
				return seq 
# Testing			
print(Arithmetic_progression.arithmetic_sequence_builder(2, 2, 100))

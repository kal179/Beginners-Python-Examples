
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
				for i in range(a, limit + 1, diff):
					seq.append(i + (a - 1) * 2)	
				
				if (a == 0):	
					return seq[1:]
				else:
					return seq
# Testing			
print(Arithmetic_progression.arithmetic_sequence_builder(2, 2, 100))
print(Arithmetic_progression.arithmetic_sequence_builder(1, 10, 100))
print(Arithmetic_progression.arithmetic_sequence_builder(1, 5, 10000))

"""
Still Some Bugs are to be fixed algo is not perfect
like sometimes it omits first value of a in seq
and it is first term.
"""

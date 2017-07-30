# Binary Search for an array seq, search element is v, from positions l to r


def binary_search(seq,v,l,r):
	#search for v in seq[l:r], seq is sorted
	if r - l == 0:
		return(False)
	mid = (l + r) // 2 #integer division
	if v == seq[mid]:
		return (True)
	if v < seq[mid]:
		return (binary_search(seq,v,l,mid))
	else:
		return (binary_search(seq,v,mid+1,r))

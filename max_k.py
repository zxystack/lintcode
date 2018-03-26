# *-* coding: utf-8 *-* 

'''
'''

def quick_sort(l, left, right):
	if left >= right:
	    return l  
	start, end = left, right 
	key = l[left]
	while left < right: 
		while left < right and l[right] >= key:
			right -= 1
		l[left] = l[right]
		while left < right and l[left] <= key:
			left += 1
		l[right] = l[left]
	l[left] = key 
	quick_sort(l,start, left-1)
	quick_sort(l,left+1,end)
	return l 

def finder(l, k):
	k_list = l[0:k]
	result = quick_sort(k_list, 0, k-1)
	for value in l[k:]:
		if value > result[0]:
			result[0] = value 
			result = quick_sort(result, 0, k-1)
			print result 
	return result[0]

print finder([2,3,1,5,3,2, 8, 9, 11, 34, 90], 3)

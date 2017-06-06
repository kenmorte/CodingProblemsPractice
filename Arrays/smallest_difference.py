# Given two arrays of positive integers (0 or positive integers)
#	Between those two arrays, the smallest difference (one number from one array, and another number from the other array) 
#		--> find the smallest difference
#	EG. ([17, 20, 5, 42, 36], [8, 13, 0, 39, 22, 64, 51] --> 2 (between 22 and 20))

def smallest_diff(arr1, arr2):
	# Brute force: going through each index in one array --> look through all the other indeices in the other array
	#				keep track of the min difference
	#	--> O(n*m) time, O(1) space

	# Sorting: arr1 is sorted, arr2 is sorted --> O(nlogn + mlogm) --> O(nlogm) time, O(1) space
	# Sorting: arr1 is sorted, arr2 is sorted
	#	arr1 = [5, 17, 20, 36, 42]
	#	arr2 = [0, 8, 13, 22, 39, 51, 64]
	#	two pointers: starting at arr1 and arr2 at index 0 --> get their diff, compare with global min 
	#					get whichever value is min, advance that pointer forward

	# Sorting = O(nlogn + O(mlogm)), Pointer movement = O(n + m), O(n + m) space 

	if not arr1 or not arr2:
		return -1

	sorted_arr1 = sorted(arr1)
	sorted_arr2 = sorted(arr2)
	min_diff = float('inf')

	pointer1 = 0
	pointer2 = 0

	while pointer1 < len(arr1) and pointer2 < len(arr2):
		diff = abs(sorted_arr1[pointer1] - sorted_arr2[pointer2])

		if diff < min_diff:
			min_diff = diff
		if min_diff == 0:
			return 0

		if sorted_arr1[pointer1] < sorted_arr2[pointer2] and pointer1 < len(arr1):
			pointer1 += 1
		elif pointer2 < len(arr2):
			pointer2 += 1

	return min_diff

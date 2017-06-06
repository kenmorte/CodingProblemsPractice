# Implement binary search given an integer array
# 	Given integer array, integer to find --> output whether integer is inside the array
#	Array --> not guaranteed to be sorted

# [1, 2, 3], 4
def binarySearch(array, integer):
	# WE can asssume the array is sorted

	if not array:
		return False

	left = 0
	right = len(array)-1

	while left < right:
		mid = (left + right) // 2

		if array[left] == integer or array[right] == integer:
			return True

		if array[mid] == integer:
			return True
		elif array[mid] < integer:
			# push our bounbds to the right
			left = mid + 1
		else:
			# push our bounds to the left
			right = mid

	return False

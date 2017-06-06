
# given n array of integers, integers represent elevation,
#	One unit of water = 1x1
#	Each integer represents a width of 1
#	Example: [1, 2, 1, 0, 3, 2, 0, 2] --> each represent a height
#	Trap 5 units of water
#	Peaks and valleys that trap water

#	You can have millions of numbers


def getTrapsOfWater(array):
	# Pre-process the list --> to get the elevations larger to its left and right + their indices
	if not array:
		return 0

	left_bounds = []
	right_bounds = [0 for n in array]

	left_max_bound = array[0]
	right_max_bound = array[len(array)-1]
	result_sum = 0

	for i in range(len(array)):
		left_max_bound = max(array[i], left_max_bound)
		left_bounds.append(left_max_bound)

	for i in range(len(array)-1, -1, -1):
		right_max_bound = max(array[i], right_max_bound)
		right_bounds[i] = right_max_bound

	for i in range(len(array)):
		if i == 0 or i == len(array) - 1:
			continue

		min_bound = min(left_bounds[i], right_bounds[i])
		height = array[i]
		traps_of_water = min_bound - height
		result_sum += traps_of_water

	return result_sum

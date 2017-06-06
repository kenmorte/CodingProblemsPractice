function modifyArray(orig_array, indexOfElementToChange, newElement) {
	// Return the new array
	// index GUARANTEED to be inside the array

	var result = [];

	for (var i = 0; i < orig_array.length; i++) {
		if (i == indexOfElementToChange)
			result.push(newElement);
		else
			result.push(orig_array[i]);
	}
	return result;
}

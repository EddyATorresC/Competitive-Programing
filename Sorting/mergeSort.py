# Written by Eddy Torres
# Merge sort function increasing
# It recieves an array x of numbers
# It sorts the array x in incresing order
# Example of usage:
# x = [5, 2, 1, 3, 4, 6]
# mergeSort(x)
# output: [1, 2, 3, 4, 5, 6]

def mergeSort(x):
	if len(x) > 1:

		# Finding the mid of the array
		mid = len(x)//2

		# Dividing the array elements into 2 halves
		L = x[:mid]
		R = x[mid:]

		# Sorting the first half & second half
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0

        #Merge section
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				x[k] = L[i]
				i += 1
			else:
				x[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			x[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			x[k] = R[j]
			j += 1
			k += 1


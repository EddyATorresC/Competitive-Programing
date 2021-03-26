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
			if L[i] > R[j]:
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

def decreasing(x):
    for j in range(1,len(x)):
        key = x[j]
        i = j-1 #dummy index
        while(i >= 0 and x[i] < key):
            x[i+1] = x[i]
            i = i-1
        x[i+1] = key
    return x

n,m = input().split()
n = int(n)
m = int(m)
difference = []
total = 0
for i in range(0,n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    total += a
    difference.append(a - b)

difference = decreasing(difference)

minimum = 0

if total <= m:
    print("0")
else:
    for val in difference:
        minimum += 1
        total = total - val
        if total <= m:
            break
    
    if total > m:
        print("-1")
    else:
        print(minimum)
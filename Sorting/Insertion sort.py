# Written by Jose Ocampo
# Insertion sort function increasing 
# It recieves an numpy array x of numbers 
# It returns the array x sorted in incresing order 
# Example of usage: 
# x = [5, 2, 1, 3, 4, 6]
# increasing(x)
# output: [1, 2, 3, 4, 5, 6]

def increasing(x):
    for j in range(1,len(x)):
        key = x[j]
        i = j-1
        while(i >= 0 and x[i] > key):
            x[i+1] = x[i]
            i = i-1
        x[i+1] = key
    return x 
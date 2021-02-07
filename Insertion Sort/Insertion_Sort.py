def insertionSort(arr): 
 
	for i in range(1, len(arr)): 

		key = arr[i] 

		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key 


# Driver code 
arr = [18, 25, 3, 4, 9, 5, 8] 
insertionSort(arr) 
print ("The Sorted array: ") 
for i in range(len(arr)): 
	print ("%d" %arr[i]) 


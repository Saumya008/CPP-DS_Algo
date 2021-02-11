def partition(arr, low, high): 
    i = (low-1)         
    pivot = arr[high]    
  
    for j in range(low, high): 
        if arr[j] <= pivot: 
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
# The main function
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
  
# Driver code
arr = [8,77,25,63,48,12] 
n = len(arr) 
quickSort(arr, 0, n-1) 
print("The Sorted array:") 
for i in range(n): 
    print("%d" % arr[i])
#include <iostream>

using namespace std;

void heapsort(int arr[], int n, int i)
{
	int largest = i; 
	int l = 2 * i + 1;
	int r = 2 * i + 2;

	if (l < n && arr[l] > arr[largest])
		largest = l;

	if (r < n && arr[r] > arr[largest])
		largest = r;

	if (largest != i) {
		swap(arr[i], arr[largest]);

		heapsort(arr, n, largest);
	}
}

void Sort(int arr[], int n)
{
	
	for (int i = n / 2 - 1; i >= 0; i--)
		heapsort(arr, n, i);

	for (int i = n - 1; i > 0; i--) {
		swap(arr[0], arr[i]);
		heapsort(arr, i, 0);
	}
}

void printArray(int arr[], int n)
{
	for (int i = 0; i < n; ++i)
		cout << arr[i] << " ";
	cout << "\n";
}

// Driver code
int main()
{
	int arr[] = { 10,8,55,12,64,23};
	int n = sizeof(arr) / sizeof(arr[0]);

	Sort(arr, n);

	cout << "Sorted array is \n";
	printArray(arr, n);
}

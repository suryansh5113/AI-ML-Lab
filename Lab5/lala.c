#include <stdio.h>
#include <stdlib.h>  // for malloc and free

// Function prototypes
int merge_and_count(int arr[], int temp[], int left, int mid, int right);
int merge_sort_and_count(int arr[], int temp[], int left, int right);

// Function to merge two halves and count comparisons
int merge_and_count(int arr[], int temp[], int left, int mid, int right) {
    int i = left;    // Starting index for left subarray
    int j = mid + 1; // Starting index for right subarray
    int k = left;    // Starting index to be sorted
    int comparison_count = 0;

    // Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
        comparison_count++; // Count each comparison
    }

    // Copy the remaining elements of left subarray, if any
    while (i <= mid) {
        temp[k++] = arr[i++];
    }

    // Copy the remaining elements of right subarray, if any
    while (j <= right) {
        temp[k++] = arr[j++];
    }

    // Copy the sorted subarray into original array
    for (i = left; i <= right; i++) {
        arr[i] = temp[i];
    }
    
    return comparison_count;
}

// Recursive function to implement merge sort and count comparisons
int merge_sort_and_count(int arr[], int temp[], int left, int right) {
    int mid, comparison_count = 0;
    if (left < right) {
        mid = (left + right) / 2;

        // Count comparisons in left and right subarrays
        comparison_count += merge_sort_and_count(arr, temp, left, mid);
        comparison_count += merge_sort_and_count(arr, temp, mid + 1, right);

        // Count comparisons during the merge step
        comparison_count += merge_and_count(arr, temp, left, mid, right);
    }
    return comparison_count;
}

int main() {
    int n;
    
    // Input number of students
    scanf("%d", &n);

    // Dynamically allocate arrays for marks and temporary array for sorting
    int *arr = (int *)malloc(n * sizeof(int));
    int *temp = (int *)malloc(n * sizeof(int));

    // Input marks of each student
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Sorting and counting comparisons
    int comparison_count = merge_sort_and_count(arr, temp, 0, n - 1);

    // Output sorted marks
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Output total number of comparisons
    printf("%d\n", comparison_count);

    // Free dynamically allocated memory
    free(arr);
    free(temp);

    return 0;
}

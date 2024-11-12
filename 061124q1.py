import pyautogui
import time

# Delay to switch to the target window
time.sleep(10)

# Text to be typed
code = """
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to store song information
typedef struct {
    long long length;
    int band;
} Song;

// Compare function for sorting
int compare(const void* a, const void* b) {
    Song* s1 = (Song*)a;
    Song* s2 = (Song*)b;
    // Sort by length in descending order
    if (s1->length < s2->length) return 1;
    if (s1->length > s2->length) return -1;
    return 0;
}

// Function to calculate maximum sweetness
long long calculateMaxSweetness(Song* songs, int n) {
    // Sort songs by length in descending order
    qsort(songs, n, sizeof(Song), compare);
    
    // Initialize variables for tracking bands and sweetness
    int* bands = (int*)calloc(100001, sizeof(int));  // Array to track unique bands
    int uniqueBands = 0;
    long long totalSweetness = 0;
    
    // Process each song
    for (int i = 0; i < n; i++) {
        // If this is a new band, increment unique bands count
        if (bands[songs[i].band] == 0) {
            uniqueBands++;
            bands[songs[i].band] = 1;
        }
        // Add sweetness for current song
        totalSweetness += songs[i].length * uniqueBands;
    }
    
    free(bands);
    return totalSweetness;
}

int main() {
    int t;
    scanf("%d", &t);  // Number of test cases
    
    while (t--) {
        int n;
        scanf("%d", &n);  // Number of songs
        
        // Allocate memory for songs
        Song* songs = (Song*)malloc(n * sizeof(Song));
        
        // Read song information
        for (int i = 0; i < n; i++) {
            scanf("%d %lld", &songs[i].band, &songs[i].length);
        }
        
        // Calculate and print result
        long long result = calculateMaxSweetness(songs, n);
        printf("%lld\n", result);
        
        // Free allocated memory
        free(songs);
    }
    
    return 0;
}
"""

# Type the code
pyautogui.write(code)

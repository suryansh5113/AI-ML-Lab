import pyautogui
import time

# Delay to switch to the target window
time.sleep(10)

# Text to be typed
code = """
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int start;
    int end;
    int compartment;
} Customer;

int compare(const void *a, const void *b) {
    Customer *c1 = (Customer *)a;
    Customer *c2 = (Customer *)b;
    return c1->end - c2->end;
}

int main() {
    int T;
    scanf("%d", &T);
    
    while (T--) {
        int N, K;
        scanf("%d %d", &N, &K);
        
        Customer customers[N];
        for (int i = 0; i < N; i++) {
            scanf("%d %d %d", &customers[i].start, &customers[i].end, &customers[i].compartment);
        }
        
        // Sort customers by end time to prioritize the earliest finish times
        qsort(customers, N, sizeof(Customer), compare);
        
        // Array to store the last end time for each compartment
        int last_end[K + 1];
        for (int i = 0; i <= K; i++) {
            last_end[i] = -1;
        }
        
        int max_customers = 0;
        
        for (int i = 0; i < N; i++) {
            int comp = customers[i].compartment;
            if (customers[i].start >= last_end[comp]) {
                // If the compartment is free, accept this customer
                max_customers++;
                last_end[comp] = customers[i].end;
            }
        }
        
        // Print the result for the current test case
        printf("%d\n", max_customers);
    }
    
    return 0;
}


"""

# Type the code
pyautogui.write(code)

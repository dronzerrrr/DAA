import random
import time

# -----------------------------
# DETERMINISTIC QUICK SORT
# -----------------------------
def deterministic_quicksort(arr, low, high):
    if low < high:
        # Partition around the last element
        pivot_index = deterministic_partition(arr, low, high)
        # Sort before and after pivot
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

def deterministic_partition(arr, low, high):
    pivot = arr[high]  # pivot = last element
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap smaller elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # place pivot correctly
    return i + 1


# -----------------------------
# RANDOMIZED QUICK SORT
# -----------------------------
def randomized_quicksort(arr, low, high):
    if low < high:
        # Pick a random pivot index
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # move pivot to end

        # Partition the array
        pivot_index = deterministic_partition(arr, low, high)

        # Sort before and after pivot
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def analyze_quicksort():
    # Take array input from user
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the elements separated by space: ").split()))

    print("\nOriginal array:", arr)

    # Make copies for both versions
    arr_det = arr.copy()
    arr_rand = arr.copy()

    # --- Deterministic Quick Sort ---
    start = time.time()
    deterministic_quicksort(arr_det, 0, n - 1)
    end = time.time()
    det_time = end - start

    # --- Randomized Quick Sort ---
    start = time.time()
    randomized_quicksort(arr_rand, 0, n - 1)
    end = time.time()
    rand_time = end - start

    # --- Print results ---
    print("\nSorted array using Deterministic Quick Sort:", arr_det)
    print("Sorted array using Randomized Quick Sort:   ", arr_rand)

    print("\n--- Time Analysis ---")
    print(f"Deterministic Quick Sort: {det_time:.6f} seconds")
    print(f"Randomized Quick Sort:    {rand_time:.6f} seconds")


# -----------------------------
# PROGRAM STARTS HERE
# -----------------------------
if __name__ == "__main__":
    analyze_quicksort()

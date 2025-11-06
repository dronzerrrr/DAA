# # 0-1 Knapsack Problem using Dynamic Programming
# 
# def knapsack(W, wt, val, n):
#     # Create a 2D DP table
#     dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
# 
#     # Build the table bottom-up
#     for i in range(1, n + 1):
#         for w in range(1, W + 1):
#             if wt[i - 1] <= w:
#                 # Choose max of including or excluding the current item
#                 dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
#             else:
#                 # If item weight is more than current capacity, skip it
#                 dp[i][w] = dp[i - 1][w]
# 
#     # The last cell will have the maximum value
#     return dp[n][W]
# 
# # Example input
# val = [60, 100, 120]   # Values of items
# wt = [10, 20, 30]      # Weights of items
# W = 50                 # Maximum weight of knapsack
# n = len(val)
# 
# # Function call
# max_value = knapsack(W, wt, val, n)
# print("Maximum value that can be put in knapsack is:", max_value)
# 
# ## 0-1 Knapsack Problem using Dynamic Programming
# ----------------------------------------------
# This program finds the maximum total value that can be carried in a knapsack
# and also shows which items are included in the optimal solution.

def knapsack(W, wt, val, n):
    # Create DP table (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                # Either include the item or exclude it — choose the better one
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                # Cannot include item if it exceeds capacity
                dp[i][w] = dp[i - 1][w]

    # Now, find which items are included
    res = dp[n][W]   # final maximum value
    w = W
    items_taken = []

    for i in range(n, 0, -1):
        # If the value comes from including this item, record it
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            # Item not included
            continue
        else:
            # Item included
            items_taken.append(i)
            res -= val[i - 1]
            w -= wt[i - 1]

    items_taken.reverse()  # to show items in original order
    return dp[n][W], items_taken


# -------- Main Program --------
n = int(input("Enter number of items: "))

val = []
wt = []

print("\nEnter value and weight of each item:")
for i in range(n):
    v = int(input(f"Value of item {i + 1}: "))
    w = int(input(f"Weight of item {i + 1}: "))
    val.append(v)
    wt.append(w)

W = int(input("\nEnter maximum capacity of knapsack: "))

# Solve Knapsack
max_value, items_taken = knapsack(W, wt, val, n)

# Display result
print("\nMaximum value that can be put in knapsack is:", max_value)
print("Items included are:", items_taken)

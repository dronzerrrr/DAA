# --------------------------------------------------------
# N-Queens Problem using Backtracking (Detailed Explanation)
# --------------------------------------------------------
# Goal: Place N queens on an N×N chessboard so that
#       no two queens attack each other.
# Queens attack in same row, same column, and diagonals.
# --------------------------------------------------------

def print_board(board):
    """
    Function to print the chessboard.
    Each cell is either '.' (empty) or 'Q' (queen placed).
    """
    for row in board:
        print(" ".join(row))
    print()  # Empty line after each solution


def is_safe(board, row, col, n):
    """
    Function to check if a queen can be safely placed
    at position (row, col) on the chessboard.
    """

    # ---- Check column (same column, previous rows) ----
    for i in range(row):
        if board[i][col] == 'Q':  # Queen already placed in this column
            return False

    # ---- Check upper-left diagonal ----
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':    # Queen found on diagonal
            return False
        i -= 1
        j -= 1

    # ---- Check upper-right diagonal ----
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':    # Queen found on diagonal
            return False
        i -= 1
        j += 1

    # If no conflicts found, it's safe to place a queen here
    return True


def solve_nqueens(board, row, n):
    """
    Recursive function to place queens one by one in different rows.
    """
    # ---- Base Case ----
    # If all queens are placed successfully, print the solution
    if row == n:
        print("Solution:")
        print_board(board)
        return True

    # ---- Recursive Case ----
    # Try placing queen in each column of the current row
    found_solution = False  # To check if at least one solution exists
    for col in range(n):
        # Check if it's safe to place queen at (row, col)
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'   # Place the queen

            # Move to the next row (recursive call)
            found_solution = solve_nqueens(board, row + 1, n) or found_solution

            # Backtrack: Remove the queen if it leads to no solution
            board[row][col] = '.'

    # Return True if any solution found, otherwise False
    return found_solution


# -------- Main Program --------
# Step 1: Take input for number of queens
n = int(input("Enter number of queens (N): "))

# Step 2: Create an empty N×N chessboard filled with '.'
board = [['.' for _ in range(n)] for _ in range(n)]

# Step 3: Call the solver function
if not solve_nqueens(board, 0, n):
    print("No solution exists for N =", n)

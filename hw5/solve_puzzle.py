def solve_puzzle(board, current_index=0, visited=None, move_sequence=None, memo=None):
    """
    Determines if a jumping puzzle is solvable and returns the solution path.

    Args:
        board: A list of integers representing allowed jump distances from each index.
        current_index: The starting index (default: 0).
        visited: A set to track visited indices (default: None).
        move_sequence: The current sequence of moves (default: None).
        memo: A dictionary for storing results (default: None).

    Returns:
        A tuple:
            * True if the puzzle is solvable, False otherwise.
            * A list of move indices representing the solution path, or an empty list if unsolvable.
    """

    if visited is None:
        visited = set()
    if move_sequence is None:
        move_sequence = []
    if memo is None:
        memo = {}

    if current_index in memo:
        return memo[current_index]

    if current_index == len(board) - 1:  # Base case: Reached the end
        return True, move_sequence + [current_index]

    if current_index in visited:  # Avoid infinite loops
        return False, []

    visited.add(current_index)
    move_sequence.append(current_index)

    for direction in (1, -1):  # Try clockwise and counterclockwise
        next_index = (current_index + direction * board[current_index]) % len(board) # current index, adds and populates. Will wrap arround due to % len(board)
        solvable, moves = solve_puzzle(board, next_index, visited.copy(), move_sequence.copy(), memo)
        if solvable:
            memo[current_index] = (True, moves)
            return True, moves

    memo[current_index] = (False, [])  # If unsolvable
    return False, []

from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.

    def valid(row):
        holder = [0] * 10 # for easier indexing
        for i in row:
            if i == 0:
                continue
            if i == holder[i]:
                return False
            else:
                holder[i] = i
        return True

    def valid_block(block_x, block_y):
        holder = [0] * 10
        for x in range(block_x, block_x + 3):
            for y in range(block_y, block_y + 3):
                num = partial_assignment[x][y]
                if num == 0:
                    continue
                if num == holder[num]:
                    return False
                else:
                    holder[num] = num
        return True

    n = len(partial_assignment)
    
    # check rows and cols
    for x in range(n):
        if not valid(partial_assignment[x]) or not valid([partial_assignment[y][x] for y in range(n)]):
            return False
    
    # check blocks
    for x in range(0, n, 3):
        for y in range(0, n, 3):
            if not valid_block(x, y):
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))

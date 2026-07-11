class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (i, j) 
        # subsquare -> i//3 + 3 + j//3
        # e.g. (4, 2) -> 4//3 * 3 + 2//3 = (1 * 3)+ 0 = 3
        # e.g. (5, 3) -> 5//3 * 3 + 3//3 = (1 * 3)+ 1 = 4
        # e.g. (2, 2) -> 2//3 * 3 + 2//3 = (0 * 3)+ 0 = 0
        r_set, c_set, s_set = [], [], []
        for i in range(9):
            r_set.append(set())
            c_set.append(set())
            s_set.append(set())
        for i in range(len(board)):
            for j in range(len(board[i])):
                sub = ((i//3) * 3) + j//3
                e = board[i][j]
                if e == ".": continue
                if e not in r_set[i] and e not in c_set[j] and e not in s_set[sub]:
                    r_set[i].add(e)
                    c_set[j].add(e)
                    s_set[sub].add(e)
                else:
                    return False
        return True
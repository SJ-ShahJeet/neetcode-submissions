class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}

        for i in range(9):
            rows, cols = set(), set()

            for j in range(9):
                rblock = board[i][j]
                cblock = board[j][i]
                box = (i // 3, j // 3)

                if rblock != ".":
                    if box not in boxes:
                        boxes[box] = set()

                    if rblock in rows or rblock in boxes[box]:
                        return False

                    rows.add(rblock)
                    boxes[box].add(rblock)

                if cblock != ".":
                    if cblock in cols:
                        return False
                    cols.add(cblock)

        return True
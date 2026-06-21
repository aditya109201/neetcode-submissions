class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                box = (r // 3, c // 3)

                if (r, value) in rows or (c, value) in cols or (box, value) in boxes:
                    return False

                rows.add((r, value))
                cols.add((c, value))
                boxes.add((box, value))

        return True
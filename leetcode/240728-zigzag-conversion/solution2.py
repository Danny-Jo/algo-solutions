def convert(s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for c in s:
            rows[current_row] += c

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1 # if numRows가 4이면 0, 1, 2, 3, 2, 1, 0, 1..반복

        return ''.join(rows)

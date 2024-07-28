def convert(s: str, numRows: int) -> str:
        if(numRows  < 2):
            return s
        
        rows = ['' for _ in range(numRows)]
        current_row = 0
        direction = 'down'

        for c in s:
            rows[current_row] += c

            if current_row == numRows - 1:
                 direction = 'up'
            elif current_row == 0:
                 direction = 'down'
            if direction == 'down':
                 current_row += 1
            else:
                 current_row -= 1

        return ''.join(rows)
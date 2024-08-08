from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # east, south, west, north
        current_direction = 0
        r, c = rStart, cStart
        result = []
        steps = 1

        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    if is_valid(r, c):
                        result.append([r, c])
                    r += directions[current_direction][0]
                    c += directions[current_direction][1]
                current_direction = (current_direction + 1) % 4
            steps += 1

        return result

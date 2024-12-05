class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Initialize pointers for both strings and get their length.
        i, j, n = 0, 0, len(start)

        # Loop until we reach the end of both strings.
        while (i < n or j < n):
            # Skip all underscores ('_') in the `start` string.
            while (i < n and start[i] == "_"):
                i += 1
            # Skip all underscores ('_') in the `target` string.
            while (j < n and target[j] == "_"):
                j += 1

            # If one pointer reaches the end of the string but the other does not, break.
            if (i == n or j == n):
                break

            # If the pieces at the current positions don't match, return False.
            if (start[i] != target[j]):
                return False

            # If the current piece is 'L', it cannot move to the right (i < j).
            if (start[i] == "L" and i < j):
                return False

            # If the current piece is 'R', it cannot move to the left (j < i).
            if (start[i] == "R" and j < i):
                return False
            
            # Move both pointers forward to check the next piece.
            i += 1
            j += 1

        # Ensure both pointers reach the end of their respective strings.
        return i == n and j == n

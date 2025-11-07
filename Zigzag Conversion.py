class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: if only one row, the string remains the same
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list for each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False
        
        # Traverse the string
        for char in s:
            rows[cur_row] += char
            # Change direction if we are at the first or last row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1
        
        # Join all rows to get the final string
        return ''.join(rows)

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n == 0:
            return 0
        else:
            while n > 0:
                n = n//5
                count += n
        return count
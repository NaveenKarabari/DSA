class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sums=[]
        for row in accounts:
            sums.append(sum(row))
        return max(sums)
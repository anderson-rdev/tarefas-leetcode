from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        teste = {} 
        for index, i in enumerate(nums):
            if i in teste:
                return [teste[i], index]
            teste[target - i] = index

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Saída esperada: [0, 1]

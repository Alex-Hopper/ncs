class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, currentSum):
            if currentSum > target or i >= len(nums):
                return
            if currentSum == target:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i, currentSum + nums[i])
            
            subset.pop()
            dfs(i + 1, currentSum)

        dfs(0, 0)
        return res
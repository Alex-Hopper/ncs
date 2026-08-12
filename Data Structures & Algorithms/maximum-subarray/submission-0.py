class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)

        cur = 0
        i = 0
        while i < len(nums):
            cur += nums[i]
            res = max(res, cur)
            cur = max(cur, 0)
            i += 1

        return res
        
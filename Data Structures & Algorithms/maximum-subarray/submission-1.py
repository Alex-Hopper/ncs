class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)

        cur = 0
        for num in nums:
            cur += num
            res = max(res, cur)
            cur = max(cur, 0)

        return res
        
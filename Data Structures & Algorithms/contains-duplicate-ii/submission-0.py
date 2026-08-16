class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if len(nums) <= k + 1:
        #     return len(list(set(nums))) != len(nums)

        # seen = set(nums[0:k])

        # i = k
        # while i < len(nums):
        #     if nums[i] in seen:
        #         return True
            
        #     seen.remove(nums[i - k])
        #     i += 1

        # return False


        counts = defaultdict(int)

        for i in range(len(nums)):
            n = nums[i]

            if counts[n] > 0:
                return True
            
            counts[n] += 1
            
            if i - k >= 0:
                counts[nums[i - k]] -= 1
            
        return False
            
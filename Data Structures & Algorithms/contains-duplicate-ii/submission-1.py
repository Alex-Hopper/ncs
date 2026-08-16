class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counts = defaultdict(int)

        for i in range(len(nums)):
            n = nums[i]

            if counts[n] > 0:
                return True
            
            counts[n] += 1
            
            if i - k >= 0:
                counts[nums[i - k]] -= 1
            
        return False
            
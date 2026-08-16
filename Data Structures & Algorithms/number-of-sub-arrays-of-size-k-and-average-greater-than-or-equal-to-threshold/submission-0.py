class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curAvg = sum(arr[0:k]) / k
        res = 1 if curAvg >= threshold else 0
        for r in range(k, len(arr)):
            curAvg -= arr[r - k] / k
            curAvg += arr[r] / k

            if curAvg >= threshold:
                res += 1

        return res
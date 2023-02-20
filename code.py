class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sorted(nums1)
        ans = bnft = 0 
        for x, y in zip(nums1, nums2): 
            ans += abs(x - y)
            k = bisect_left(s1, y)
            if k < len(s1): bnft = max(bnft, abs(x - y) - (s1[k] - y)) # benefit of replacing x to s1[k]
            if 0 < k: bnft = max(bnft, abs(x - y) - (y - s1[k-1])) # benefit of replacing x to s1[k-1]
        return (ans - bnft) % 1_000_000_007




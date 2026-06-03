class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preProduct = 1
        sufProduct = 1
        prefix = []
        suffix = []
        for i in range(n):
            prefix.append(preProduct)
            preProduct *= nums[i]
            suffix.append(sufProduct)
            sufProduct *= nums[n - i - 1]
        print(prefix, suffix)
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[n - i - 1])
        return res
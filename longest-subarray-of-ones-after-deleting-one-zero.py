class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # zero_index = []
        n = len(nums)
        # for i in range(n):
        #     if nums[i] == 0:
        #         zero_index.append(i)
        
        # print(zero_index)
        # if not zero_index:
        #     return n-1
        
        # if len(zero_index) == n:
        #     return 0
        
        # res = 0
        # for i in zero_index:
        #     dp = nums.copy()
        #     dp.pop(i)
        #     print(dp)
        #     r = 0
        #     for i in range(len(dp)):
        #         if dp[i] == 1:
        #             r += 1
        #         else:
        #             res = max(res,r)
        #             r = 0
        #     res = max(res,r)
        # return res

        z = False
        l,res = 0,0

        for r in range(n):
            if nums[r] == 0:
                while z:
                    if nums[l] == 0:
                        z = False
                    l += 1
                z = True
            res = max(res,r-l)
        return res
                
        


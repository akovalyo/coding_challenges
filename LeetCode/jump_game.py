class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums) - 1
        last_ind = length
        for i in range(length, -1, -1):
            if nums[i] + i >= last_ind:
                last_ind = i
        return last_ind == 0
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        curr = sum(nums) // k
        nums.sort()
        cnt = 0

        l,  r = 0, len(nums)-1
        while l <= r:
            remain = curr - nums[r]
            r -= 1
            cnt += 1

            if l <= r and remain >= nums[l]:
                l += 1
        
        return cnt == k
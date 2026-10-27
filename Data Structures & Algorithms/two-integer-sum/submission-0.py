class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for i in range(len(nums)):
            r = target - nums[i]
            if r in H:
                return [H[r], i]
            H[nums[i]] = i
  
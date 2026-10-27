class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        H = {}
        for i in range(len(numbers)):
            r  = target - numbers[i]
            if r in H:
                return[H[r], i + 1]
            H[numbers[i]] = i + 1
        
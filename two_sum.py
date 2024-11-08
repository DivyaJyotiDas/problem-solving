class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        for outer in range(start, len(nums)):
            next = outer + 1
            for inner in range(next, len(nums)):
                if nums[outer] + nums[inner] == target:
                    return [outer, inner]
        

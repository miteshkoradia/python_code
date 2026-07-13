from typing import List

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[nums[i]] = i
        # return empty if not found 
        return []

    def twoSum_sorted_nums(self, nums: List[int], target: int) -> List[int]:
        low = 0 
        high = len(nums) - 1 
        while low < high:
            sum = nums[low] + nums[high]
            if sum == target:
                return [low+1, high+1]
            elif sum < target:
                low += 1
            else:
                high -= 1
        return [ -1 , -1]


             

def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)    
    print(result)
    result = Solution().twoSum_sorted_nums(nums, target)    
    print(result)




if __name__ == "__main__":
    main()

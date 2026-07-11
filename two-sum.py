from typing import List


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


def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()

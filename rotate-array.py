from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[k:],nums[:k] = nums[:-k],nums[-k:]
        return nums



def main():
    print(Solution().rotate(nums=[1,2,3,4,5,6,7], k=3))


if __name__ == "__main__":
    main()



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for _ in range(k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

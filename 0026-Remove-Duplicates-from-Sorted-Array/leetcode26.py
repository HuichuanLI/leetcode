class Solution:
    def removeDuplicates(self, nums) -> int:
        a = set()
        i = 0
        while i < len(nums):
            if nums[i] in a:
                 nums.pop(nums[i])
            else:
                a.add(nums[i])
                i += 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1,1]
    print(s.removeDuplicates(nums))
    print(nums)

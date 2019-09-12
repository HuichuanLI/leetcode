class Solution:
    def removeDuplicates(self, nums) -> int:
        a = set()
        i = 0
        while i < len(nums):
            if nums[i] in a:
                nums.pop(nums[i])
            else:
                a.add(i)
                i += 1
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


class Solution3:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        tmp_num = None
        for idx in range(len(nums) - 1, -1, -1):
            if tmp_num != nums[idx]:
                tmp_num = nums[idx]
            else:
                del nums[idx]

        return len(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1]
    print(s.removeDuplicates(nums))
    print(nums)

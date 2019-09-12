# 时间复杂度: O(N^2) 空间复杂度: O(1)
class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        while i < len(nums):
            if (nums[i] == val):
                nums.pop(i)
            else:
                i += 1
        return len(nums)

# 时间复杂度: O(N) 空间复杂度: O(1)

class Solution2:
    def removeElement(self, nums, val: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums[idx] = nums[-1]
                del nums[-1]
            else:
                idx += 1
        return len(nums)

if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    s = Solution().removeElement(nums, val)
    print(s)

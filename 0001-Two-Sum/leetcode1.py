class Solution:
    def twoSum(self, nums, target) :
        a = {}
        for i in range(len(nums)):
           a[nums[i]] = i
        for i in a.keys():
            if target - i in a.keys():
                return [a[i],a[target - i]]


if __name__ == '__main__':
    a = [1,2,3,4,5]
    b = Solution()
    print(b.twoSum(a,7))




class Solution:
   ## time complexity O(n^2)  using nested loop
    def unenhnacedtwoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        ret = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    ret.append(i)
                    ret.append(j)

        return ret

    ## time complexiy O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}

        for i , v in enumerate(nums):
            if target-v in hm:
                return i , hm[target-v]
            else:
                hm[v] = i 

if __name__ == '__main__':
    solution = Solution()

    nums = [2,7,11,15]
    target = 9

    print("unenhanced solution", solution.unenhnacedtwoSum(nums, target))
    print("unenhanced solution", solution.twoSum(nums, target))
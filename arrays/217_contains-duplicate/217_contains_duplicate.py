class Solution:
    ## time complexity O(n^2) as we use nested loop
    def UnenhancedcontainsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                else:
                    continue

        return False
    ## time complexity O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
    

if  __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,1]

    print("Direct solution ", solution.UnenhancedcontainsDuplicate(nums))

    print("Enhanced Solution", solution.containsDuplicate(nums))
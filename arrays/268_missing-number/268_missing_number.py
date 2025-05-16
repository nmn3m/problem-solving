class Solution:
    def unenhancedmissingNumber(self, nums: list[int]) -> int:
        ## time complexity O(nlogn)
        nums.sort()

        for i, v in enumerate(nums):
            if i != v:
                return (v-1)
            if v == len(nums) -1:
                return v+1
    
    ## time complexity 
    ### sum O(n)
    ### len O(1)

    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
            
if __name__ == '__main__':
    solution = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print("Unenhanced solutions", solution.unenhancedmissingNumber(nums))
    print("enhanced solution", solution.missingNumber(nums))



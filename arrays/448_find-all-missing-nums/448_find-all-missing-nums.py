class Solution:
    ## time complexity O(n)
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set_nums = set(nums)
        ret = []
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                ret.append(i)
        return ret


if __name__ == '__main__':
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print("unenhaced solution", solution.findDisappearedNumbers(nums))

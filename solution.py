class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        #print(val)
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            #print(nums)
        return i

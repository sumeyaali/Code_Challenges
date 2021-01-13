class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #         loop through the list
        p1 = 0
#         first pointer starts at index 0
        for i in range(1,len(nums)): 
#             loop through the list starting at index 1
            if nums[i] != nums[p1]:
#         if the value of i is the not the same as value of p1, then its two unique numbers
                p1 += 1
#              increment p1 to the next value
            nums[p1] = nums[i]
#     else if the value next to eachother are the same, then it is a dupliate and set the nums[p1] to be the value of te current number               
        return p1 + 1 
        
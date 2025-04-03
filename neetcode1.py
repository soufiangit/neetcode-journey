'''
neetcode problem 1 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we need to see if there is a duplicate in the array. We should scan the whole list. 
        #We need to have a memory that says, ok I seen the number 1, so I am going to store it. 
        # We can create a new list, by adding elements from the original list, unless it already exists.
        # then we can compare the two lists, and if they are false, then it must be that there is a dupe.
        result = []
        # this is our memory
        for i in nums:
            if i not in result:
                result.append(i)
        print (result)
        print (nums)


        if result != nums:
            return True
        else:
            return False 
            it worked. the date on this attempt is 4/3/2025
            ''' 
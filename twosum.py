class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # how as a human I would solve this problem?
        # first i would create a memory . I need to first create a memory of where each element is in thelist
        # then i need to add each item in the list to see if it reaches the target value
        # first , you add the first value and keep going until you get the target value. If none
        # of the values after the first go with the first value, then you move onto the second. 
        #abort no dict 

    
       
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    
                    return ([i,j])
                
                        
                
                elif nums[0] + nums[1] == target:
                    
                    
                    return ([0,1])
        # we didnt get 5,5 right because we didnt account for the test case of multiples of two. 
            
        # it appears as if my previous dictionary method did not work. I brute forced this one and it worked.
        # ITs not optimal at all. and I feel like I totally forgot the fact that I you cant have dupplicate values
        # in a dict. 

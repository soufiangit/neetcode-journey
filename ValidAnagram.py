class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # understand- I need to see if the first string has the same letters as the second string.
        # as a human, first i read the first string, then remember each letter and how many times i
        #it occurs. then I take this remembered data and see if it matches the second string, with 
        #letters present and the amount of each letter available. 
        # i can do this by making hashmaps of each string. if the hashmaps are the same, then its true.

        # try another way
        # convert the strings into two lists. sort the lists. then compare if the two lists are the same.

        s = sorted(list(s))
        t = sorted(list(t))

        if s == t:
            return True
        else:
            return False 

        

    #Solved using the sorting solution. So i first i tried to do some hashmap thing, but i clearly didnt understand it.
    # ig im dumb. so I did a sorting thing and it worked ig


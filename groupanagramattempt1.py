class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we need to group anagrams together into sublists. 
        # first we can use the isAnagram from the previous problem. 
        # first we need to turn each element in the array into its set
        # then we can ensure each sublist is a set. 
        # then we can do a brute force thing to see which sets equal each other. then add those sets in 
        #their own list. Then combine 
        result = []
        result1 = []
        sublist = []
        

        for i in range(len(strs)):
            result.append((strs[i]))
        
        result = sorted(result)

        for i in range(len(result)):
            for k in range(i +1 , len(result)):
                if set(result[i]) == set(result[k]):
                   
                    sublist.append(result[i] )
                    sublist.append(result[k])
                    result1.append(sublist)
                    sublist = []
        print (result1)
                    
        class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        
        # 

        print (result)

        #my idea didn't work. no clue why. not gonna try figuring out, but ill type my understanding of the solution below.
        # default dict works because firstly we need 
        # dang i have no clue maybe i will just do the easies here then once i get them all done ill try the mediums.
        
            

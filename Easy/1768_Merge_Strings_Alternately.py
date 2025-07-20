class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l1=len(word1)
        l2=len(word2)

        
        # Getting delta in size of strings if any
        
        spaces=abs(l1-l2)
        if l1>l2:
            word2=word2+' '*spaces
        elif l2>l1:
            word1=word1+' '*spaces
        
        # Iterating through max length
        
        max_len=max(l1,l2)
        lst=[]
        for each_index in range(max_len):
            lst.append(word1[each_index])
            lst.append(word2[each_index])
        
        merged_string=''.join(lst)
        merged_string=merged_string.replace(' ','')
        
        return merged_string
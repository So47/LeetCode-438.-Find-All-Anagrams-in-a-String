class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        indices = []
        i = 0
        
        while i <= len(s):
            s_counter = Counter(s[i:len(p)+i])
            if p_counter == s_counter:
                indices.append(i)
            i+=1    
        return indices
        

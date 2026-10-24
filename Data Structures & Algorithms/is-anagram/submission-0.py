class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sletters = {}
        for char in s:
            if char not in sletters:
                sletters[char] = 1
            else:
                sletters[char] += 1
        
        tletters = {}
        for char in t:
            if char not in tletters:
                tletters[char] = 1
            else:
                tletters[char] += 1

        if tletters == sletters:
            return True
        else:
            return False
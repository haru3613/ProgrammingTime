def longestCommonPrefix(self, strs: List[str]) -> str:
        import re
        shortest = min(strs, key=len, default=0)
        
        if shortest == 0 or shortest == "": return ""
        if len(strs) == 1: return strs[0]
        prefix=""
        
        for char in shortest:
            prefix += char
            result = all([re.search('^'+prefix, s) for s in strs])
            if result==False: break
        
        if len(prefix)==1 and result != False:
            return prefix
        elif len(prefix)==len(shortest) and result != False:
            return prefix
        else:
            return prefix[:-1]


def romanToInt(self, s: str) -> int:
    symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    result = 0
    for index, char in enumerate(s):
        try:
            if symbols[char] < symbols[s[index+1]]:
                result -= symbols[char]
            else:
                result += symbols[char]
        except:
            result += symbols[char]
        
    return result
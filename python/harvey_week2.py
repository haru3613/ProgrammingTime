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


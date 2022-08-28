class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key= lambda x: len(x))
        result = ''
        for i in range(len(strs[0])):
            temp = result + strs[0][i]
            for string in strs[1:]:
                if string.find(temp) != 0:
                    return result
            result = temp
        
        return result
        
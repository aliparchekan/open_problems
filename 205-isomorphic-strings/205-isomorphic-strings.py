class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        for i, char in enumerate(s):
            table[char] = t[i]
        if len(table) != len(set(table.values())):
            return False
        new_list = [table[char] for char in s]
        new_list = ''.join(new_list)
        if new_list == t:
            return True
        return False
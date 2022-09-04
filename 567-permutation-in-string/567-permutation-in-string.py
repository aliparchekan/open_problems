class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        table_s1 = {}
        for char in s1:
            table_s1[char] = table_s1.get(char, 0) + 1
        slow = 0
        fast = len(s1)
        while fast <= len(s2):
            new_table = {}
            for char in s2[slow: fast]:
                new_table[char] = new_table.get(char, 0) + 1
            if new_table == table_s1:
                return True
            slow += 1
            fast += 1
        return False
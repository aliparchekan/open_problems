import re
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        used_secret = [False] * len(secret)
        used_guess = [False] * len(guess)
        bull = 0
        cow = 0
        for i, char in enumerate(guess):
            if char == secret[i]:
                used_secret[i] = True
                used_guess[i] = True
                bull = bull + 1
                continue
        for i, char in enumerate(guess):
            if used_guess[i]:
                continue
            occurrences = re.finditer(char, secret)
            for index in occurrences:
                start = index.start()
                if(used_secret[start] == False):
                    used_secret[start] = True
                    cow += 1
                    break
                    
        
        return str(bull) + 'A' + str(cow) + 'B'
    
test = Solution()
print(test.getHint("1122", "0001"))
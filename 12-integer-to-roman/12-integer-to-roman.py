class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        if(n:= num // 1000):
            num = num - 1000 * n
            result = result + 'M'*n
        if(n:= num // 900):
            num = num - 900* n
            result = result + 'CM'* n
        if(n:= num // 500):
            num = num - 500* n
            result = result + 'D'* n
        if(n:= num // 400):
            num = num - 400* n
            result = result + 'CD'* n
        if(n:= num // 100):
            num = num - 100* n
            result = result + 'C'* n
        if(n:= num // 90):
            num = num - 90* n
            result = result + 'XC'* n
        if(n:= num // 50):
            num = num - 50* n
            result = result + 'L'* n
        if(n:= num // 40):
            num = num - 40* n
            result = result + 'XL'* n
        if(n:= num // 10):
            num = num - 10* n
            result = result + 'X'* n
        if(n:= num // 9):
            num = num - 9* n
            result = result + 'IX'    * n
        if(n:= num // 5):
            num = num - 5* n
            result = result + 'V'* n
        if(n:= num // 4):
            num = num - 4* n
            result = result + 'IV'* n
        if(n:= num // 1):
            num = num - 1* n
            result = result + 'I'* n
            
        return result
        

                
                
                
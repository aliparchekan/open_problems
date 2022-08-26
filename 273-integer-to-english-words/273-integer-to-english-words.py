class Solution:
    def wordUnderHundred(self, num):
        result = ''
        decimal = {2: 'Twenty', 3: 'Thirty', 4:'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8:'Eighty', 9: 'Ninety'}
        unity = {0:'', 1:'One', 2: 'Two', 3:'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        specials = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        remainder = num % 10
        divisor = num // 10
        if divisor == 0 and remainder == 0:
            result = 'Zero'
        elif divisor >= 2:
            if remainder == 0:
                result = decimal[divisor]
            else:
                result = decimal[divisor] + ' ' + unity[remainder]
        elif divisor == 1:
            result = specials[num]
        else:
            result = unity[remainder]
            
        return result
    def wordHundred(self, num):
        unity = {0:'', 1:'One', 2: 'Two', 3:'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        divisor = num // 100
        remainder = num % 100
        if divisor == 0:
            return self.wordUnderHundred(remainder)
        if divisor != 0 and remainder == 0:
            return unity[divisor] + ' ' + 'Hundred'
        return unity[divisor] + ' ' + 'Hundred' + ' ' + self.wordUnderHundred(remainder)
    def wordThousand(self, num):
        divisor = num // 1000
        remainder = num % 1000
        if divisor == 0:
            return self.wordHundred(remainder)
        if divisor != 0 and remainder == 0:
            return self.wordHundred(divisor) + ' ' + 'Thousand'
        return self.wordHundred(divisor) + ' ' + 'Thousand' + ' ' + self.wordHundred(remainder)
    def wordMillion(self, num):
        divisor = num // 1e6
        remainder = num % 1e6
        if divisor == 0:
            return self.wordThousand(remainder)
        if divisor != 0 and remainder == 0:
            return self.wordHundred(divisor) + ' ' + 'Million'
        return self.wordHundred(divisor) + ' ' + 'Million' + ' ' + self.wordThousand(remainder)
    
    def wordBillion(self, num):
        divisor = num // 1e9
        remainder = num % 1e9
        if divisor == 0:
            return self.wordMillion(remainder)
        if divisor != 0 and remainder == 0:
            return self.wordHundred(divisor) + ' ' + 'Billion'
        return self.wordHundred(divisor) + ' ' + 'Billion' + ' ' + self.wordMillion(remainder)
    
    
        
    def numberToWords(self, num: int) -> str:
        result = self.wordBillion(num)
        return result
unit = {"1" : 'One', "2" : 'Two', "3" : 'Three', "4" : 'Four', "5" : 'Five', "6" : 'Six', "7" : 'Seven', "8" : 'Eight', "9" : 'Nine'}
        
teen = {"10" : 'Ten', "11" : 'Eleven', "12" : 'Twelve', "13" : 'Thirteen', "14" : 'Fourteen', "15" : 'Fifteen', "16" : 'Sixteen', "17" : 'Seventeen', "18" : 'Eighteen', "19" : 'Nineteen'}
        
tens = {"2" : 'Twenty', "3" : 'Thirty', "4" : 'Forty', "5" : 'Fifty', "6" : 'Sixty', "7" : 'Seventy', "8" : 'Eighty', "9" : 'Ninety'}
        
class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        position = ['Thousand', 'Million', 'Billion', 'Trillion']
        
        words = self.segmentToWords(num % 1000)
        num //= 1000 
        pos = 0
        while num > 0:
            segment = num % 1000
            if segment == 0:
                pos += 1
                num //= 1000
                continue
            if words == "":
                words = self.segmentToWords(segment) + " " + position[pos]
            else:
                words = self.segmentToWords(segment) + " " + position[pos] + " " + words
            pos += 1
            num //= 1000
        return words
            
    def segmentToWords(self, digit):
        words = ""
        if digit == 0:
            return words
        digit = str(digit)
        length = len(digit)
        if length == 2 and (int(digit[0]) <= 1):
            return teen[digit]
        
        if length == 1 and digit[0] != "0":
            return unit[digit]
        
        if length == 2 and (int(digit[0]) > 1) and digit[1] == "0":
            return tens[digit[0]]
        
        if length == 2 and (int(digit[0]) > 1):
            return tens[digit[0]] + " " + self.segmentToWords(int(digit[1]))
        
        if length == 3 and (int(digit[0]) >= 1) and digit[1] == "0" and digit[2] == "0":
            return unit[digit[0]] + " Hundred"
        
        if length == 3 and (int(digit[0]) >= 1):
            return unit[digit[0]] + " Hundred " + self.segmentToWords(int(digit[1:]))
        
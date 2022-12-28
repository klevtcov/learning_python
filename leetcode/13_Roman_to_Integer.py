class Solution:
    def romanToInt(self, s: str) -> int:
        alphabet = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = 0
        i = 0
        while i < len(s):
            if i+1 == len(s):
                number += alphabet[s[i]]
                break
            first = int(alphabet[s[i]])
            second = int(alphabet[s[i+1]])
            if second > first:
                i+=1
                number = number - first + second           
            else:
                number = number + first
            i+=1
        return(number)
# 55.10%

if __name__ == '__main__':
    s = "III"  
    answer = Solution()
    print(answer.romanToInt(s))



# class Solution:
#     def romanToInt(self, s: str) -> int:
#         sum = 0
#         sum = sum + s.count("IV")*4 + s.count("IX")*9 + s.count("XL")*40 + s.count("XC")*90 + s.count("CD")*400 + s.count("CM")*900
#         s = s.replace("IV","")
#         s = s.replace("IX","")
#         s = s.replace("XL","")
#         s = s.replace("XC","")
#         s = s.replace("CD","")
#         s = s.replace("CM","")
#         sum = sum + s.count("I")*1 + s.count("V")*5 + s.count("X")*10 + s.count("L")*50 + s.count("C")*100 + s.count("D")*500 + s.count("M")*1000
#         return sum

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
        
#         count = 0
#         for i in range(len(s)):
#             if i+1<len(s) and d[s[i]] < d[s[i+1]]:
#                 count -= d[s[i]]
#             else:
#                 count += d[s[i]]
#         return count

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         Roman = {"I":1, "V":5, "X": 10, "L" : 50, "C":100, "D":500, "M":1000,
#                 "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
#         sum = 0
#         i = 0
#         while i < len(s):
#             if s[i:i+2] in Roman:
#                 sum += Roman[s[i:i+2]]
#                 i += 2
#             else:
#                 sum += Roman[s[i]]
#                 i += 1
#         return sum
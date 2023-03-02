"""
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。

M05.02 bianry-number-to-string-lcci/
"""
class Solution:
    def printBin(self, num: float) -> str:
        res = "0."
        while len(res) <= 32 and num != 0:
            num *= 2
            digit = int(num)
            res += str(digit)
            num -= digit
        return res if len(res) <= 32 else "ERROR"

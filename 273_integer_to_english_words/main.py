from typing import List

class Solution:
    nmap = {'1': 'One', '2': 'Two'}
    suffix = {None, 'Thousand', 'Million', 'Billion'}

    def split3(snum: str) -> List[str]:
        "Splits a string into groups of 3 starting from right"
        pass

    def word3(snum: str) -> str:
        "Converts a 3 digit number (max 3 digits) into its word representation"
        num3str = ""
        if len(snum) == 3:
            hundigit = word3[0]
            hunstr = nmap[hundigit]

    def numberToWords(self, num: int) -> str:
        if num <= 20:
            return nmap[num]
        
        snum = str(num) # '1234567890'
        num_groups = split3(snum) # ['1', '234', '567', '890']
        wnum = []
        for i, ng in enumerate(num_groups):
            wnum3 = word3(ng) # 'Two Hundred Thirty Four'
            sidx = len(num_groups) - (i + 1)
            snum3 = suffix[sidx]    # 'Million'
            num3str = (wnum3 + ' ' + snum3) if snum3 is not None else wnum3 # 'Two Hundred Thirty Four Million'
            wnum += num3str
        
        return ' '.join(wnum)

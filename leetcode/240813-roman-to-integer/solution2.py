def romanToInt(s: str) -> int:

        translate = {"I": 1,"IV": 4, "V": 5, "IX": 9, "X": 10, "XL" : 40, "L": 50, "C": 100, "XC": 90, "D": 500, "CD": 400, "CM": 900, "M": 1000}

        num =0 
        for i in range(len(s)):
            if i < len(s) -1 and translate[s[i]] < translate[s[i+1]]:
                num -= translate[s[i]]
            else:
                num += translate[s[i]]

        return num
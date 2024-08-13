def romanToInt(s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        roman2 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        result = 0
        string = s 

        for r2 in roman2:
            count = string.count(r2)
            result += roman2[r2] * count
            string = string.replace(r2, "")

        for r1 in roman:
            count = string.count(r1)
            result += roman[r1] * count
            string = string.replace(r1, "")
        
        return result
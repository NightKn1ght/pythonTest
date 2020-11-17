class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        letters = s.replace('', ' ').split()
        number = 0
        for x in romanNumerals:
            if x in letters:
                if letters.index(x) == 0:
                    number += romanNumerals.get(x)
                    letters.remove(x)
                    return number + self.romanToInt(''.join(letters))
                elif letters.index(x) > 0:
                    arr = ''.join(letters).split(x, maxsplit=1)
                    number += romanNumerals.get(x) - self.romanToInt(arr[0])
                    return number + self.romanToInt(''.join(arr[1]))
            else:
                continue

        return 0


ff = Solution()
print(ff.romanToInt("MMCMDXXXIV"))

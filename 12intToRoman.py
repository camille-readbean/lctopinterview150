from bisect import bisect

class Solution:
    def intToRoman(self, num: int) -> str:
        # max power is 3
        def intToRomanHelper(num: int, power: int) -> str:
            values = [1, 5, 10, 50, 100, 500, 1000]
            symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
            subtractive_values = [1, 10, 50, 100, 500, 1000]
            subtractive_symbols = []
            number_as_string = str(num)
            first_char = number_as_string[0]
            if first_char == '4' or first_char =='9':
                value_of_first_num = int(first_char) * 10 ** power
                i = bisect(values, value_of_first_num)
                if i%2 == 2:
                    symbol = symbols[i-3] + symbols[i-1]
                else:
                    symbol = symbols[i-2] + symbols[i-1]
                if power > 1:
                    remaining_symbols = intToRomanHelper(int(number_as_string[1:]), power - 1)
                    return symbol + remaining_symbols
                return symbol

        power = len(str(num)) - 1
        return intToRomanHelper(num, power)
            
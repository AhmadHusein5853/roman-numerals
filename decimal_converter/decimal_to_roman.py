class DecimalToRoman:

    def convert_decimal_number(self, string_data):
        number = int(string_data)
        list_divider = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        dictionary = {1: "I", 4: "IV", 5: "V", 9: "IX",
                      10: "X", 40: "XL", 50: "L", 90: "XC",
                      100: "C", 400: "CD", 500: "D", 900: "CM",
                      1000: "M"}

        result = ""
        
        # for loop to find the first divider
        for i in range(len(list_divider)):
            if number < list_divider[i]:
                continue
            # max 3 loops in cases like 300 --> CCC
            for _ in range(3):
                result = result + str(dictionary.get(list_divider[i]))
                number = number - list_divider[i]

                if number < list_divider[i]:
                    break
            if number == 0:
                break

        return result


class RomanToDecimal:

    def convert_roman_number(self, string_data):

        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        for index in range(len(string_data)):
            char = string_data[index]
            # if the previous char if smaller than the current one then we have to subtract the smaller one twice
            if (index > 0) and dictionary.get(char) > dictionary.get(string_data[index - 1]):
                result += dictionary.get(char) - 2 * dictionary.get(string_data[index - 1])
            # otherwise just add the value of the char
            else:
                result += dictionary.get(char)

        return str(result)

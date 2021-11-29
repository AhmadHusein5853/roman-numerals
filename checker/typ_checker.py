import re


class TypChecker:

    def check_input(self, string_data) -> str:
        # check if the input is empty
        if len(string_data) == 0:
            return "NOT VALID"
        # see if the input is a decimal
        string_data = str(string_data)
        decimal = r'^\d{0,4}$'
        regex_pattern = r"%s" % decimal
        if re.match(regex_pattern, string_data) and 0 < int(string_data, 10) <= 3999:
            return "DEC"

        # see if the input is a roman numerals
        regex_pattern_roman = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

        if bool(re.match(regex_pattern_roman, string_data)):
            return "ROM"

        # otherwise it is an invalid input
        return "NOT VALID"

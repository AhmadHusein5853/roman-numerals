
import checker.typ_checker as c
import decimal_converter.decimal_to_roman as d_converter
import roman_converter.roman_to_decimal as r_converter




if __name__ == "__main__":
    print('''
        - this script take a decimal number form the user between 1 and 3999 and convert it to a roman numeral
        - or you can provide a roman numeral and the script will convert it to a decimal in case it is valid 
                                        ------------------------------
    ''')

    while(True):
        string_input = input("provide a decimal/roman number, 'q'/'Q' terminate this script : ")

        if string_input.upper() == 'Q': break

        checker = c.TypChecker().check_input(string_data=string_input)

        if checker == "DEC":
            result = d_converter.DecimalToRoman().convert_decimal_number(string_input)
            print(result)
        elif checker == "ROM":
            result = r_converter.RomanToDecimal().convert_roman_number(string_input)
            print(result)
        else:
            print ("not valid input ")


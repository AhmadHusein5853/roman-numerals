import unittest
import roman_converter.roman_to_decimal as d


class RomanToDecimal(unittest.TestCase):
    def test_convert_decimal_number1(self):
        dConverter = d.RomanToDecimal()
        result = dConverter.convert_roman_number("XXXVI")
        self.assertEqual(result, "36")

    def test_convert_decimal_number2(self):
        dConverter = d.RomanToDecimal()
        result = dConverter.convert_roman_number("MMMDXLIII")
        self.assertEqual(result, "3543")

    def test_convert_decimal_number3(self):
        dConverter = d.RomanToDecimal()
        result = dConverter.convert_roman_number("MMMLXXXIX")
        self.assertEqual(result, "3089")

    def test_convert_decimal_number4(self):
        dConverter = d.RomanToDecimal()
        result = dConverter.convert_roman_number("DVI")
        self.assertEqual(result, "506")

    def test_convert_decimal_number5(self):
        dConverter = d.RomanToDecimal()
        result = dConverter.convert_roman_number("MDLXXIII")
        self.assertEqual(result, "1573")


if __name__ == '__main__':
    unittest.main()

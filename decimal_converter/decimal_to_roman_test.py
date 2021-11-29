import unittest
import decimal_converter.decimal_to_roman as d


class DecimalToRoman(unittest.TestCase):
    def test_convert_decimal_number1(self):
        dConverter = d.DecimalToRoman()
        result = dConverter.convert_decimal_number("36")
        self.assertEqual(result, "XXXVI")

    def test_convert_decimal_number2(self):
        dConverter = d.DecimalToRoman()
        result = dConverter.convert_decimal_number("3543")
        self.assertEqual(result, "MMMDXLIII")

    def test_convert_decimal_number3(self):
        dConverter = d.DecimalToRoman()
        result = dConverter.convert_decimal_number("3089")
        self.assertEqual(result, "MMMLXXXIX")

    def test_convert_decimal_number4(self):
        dConverter = d.DecimalToRoman()
        result = dConverter.convert_decimal_number("506")
        self.assertEqual(result, "DVI")

    def test_convert_decimal_number5(self):
        dConverter = d.DecimalToRoman()
        result = dConverter.convert_decimal_number("1573")
        self.assertEqual(result, "MDLXXIII")


if __name__ == '__main__':
    unittest.main()

import unittest
import checker.typ_checker as c


class TypCheckerTest(unittest.TestCase):
    def test_check_not_empty_string(self):
        checker = c.TypChecker()
        result = checker.check_input("")
        self.assertEqual(result, "NOT VALID")

    def test_check_decimal(self):
        checker = c.TypChecker()
        result = checker.check_input("1000")
        self.assertEqual(result, "DEC")

    def test_check_decimal_not_between_1_and_3999(self):
        checker = c.TypChecker()
        result = checker.check_input("0")
        self.assertEqual(result, "NOT VALID")

    def test_check_ROM(self):
        checker = c.TypChecker()
        result = checker.check_input("MMMDCCXXIV")
        self.assertEqual(result, "ROM")

    def test_check_not_valid_ROM(self):
        checker = c.TypChecker()
        result = checker.check_input("IXIV")
        self.assertEqual(result, "NOT VALID")

    def test_check_combined_case(self):
        checker = c.TypChecker()
        result = checker.check_input("1234XL")
        self.assertEqual(result, "NOT VALID")


if __name__ == '__main__':
    unittest.main()

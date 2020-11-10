import unittest
import doctest


class PasswordChecker:
    """
    >>> password_checker = PasswordChecker()
    >>> password_checker.valid_password('Ab?c1')
    False
    >>> password_checker.valid_password('abcvssj1?')
    False
    >>> password_checker.valid_password('aBsgds!s')
    False
    >>> password_checker.valid_password('vbkjbV3r1')
    False
    >>> password_checker.valid_password('')
    False
    >>> password_checker.valid_password('qWerty?51')
    True
    """
    def valid_password(self, password):
        if len(password) >= 8 and any(i.isupper() for i in password) and any(i.isdigit() for i in password) and any(not i.isalnum() for i in password):
            return True
        else:
            return False


class PasswordCheckerTest(unittest.TestCase):
    def setUp(self):
        self.temp = PasswordChecker()

    def test_is_working(self):
        self.assertEqual(self.temp.valid_password('aBcdE?56'), True)

    def test_disallow_too_short_password(self):
        self.assertEqual(self.temp.valid_password('Ab?c1'), False)

    def test_disallow_password_without_capital_letter(self):
        self.assertEqual(self.temp.valid_password('abcvssj1?'), False)

    def test_disallow_password_without_digit(self):
        self.assertEqual(self.temp.valid_password('aBsgds!s'), False)

    def test_disallow_password_without_special_character(self):
        self.assertEqual(self.temp.valid_password('vbkjbV3r1'), False)

    def test_disallow_empty_password(self):
        self.assertEqual(self.temp.valid_password(''), False)

    def tearDown(self):
        self.temp = None


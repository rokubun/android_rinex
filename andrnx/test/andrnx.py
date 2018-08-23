import unittest
import doctest

class Test(unittest.TestCase):
    """
    Unit tests for pyrok
    """

    def test_doctests_gnsslogger(self):
        import andrnx.gnsslogger
        fails, tests = doctest.testmod(andrnx.gnsslogger)
        self.assertEqual(fails, 0)


if __name__ == "__main__":
    unittest.main()

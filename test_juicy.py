import unittest

from juicy import invest_flash, invest_myst, invest_kush, invest_haze


class TestJuicy(unittest.TestCase):

    def test_flash(self):
        res = invest_flash(51)
        self.assertEqual(res, [1, 0, 0, 68])
        self.assertEqual(sum(res), 69)

    def test_myst(self):
        res = invest_myst(2000)
        self.assertEqual(len(res), 3 * 12)
        for period in range(3 * 12 // 4):
            self.assertEqual(res[period * 3], 0)
            self.assertEqual(res[period * 3 + 1], 0)
            self.assertEqual(res[period * 3 + 2], 300)
        self.assertEqual(sum(res), 3600)

    def test_kush(self):
        res = invest_kush(4500)
        self.assertEqual(len(res), 4 * 12)
        self.assertEqual(sum(res), 12500)

    def test_haze(self):
        res = invest_haze(2000)
        self.assertEqual(len(res), 5 * 12)
        self.assertEqual(sum(res), 9000)


if __name__ == "__main__":
    unittest.main()

# test_juicy.py ends here

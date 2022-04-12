import unittest

from juicy import invest_flash, invest_myst, invest_kush, invest_haze, merge_arrays, re_invest


class TestJuicy(unittest.TestCase):

    def test_flash(self):
        res = invest_flash(51)[0]
        self.assertEqual(res, [1, 0, 0, 68])
        self.assertEqual(sum(res), 69)

    def test_myst(self):
        res = invest_myst(2000)[0]
        self.assertEqual(len(res), 3 * 12)
        for period in range(3 * 12 // 4):
            self.assertEqual(res[period * 3], 0)
            self.assertEqual(res[period * 3 + 1], 0)
            self.assertEqual(res[period * 3 + 2], 300)
        self.assertEqual(sum(res), 3600)

    def test_kush(self):
        res = invest_kush(4500)[0]
        self.assertEqual(len(res), 4 * 12)
        self.assertEqual(sum(res), 12500)

    def test_haze(self):
        res = invest_haze(2000)[0]
        self.assertEqual(len(res), 5 * 12)
        self.assertEqual(sum(res), 9000)

    def test_re_invest(self):
        years = 5
        res = re_invest(4000, years)
        self.assertEqual(sum(res), 294766)

    def test_merge_arrays(self):
        res = [10, 10, 10]
        merge_arrays(res, 1, [10, 10, 10])
        self.assertEqual(res,
                         [10, 20, 20, 10])

if __name__ == "__main__":
    unittest.main()

# test_juicy.py ends here

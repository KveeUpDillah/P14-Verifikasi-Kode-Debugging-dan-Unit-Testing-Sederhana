import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()
    
    def test_diskon_float_33_persen(self):
        """Tes 5 (Float): Menguji diskon 33% pada harga 999 Menggunakan assertAlmostEqual karena hasil berupa float."""
        hasil = self.calc.hitung_diskon(999, 33)
        self.assertAlmostEqual(hasil, 669.33)

    def test_harga_awal_nol(self):
        """Tes 6 (Edge Case): Jika harga awal 0, maka harga akhir harus 0."""
        hasil = self.calc.hitung_diskon(0, 10)
        self.assertEqual(hasil, 0)

if __name__ == '__main__':
    unittest.main()
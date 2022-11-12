import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
    
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_kortilta_voi_ottaa_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_otetaan_yli_saldon(self):
        self.maksukortti.ota_rahaa(2000)    

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_palauttaa_true_jos_otto_onnistuu(self):
        tulos = self.maksukortti.ota_rahaa(500)    
        self.assertTrue(tulos)
    
    def test_palauttaa_false_jos_otto_epaonnistuu(self):
        tulos = self.maksukortti.ota_rahaa(2000)    
        self.assertFalse(tulos)
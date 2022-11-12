import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    # init oikein
    def test_konstruktori_asettaa_arvot_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)

    # syo_edullisesti_kateisella
    def test_syo_edullisesti_toimii_riittavalla_rahamaaralla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha,60)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_syo_edullisesti_toimii_liian_pienella_rahamaaralla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)

    # syo_maukkaasti_kateisella
    def test_syo_maukkaasti_toimii_riittavalla_rahamaaralla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihtoraha,50)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_syo_maukkaasti_toimii_liian_pienella_rahamaaralla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    # syo_edullisesti_kortilla
    def test_syo_edullisesti_toimii_kortilla(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(tulos)
        self.assertEqual(self.kortti.saldo,760)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_syo_edullisesti_kortilla_epaonnistuu_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        tulos = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)

    # syo_maukkaasti_kortilla
    def test_syo_maukkaasti_toimii_kortilla(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(tulos)
        self.assertEqual(self.kortti.saldo,600)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_syo_maukkaasti_kortilla_epaonnistuu_jos_saldo_ei_riita(self):
        kortti = Maksukortti(200)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    # laata_rahaa_kortille
    def test_rahan_lataaminen_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo,1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100500)
    
    def test_neg_rahan_lataaminen_kortille_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kortti.saldo,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        
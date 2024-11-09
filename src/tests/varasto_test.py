import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_liikaa_varastoon(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_liikaa_varastosta(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(12)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_nollataan_neg_alkusaldo(self):
        neg_varasto = Varasto(10,-5)
        self.assertAlmostEqual(neg_varasto.saldo, 0.0)
    
    def test_nollataan_neg_tilavuus(self):
        neg_tilavuus = Varasto(-5)
        self.assertAlmostEqual(neg_tilavuus.tilavuus, 0)

    def test_lisays_neg_maara_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_neg_maara_palauttaa_0(self):
        saatu = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu, 0)
    
    def test_saldo_on_max_tilavuus(self):
        varasto = Varasto(10,15)
        self.assertAlmostEqual(varasto.saldo, 10)
    
    def test_lisays_taydentaa_varaston(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)  

    def test_merkkijonoesitys(self):
        self.varasto.lisaa_varastoon(8)moi
        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")

if __name__ == "__main__":
    unittest.main()
import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 1)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_laitetaan_liikaa(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Branch 1: saldo = tilavuus

    def test_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(4)
        saatu_maara = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(saatu_maara, 4)  # Branch 2: maara > self.saldo

    def test_lisaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-2)  # Branch 3: maara < 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(4)
        saatu_maara = self.varasto.ota_varastosta(-2)  # Branch 4: maara < 0
        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_tilavuus_zero(self):
        varasto = Varasto(0)  # Branch 5: tilavuus = 0
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_tilavuus_negative(self):
        varasto = Varasto(-5)  # Branch 6: tilavuus < 0
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_alku_saldo_negative(self):
        varasto = Varasto(10, -5)  # Branch 7: alku_saldo < 0
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_alku_saldo_too_large(self):
        varasto = Varasto(10, 15)  # Branch 8: alku_saldo > tilavuus
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_str_method(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(3)
        expected_str = "saldo = 2, vielä tilaa 8"
        self.assertEqual(str(self.varasto), expected_str)  # Branch 9: __str__ method
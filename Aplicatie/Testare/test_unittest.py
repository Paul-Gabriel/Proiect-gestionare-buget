import unittest
from Program.Buget import Buget
from Program.Venit import Venit
from Program.Plata import Plata

class Test_Aplicatie(unittest.TestCase):
    def test_combinaPlati(self):
        buget=Buget(2000)
        self.assertEqual(buget.venit, buget.combinaPlati())

if __name__ == '__main__':
    unittest.main()

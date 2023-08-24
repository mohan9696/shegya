from module_add1 import add_10
import unittest
class AdditionTest(unittest.TestCase):
    def test_add(self):
        x=add_10(15)
        self.assertEqual(x,250)
if __name__=='__main__':
     unittest.main()
 
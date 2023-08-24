from module2_add import add_two,sub_two,mul_two,div_two
import unittest
class AdditionTest(unittest.TestCase):
    def test_add(self):
        x=add_two(10,20)
        self.assertEqual(x,20)
    def test_sub(self):
        x = sub_two(10, 20)
        self.assertEqual(x,20)
    def test_mul(self):
        x=mul_two(10,20)
        self.assertEqual(x,20)
    def test_dev(self):
        x = div_two(10, 20)
        self.assertEqual(x,20)
if __name__== '__main__':
    unittest.main()






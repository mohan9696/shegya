import unittest
class Test_add (unittest.TestCase):
    def setup (self):
        print("this is setup")
    def setup_a (self):
        print("this is a setup")
    def setup_b (self):
        print("this is b setup")
    def tearDown(self):
        print("teardown method")
if __name__ =='__main__':
    unittest.main()
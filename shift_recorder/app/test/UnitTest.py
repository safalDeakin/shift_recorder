import unittest
from timeit import default_timer as timer

class UnitTest(unittest.TestCase):
    
    def test_start_shift(self):
        start = timer()
        expected = True
        result = True
        self.assertEqual(expected, result)
        end= timer()
        print(f'Time Taken: {end-start}')
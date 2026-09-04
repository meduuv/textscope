import unittest
from textscope import stats
class Tests(unittest.TestCase):
 def test_stats(self): self.assertEqual(stats("hello hello\nworld"),{"characters":17,"words":3,"lines":2,"unique_words":2})
if __name__=="__main__": unittest.main()

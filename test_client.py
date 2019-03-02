import unittest
import random
from worker import add_int, add_int_kwargs, add_str, add_str_int
from worker import add_float, max_arr_len, add_arr, add_dict, and_bool

class TestCeleryExecution(unittest.TestCase):

  # 1) integer addition
  def test_add(self):
    x = random.randint(1, 5000)
    y = random.randint(1, 5000)
    expected = x + y
    ar = add_int.apply_async((x, y), serializer='json')
    self.assertEqual(expected, ar.get())

  # 2) integer addition with kwargs
  def test_add_int_kwargs(self):
    x = random.randint(1, 5000)
    y = random.randint(1, 5000)
    expected = x + y
    ar = add_int_kwargs.apply_async(kwargs={'x':x, 'y':y}, serializer='json')
    self.assertEqual(expected, ar.get())

  # 3) string addition
  def test_add_str(self):
    a = 'hello'
    b = ' world'
    expected = a + b
    ar = add_str.apply_async((a, b), serializer='json')
    self.assertEqual(expected, ar.get())

  # 4) integer and string concatenation
  def test_add_str_int(self):
    a = 'hello'
    b = random.randint(1, 5000)
    expected = a + str(b)
    ar = add_str_int.apply_async((a, b), serializer='json')
    self.assertEqual(expected, ar.get())

  # 5) float addition
  def test_add_float(self):
    a = random.uniform(1.0, 10.0)
    b = random.uniform(1.0, 10.0)
    expected = a + b
    ar = add_float.apply_async((a, b), serializer='json')
    self.assertEqual(expected, ar.get())

  # 6) maximum array length
  def test_max_arr_len(self):
    a = []
    b = []
    for _ in range(random.randint(5, 10)):
      a.append(0)
    for _ in range(random.randint(5, 10)):
      b.append(0)
    expected = len(b)
    if len(a) > len(b):
      expected = len(a)
    ar = max_arr_len.apply_async((a, b), serializer='json')
    self.assertEqual(expected, ar.get())

  # 6) array addition
  def test_add_arr(self):
    a = []
    b = []
    length = random.randint(5, 10)
    for _ in range(length):
      a.append(random.randint(1, 5000))
    for _ in range(length):
      b.append(random.randint(1, 5000))
    expected = a + b
    ar = add_arr.apply_async((a, b), serializer='json')
    self.assertEqual(expected, ar.get())

  # 7) dictionary addition
  def test_add_dict(self):
    a = {}
    b = {}
    expected = a.copy()
    expected.update(b)
    ar = add_dict.apply_async((a, b), serializer='json')
    self.assertEqual(expected, ar.get())

  # 8) boolean and operation
  def test_and_bool(self):
    a = bool(random.getrandbits(1))
    b = bool(random.getrandbits(1))
    expected = a and b
    ar = and_bool.apply_async((a, b), serializer='json')
    self.assertEqual(expected, ar.get())


if __name__ == '__main__':
  unittest.main()
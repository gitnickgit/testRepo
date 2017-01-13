import unittest

def fizzbang(i):
  if(i < 1) or (i > 101) or (type(i) != int):
      return('invalidinput')
  threemod = i%3
  fivemod = i%5
  if(threemod == 0) and (fivemod == 0):
    return('FizzBang')
  elif threemod == 0 and fivemod != 0:
    return('Fizz')
  elif fivemod == 0 and threemod != 0:
    return('Bang')
  elif fivemod !=0 and threemod !=0:
    return(i)
  else:
    print("ERROR FOUND")
    
for i in xrange(1,101):
  print(fizzbang(i))

class MyTest(unittest.TestCase):

  def test_fizz(self):
    #print('Fizz testing')
    self.assertEqual(fizzbang(3), 'Fizz')
    self.assertFalse(fizzbang(2) == 'Fizz')
  def test_bang(self):
    #print('Bang testing')
    self.assertTrue(fizzbang(5) == 'Bang')
    self.assertFalse(fizzbang(2) == 'Bang')
  def test_remainder(self):
    print('Remainder testing')
    self.assertTrue(fizzbang(2) == 2)
  def test_type(self):
    #print('type testing')
    self.assertTrue(type(fizzbang(2)) == int)
    self.assertTrue(fizzbang(999) == 'invalidinput')
    self.assertTrue(fizzbang('blah') == 'invalidinput')

suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
unittest.TextTestRunner(verbosity=2).run(suite)

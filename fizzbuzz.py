#fizzbuzz.py

class FizzBuzz:
	x = "hello"

	def fizz(self, x):
		return "Fizz" if x % 3 == 0 else x

	def buzz(self, x):
		if x % 5 == 0:
			return "Buzz"
		else:
			return x


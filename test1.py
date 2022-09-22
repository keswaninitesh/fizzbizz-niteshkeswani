#Generating the first code
#!/usr/bin/env python
# Reference https://www.programsbuzz.com/interview-question/write-program-prints-numbers-1-100-multiples-three-print-fizz
x_1 = 1
x_101 = 101
def fizzbuzz_niteshkeswani(x_1,x_101):
	for num in range(x_1, x_101):
		if num % 3 == 0 and num % 5 == 0:
			print("FizzBuzz")
			continue
		elif num % 3 == 0:
			print("Fizz" +str(num))
			continue
		elif num % 5 == 0:
			print("Buzz" +str(num))
			continue
		else:
			print(num)
	return()
fizzbuzz(1,101)

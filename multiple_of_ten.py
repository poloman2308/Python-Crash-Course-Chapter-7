{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

number = input("Guess a number, please: ")
number = int(number)

if number % 10 == 0:
	print(str(number) + " is a multiple of 10.")
else:
	print(str(number) + " is not a multiple of 10.")
	
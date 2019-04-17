{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

people = input("How many people are in your dinner group? ")
people = int(people)

if people > 8:
	print("I'm sorry, We are waiting for a table to open.")
else:
	print("Your table is ready to be seated!")


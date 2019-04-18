{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are done. "

while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)
	
	if age < 3:
		print(" You get in free!")
	elif age < 13:
		print(" Tickets are $10")
	else:
		print(" Tickets are $15")

		
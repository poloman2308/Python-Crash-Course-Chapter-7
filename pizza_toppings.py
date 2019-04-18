{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

prompt = "\nEnter your pizza toppings:"
prompt += "\n(Enter 'quit' when you are done. "

while True:
	topping = input(prompt)
	if topping != 'quit':
		print(" I'll add " + topping + " to your pizza")
	else:
		break
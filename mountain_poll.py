{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

responses = {}

# Set a flag to indicate poll is active

polling_active = True

while polling_active:
	# Prompt or the person's name and response
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	# Store responses in the dictionary
	responses[name] = response

	# Find out who else is taking the poll
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# When poll is complete show results
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

	
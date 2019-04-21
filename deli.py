{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

sandwich_orders = ['beach club', 'santa fe', 'chicken', 'tuna']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I'm working on your " + current_sandwich.title() + " sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
	print("I made a " + sandwich.title() + " sandwich.")

	
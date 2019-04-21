{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

sandwich_orders = ['pastrami', 'beach club', 'santa fe', 'pastrami', 'chicken', 'tuna', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I'm working on your " + current_sandwich.title() + " sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
	print("I made a " + sandwich.title() + " sandwich.")

	
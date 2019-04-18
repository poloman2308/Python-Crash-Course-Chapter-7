{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)


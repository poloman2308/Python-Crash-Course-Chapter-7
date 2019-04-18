{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

# Starting with users that need to be verified
# Empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Going to verify each unconfirmed user and then move them to confirmed user list

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

# Display confirmed users

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

	
usernames = ["alice", "bob", "charlie", "diana", "sofia", "alice"]
print("Checking for duplicates...")
duplicates = set([name for name in usernames if usernames.count(name) > 1])
if duplicates:
    print("Duplicate usernames found:", duplicates)
else:
    print("No duplicates found.")
while True:
    new_username = input("Enter a new username: ").strip().lower()
    if new_username in usernames:
        print("❌ That username already exists. Please try another one.")
    else:
        usernames.append(new_username)
        print(f"✅ Username '{new_username}' added successfully!")
        break
print("\nUpdated usernames list:", usernames)

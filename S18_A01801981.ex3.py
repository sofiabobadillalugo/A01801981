shopping_list = ["Milk", "Bread", "Eggs", "Apples", "Rice"]
already_purchased = [False, True, False, False, True]
print("Items not yet purchased:")
for i in range(len(shopping_list)):
    if not already_purchased[i]:
        print(f"- {shopping_list[i]}")
for i in range(len(shopping_list)):
    if not already_purchased[i]:
        answer = input(f"Have you purchased {shopping_list[i]}? (yes/no): ").strip().lower()
        if answer == "yes":
            already_purchased[i] = True
print("\n Updated Shopping Status:")
for i in range(len(shopping_list)):
    status = "Purchased" if already_purchased[i] else "Not purchased"
    print(f"- {shopping_list[i]}: {status}")

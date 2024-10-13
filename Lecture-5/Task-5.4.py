user_number = int(input("ჩაწერე ნაძვის ხის სიმაღლე: "))

print(" " * user_number + "*")

for i in range(user_number - 1):
    spaces = user_number - 1 - i
    tree_branches = "/" * (i + 1) + "|" + "\\" * (i + 1)
    print(" " * spaces + tree_branches)

print(" " * user_number + "|")
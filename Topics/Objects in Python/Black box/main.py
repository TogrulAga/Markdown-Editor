# use the function blackbox(lst) that is already defined
my_list = [1, 2, 3]
new_list = blackbox(my_list)

if my_list is new_list:
    print("modifies")
else:
    print("new")

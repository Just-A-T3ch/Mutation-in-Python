def mutation(my_list):
  my_list.append(50)
  return my_list

my_rolls = [1, 2, 3, 4, 5, 6, 7]
list_after_call = mutation(my_rolls)

print("Original list:", my_rolls)
print("New list:", list_after_call)

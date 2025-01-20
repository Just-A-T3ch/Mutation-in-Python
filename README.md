Python Concept on Mutation: 
In Python, mutation refers to the ability to change or modify the contents of an object after it has been created. 
This concept is particularly relevant for mutable data types, such as lists and dictionaries, which allow for modifications without creating a new object. 
Understanding mutation is essential for effectively managing data structures in Python and ensuring that your code behaves as expected.

**Python Mutation Concept**: In Python, all data types are classified as either mutable or immutable. 
Standard types such as float, boolean, and string are immutable, meaning that once they are defined, they cannot be changed. 

Consider the function defined as `def mutation(my_list):`. This function takes in a mutable list. Inside the function, `my_list.append(50)` adds the value 50 to the end of the list and then returns the modified list. 

You might wonder what happens to the original list, `my_rolls`, after calling the function: `list_after_call = mutation(my_rolls)`. 
You might think we are creating a copy of `my_rolls`, resulting in something like `[1, 2, 3, 4, 5, 6, 7, 50]`. The key question is whether `my_rolls` itself changes or remains the same.

When we run the code, we see that `my_rolls` actually changes. This occurs because when we pass a mutable type like my_list as a parameter to a function, 
we are not creating a deep copy of the original list object; instead, we are passing a reference to it. 
Therefore, when we execute `my_list.append(50)`, we are modifying the existing list that was passed into the function rather than creating a new one. 
As a result, after the function call, `list_after_call` will refer to a list that is also a reference to the original list, now containing the appended value.


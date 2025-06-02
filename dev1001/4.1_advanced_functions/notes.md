# LAMDAS 
- single line funciton that has NO name and needs no "return" statement 
## Why would you use a lambda? 
- if you are passing a function into ANOTHER function as a parameter and that function is not used anywhere else 
- the more experienced you are with standard functions and lambdas, you wil get a better feel of which one to use 
- generally good when you want to quickly create something without having to create a entire function/defining it. 

# are lambdas more superior than normal fucntions?
- no, they dont do anything functions CANNOT do
- they also keep them DRY but also a quicker and nicer way of doing it. 
- because python is a interpreting language, anywhere we can shortcut things, is good, which is why its good using lambdas when we can 

``` python
power = lambda base, exp: base ** exp
#this is the same as 
def power(base, exp):
    return base ** exp
``` 

# EXAMPLE OF LAMBDAS
``` python
points = [(3, 4), (1, 7), (0, -2), (5, 2)]
## sort the tuples by the x coordinates
print(sorted(points))
# sort the tuples by the y coordinates
y_sorted_points = sorted(points, key=lambda point: point[1])
``` 
🧩 The full expression is:
``` python 
sorted(points, key=lambda point: point[1])
```
Let’s unpack it part by part:

✅ 1. sorted(...)
This is the built-in function that takes in:

an iterable (like a list, tuple, etc.)

an optional key function to tell it how to sort

✅ 2. points
This is the list you want to sort. So it goes into the first argument of sorted().
``` python
sorted(points)
```
would sort the list points.

✅ 3. key=lambda point: point[1]
This is a custom instruction for how to sort:
key= means: “use this function to pull a value from each item to sort by”
lambda point: point[1] means:
→ "For every item (like (3, 4)), just grab the second number (4) and use that to sort"

🔄 Put it all together:
``` python
sorted(points, key=lambda point: point[1])
```
"Sort the list called points, using the second number in each tuple as the sort value."

🧠 Why do we put points before key=...?
Because:

The first argument to sorted() is what you're sorting.

The key= part is how you want to sort it.

It's just like saying:
``` python
function(thing_to_process, special_rules)
```
🎯 Analogy
Think of sorted() like a sorting machine:
``` python
sorted(what_to_sort, key=how_to_sort_it)
```
Example:
``` python 
sorted(points, key=lambda p: p[1])
```
= “Sort the points list, but use the second value of each point to decide the order.”

# Lambdas Exercise
# 
# You have a list of tuples.
# Use the built-in sorted() function with a lambda as the 'key' argument
#   to sort these points on their y-coordinate (2nd element of each tuple).
# Print out the sorted points.

points = [(1, 2), (3, 1), (5, -4), (0, 0)]

sorted_points = sorted(points, key=lambda p: p[1]) 

print(sorted_points)


#exercise 2 from Chatgpt
points = [(2, 5), (1, 3), (4, 1), (0, 6)]
sorted_by_y = sorted(points, key=lambda point: point[1])
print(sorted_by_y)

#exercise 3 from chatgpt
points = [(3, 4), (1, 7), (0, -2), (5, 2)]

#exercise4 from chatgpt
points = [(3, 4), (1, 7), (0, -2), (5, 2)]
## sort the tuples by the x coordinates
print(sorted(points))
# sort the tuples by the y coordinates
y_sorted_points = sorted(points, key=lambda point: point[1])
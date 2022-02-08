# 1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
print()
def createCountDownArray(n):
    a = []
    for i in range (n, 0, -1):
        a.append(i)
    return a
given = 10
arr = createCountDownArray(given)
print(arr)

# 2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
print()
def print_and_return(a):
    print(a[0])
    return a[1]
print(print_and_return([3,66]))


# 3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
print()
def first_plus_length(a):
    return a[0] + len(a)
print(first_plus_length([1,2,3,4,5]))



# 4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
print()
def values_greater_than_second(a):
    b = []
    if len(a) < 2:
        return False
    for i in range(0,len(a)):
        if a[i] > a[1]:
            b.append(a[i])
    print(len(b))
    return b
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))




# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

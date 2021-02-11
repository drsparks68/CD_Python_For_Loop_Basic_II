# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def big(mylist):
    for x in range(0, len(mylist)):
        if mylist[x] > 0:
            mylist[x] = "big"
    return mylist

print(big([-1, 3, 5, -5]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def positives(mylist):
    counter = 0
    for x in range(len(mylist)):
        if mylist[x] > 0:
            counter += 1
    mylist[(len(mylist) -1 )] = counter
    return mylist

z = positives([1,6,-4,-2,-7,-2])
print(z)



# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def addItUp(mylist):
    sum = 0
    for x in range(len(mylist)):
        sum = sum + mylist[x]
    return sum

z = addItUp([1,2,3,4])
print(z)



# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def sumItUp(mylist):
    sum = 0
    avrg = 0
    for x in range(len(mylist)):
        sum = sum + mylist[x]
    avrg = sum / len(mylist)
    return avrg

z = sumItUp([1,2,3,4])
print(z)



# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def listLength(mylist):
    return len(mylist)

z = listLength([])
print(z)


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimumval(mylist):
    if len(mylist) < 1:
        return False
    else:
        minval = mylist[0]
        for x in range(1, len(mylist)):
            if mylist[x] < minval:
                minval = mylist[x]
        return minval

z = minimumval([])
print(z)



# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximumval(mylist):
    if len(mylist) < 1:
        return False
    else:
        minval = mylist[0]
        for x in range(1, len(mylist)):
            if mylist[x] < minval:
                minval = mylist[x]
        return minval

z = minimumval([])
print(z)



# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

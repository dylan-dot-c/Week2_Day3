# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
# assumptions
# input is a list of numbers, size doesnt matter
#if element is empty or null return empty array
#output -> [] of ints in format of [countPositives, sum Negatives]
#0 is not pos or neg so ignore
# vars for posCount and negSum
# if arr empty or null return []
#loop through arr
#check polarity +/- 
# if + incre poscount
# else incre negCount
def solution(array):
    posCount = 0
    negSum = 0
    if array == [] or array == None:
        return []
    else:
        for num in array:
            if num == 0:
                continue
            if num > 0:
                posCount+=1
            elif num < 0:
                negSum += num
    return [posCount, negSum]
def average(nums):
    sum = 0
    for i in nums:
        sum += i

    return sum / len(nums)

numbers = [1,2,4,6]

print(average(numbers))

#COULD'VE DONE SUM(NUMS)

nums = [1, 2, 3, 4, 5, 6, 7, 9, 8]


def odd_even(num):
    if num % 2 == 0:
        return 'even'
    if num % 2 == 1:
        return 'odd'


parity = list(map(odd_even, nums))
rest = {}
for i in range(0, len(nums)):
    rest[nums[i]] = parity[i]
print(rest)


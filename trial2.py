# print('Hello World!')
file = 'LocalFolder/junk.txt'

with open(file) as file:
    nums = file.readlines()

final_print = ''
for num in nums:
    final_print += num.strip()
final_print.replace(' ', '')
print(len(final_print))
# birth = input('ddmmyy')
# x = '0'
# y = 0
# if birth in final_print:
#     print('YEs your birthday does appears in the 1M values of pi')
# else:
#     print('Better luck next life')

print(type(nums))
print(type(num))
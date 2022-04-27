my_dic = {
    1:'۱',
    2:'۲',
    3:'۳',
    4:'۴',
    5:'۵',
    6:'۶',
    7:'۷',
    8:'۸',
    9:'۹',
    0:'۰',
}

# your number here...
number = "3158096"
result = ""
my_arr = []
for n in number: 
    my_arr.append(my_dic[int(n)])

dots = len(my_arr) // 3

if len(my_arr) % 3 == 0:
    dots = dots - 1

for i in range(0, dots):
    n = 3 * (i+1) 
    index = len(result) - n 
    index = index - i
    my_arr.insert( index , ',')

for n in my_arr:
    result += n

print(result)

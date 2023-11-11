# This is a sample Python script.

# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
a = ('some', 1, 2, 3, 10, 20, 9, 'text')
b = ['another', 0, 4, 2, 1, 7, 'long text']
c = 123456789
d = 'Number of letters in this string is: 29'


def func(input_value):
    result = {}
    let_count = 0
    num_count = 0

    if type(input_value) == tuple:
        for i in str(input_value):
            let_count += str.isalpha(i)
        result.update({'input type': 'tuple', 'letters count': let_count})

    elif type(input_value) == list:
        for i in str(input_value):
            let_count += str.isalpha(i)
            num_count += str.isdigit(i)
        result.update({'input type': 'list', 'letters count': let_count, 'numbers count': num_count})

    elif type(input_value) == int:
        for i in str(input_value):
            if int(i) % 2 != 0:
                num_count += 1
        result.update({'input type': 'int', 'numbers count': num_count})

    elif type(input_value) == str:
        for i in str(input_value):
            let_count += str.isalpha(i)
        result.update({'input type': 'str', 'letters count': let_count})

    return result


print(func(a), func(b), func(c), func(d), sep='\n')
# Este programa sirve para ...
def programa_1():
    max_num = int(input("Introduce un número: "))
    sum_nums = max_num
    for i in range(8):
        num = int(input("Introduce otro número: "))
        sum_nums += num
        if num > max_num:
            max_num = num
    print("The largest number is:", max_num)
    print("The average is:", sum_nums / 9)
programa_1()

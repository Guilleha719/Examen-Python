def programa_1():
    max_num = int(input("Introduce un número: "))
    sum_nums = max_num
    count = 1
    while count < 9:
        num =int(input("Introduce otro número: "))
        sum_nums += num
        if num > max_num:
            max_num = num
        count += 1
    print("The largest number is:", max_num)
    print("The average is:", sum_nums / 9)
programa_1()

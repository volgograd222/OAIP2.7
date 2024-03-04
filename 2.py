def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

my_list = [2,3,5]
max_number = find_max(my_list)
print("Максимальное число в списке:", max_number)

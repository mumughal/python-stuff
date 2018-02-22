def check_number_ascending(number):
    number_list = [int(x) for x in str(number_list)]
    if sorted(number_list) == number_list:
        return True
    
def last_number_by_peter(number):
    number_list = [int(x) for x in str(number)]
    flag = True
    last_number = number
    while flag:
        if sorted(number_list) == number_list:
            return int(last_number)
        else:
            x = 0
            while x < (len(number_list) - 1):
                if number_list[x] > number_list[x+1]:
                    number_list[x+1] = 9
                    if int(''.join(str(e) for e in number_list)) > number:
                        number_list[x] = number_list[x] - 1
                x = x+1
        last_number = ''.join(str(e) for e in number_list)

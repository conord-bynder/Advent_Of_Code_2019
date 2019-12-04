#!/usr/bin/python
import pdb



def check_password_min_reqs(password):
    digit_list = [int(d) for d in str(password)]
    dupe_found = False

    for index, digit in enumerate(digit_list):
        if index == len(digit_list) - 1 :
            break
        if digit_list[index+1] == digit:
            dupe_found = True
            break

    if not dupe_found:
        return

    sorted_list = digit_list.copy()
    sorted_list.sort()

    if digit_list == sorted_list:
        return password

def check_password_full_reqs(password):
    digit_list = [int(d) for d in str(password)]
    dupe_found = False

    for index, digit in enumerate(digit_list):
        if index == len(digit_list) - 1 :
            break

        count = digit_list.count(digit) 
        if count != 2:
            continue
        if digit_list[index+1] == digit:
            dupe_found = True
            break

    if not dupe_found:
        return

    sorted_list = digit_list.copy()
    sorted_list.sort()

    if digit_list == sorted_list:
        return password

def find_password_in_range(min, max):
    output = []
    if max < 100000 or min > 1000000 or min > max:
        return 'Password is a 6 digit number, range is wrong'

    for n in range(min, max):
        attempt = check_password_full_reqs(n)
        if attempt:
            output.append(attempt)
    return output

def main(): 
    answer = find_password_in_range(min=123257, max=647015)
    print(answer)
    print(len(answer))

if __name__ == "__main__":
    main()

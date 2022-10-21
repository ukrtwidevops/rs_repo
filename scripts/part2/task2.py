def balanced_num(number):
    string = str(number)
    if len(string) < 3:
        return 'Balanced'
    else:
        print(len(string) % 2)
        if not len(string) % 2:
            left = string[:int(len(string) / 2) - 1]
            right = string[-int(len(string) / 2) + 1:]
            print(left, right)
        else:
            left = string[:int(len(string) / 2)]
            right = string[-int(len(string) / 2):]
            print(left, right)
    right = [int(x) for x in right]
    left = [int(x) for x in left]
    return 'Balanced' if sum(left) == sum(right) else 'Not Balanced'
def never_decrease(num):
    for i in range(5):
        if num[i] > num[i + 1]:
            return False
    return True


def has_same_not_in_group(num):
    if num[2] != num[1] and num[1] == num[0]:
        return True
    for i in range(1, 4):
        if num[i] == num[i + 1] and num[i] != num[i + 2] and num[i - 1] != num[i]:
            return True
    if num[3] != num[4] and num[4] == num[5]:
        return True
    return False


if __name__ == '__main__':
    low = 271973
    high = 785961
    sum = 0
    for i in range(low, high):
        if never_decrease(str(i)) and has_same_not_in_group(str(i)):
            sum += 1
    print(sum)

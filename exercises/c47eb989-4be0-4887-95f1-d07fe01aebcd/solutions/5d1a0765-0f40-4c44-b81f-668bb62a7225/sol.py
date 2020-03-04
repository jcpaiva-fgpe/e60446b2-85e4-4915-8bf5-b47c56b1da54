def divisible_by_7_not_multiple_of_5(begin, end):
    res = []
    for i in range(begin, end):
        if (i % 7 == 0) and (i % 5 != 0):
            res.append(str(i))
    return res

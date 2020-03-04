import random

f = open(input())
source = f.read()
exec(source)


nr_of_tests = int(input())

for i in range(0, nr_of_tests):
    begin = random.randint(0, 10000)
    end = random.randint(begin, 10000)

    f = open("tests/in" + str(i+1) + ".txt", "w+")
    f.write("%d\n%d\n" % (begin, end))
    f.close()

    out = divisible_by_7_not_multiple_of_5(begin, end)

    f = open("tests/out" + str(i+1) + ".txt", "w+")
    f.write('\n'.join(out))
    f.close()


def odd_num_gen(n):
    for i in range(n):
        if i % 2 != 0:
            yield i


for i in odd_num_gen(10):
    print(i)

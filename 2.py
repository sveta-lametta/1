def res(t):
    for num in t:
        split_num = str(num)
        split_num_l = list(split_num)
        sp = []
        i = 0
        for i in range(len(split_num_l)):
            if int(split_num_l[i]) % 2 == 0:
                sp.append(int(split_num_l[i]))
                i+=1
            else:
                i+=1
        print(sum(sp))

A = [22, 314]
res(A)
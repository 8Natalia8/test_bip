'''
Created on 5 нояб. 2020 г.

@author: nataa
'''
def help():

   print("---------------------------------\n")
   print("1) для вывода подстановки на экран\n")
   print("2) для вывода таблицы разностей\n")
   print("3) для вывода таблицы разностей подстановки, наиболее вероятных дифференциалов в зависимости от веса\n")
   print("0) для выхода\n")
   print("Любую  цифру для помощи\n")
   print("---------------------------------\n")
def show(table):
    print(end="         ")
    for i in range(16):
        if (i < 10):
            print(i, end="  ")
        else:
            print(i, end=" ")
    print("\n         __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __")
    for i in range(16):
        if (i < 10):
            print(i, " |   ", table[i])
        else:
            print(i, "|   ", table[i])
def create_table_d(S):
    table = [[0 for i in range(16)] for j in range(16)]
    for alpha in range (16):
        for beta in range (16):
            for x in range (16):
                if (S[x ^ alpha]) == (S[x] ^ beta):
                    table[alpha][beta]+=1
    return table
def  count_bit(num):
    bit = 0
    while num != 0:
        bit += num & 1
        num >>= 1
    return bit

def create_weight(S,t):
    t_weight = [[[] for i in range(16)] for j in range(16)]
    mas_W =[[0,[]] for i in range(9)]
    cou=0
    for alpha in range (16):
        for beta in range (16):
            t_weight[alpha][beta].append(count_bit(alpha)+count_bit(beta))
            t_weight[alpha][beta].append(float(t[alpha][beta])/16)
            if t_weight[alpha][beta][1] >= 0:
                f=1
                if(t_weight[alpha][beta][1]>mas_W[t_weight[alpha][beta][0]][0]):
                    mas_W[t_weight[alpha][beta][0]][1].clear()
                    mas_W[t_weight[alpha][beta][0]][0]=t_weight[alpha][beta][1]
                    mas_W[t_weight[alpha][beta][0]][1].append([alpha,beta])
                elif(t_weight[alpha][beta][1]==mas_W[t_weight[alpha][beta][0]][0]):
                    mas_W[t_weight[alpha][beta][0]][1].append([alpha, beta])
                    # print(mas_W[cou], f)

    print("\n---")
    for i in range(9):
        print(i," ", mas_W[i])
    for i in range(16):
        print("")
        for j in range(16):
            print(t_weight[i][j][0],end=" ")
if __name__ == "__main__":
    S=[10, 0, 11, 5, 7, 12, 13, 4, 9, 6, 15, 14, 1, 2, 8, 3]
    help()
    while(1):
        task = int(input())
        if (task==1):
            print("подстановка: S = {}".format(S))
        elif(task==2):
            print("Таблица разности")
            t= create_table_d(S)
            show(t)
        elif(task==3):
            print("parametr")
            t = create_table_d(S)
            create_weight(S,t)
        elif(task==0):
            print("out")
            break
        else:
            help()
        print("---------------------------------\n")


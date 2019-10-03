import random

while True:
    ans = random.randint(1000,9999)
    while True:
        while True:
            put = int(input("input number 1~9999:"))
            if put > 9999 or put < 1000:
                print("please input again")
            else:
                break
        anslist = list(str(ans))
        putlist = list(str(put))
        A=0
        B=0
        for i in range(4):
            if  int(anslist[i] == putlist[i]):
                A+=1
            else:
                B+=1
        if A==4:
            print("Boom")
            break
        else:
            print(A,"A",B,"B")
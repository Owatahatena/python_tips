import random
import matplotlib.pyplot as plt
import numpy as np


def hazure_open(ans):
    hazure = random.randint(0,2)

    while hazure == ans:
        hazure = random.randint(0,2)

    return hazure

def rere_choice(hazure):
    re_choice = random.randint(0,2)

    while re_choice == hazure:
        re_choice = random.randint(0,2)

    return re_choice



def montty(doors):
    ans = random.randint(0,2) #答えの場所
    first_choice = random.randint(0,2)#最初のチョイス

    hazure = hazure_open(ans)

    re_choice = rere_choice(hazure)

    if ans == first_choice and ans == re_choice:
        return 1,1

    elif ans == first_choice and ans != re_choice:
        return 1,0

    elif ans != first_choice and ans == re_choice:
        return 0,1

    else:
        return 0,0


def plot(first_choicelist,re_choicelist):
    x = np.arange(0, 5000, 500)

    # 計算式

    a = len(first_choicelist)
    b = len(re_choicelist)

    c = b -a

    for i in range(c):
        first_choicelist.append(0)


    first_choicelist=np.array(first_choicelist) # ndarray型へキャスト
    re_choicelist=np.array(re_choicelist) # ndarray型へキャスト

    # 横軸の変数。縦軸の変数。
    plt.plot(range(len(first_choicelist)), first_choicelist,label="first_choice")
    plt.plot(range(len(first_choicelist)), re_choicelist,label="re_choice",)

    plt.title('kakuritu')

    # ラベルの描画
    plt.legend()

    # 描画実行
    plt.show()

def main():
    a,b = 0,0
    doors = [0,1,2]
    first_choice = 0
    re_choice = 0

    first_choicelist=[]
    re_choicelist=[]

    print("aa")
    for i in range(10000):
        a,b = montty(doors)
        first_choice += a
        re_choice += b
        first_choicelist.append(first_choice)
        re_choicelist.append(re_choice)

    a = len(first_choicelist)
    b = len(re_choicelist)

    c = b -a

    plot(first_choicelist,re_choicelist)

    print(first_choicelist)

    print("===========================================================")

    print(re_choicelist)

if __name__ == "__main__":
    main()

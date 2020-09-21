import random
# python ./PycharmProjects/pys/terminalCalc/calc.py


def quiz():
    # 変数設定
    integerFirst = random.randint(1, 1000)
    integerSecond = random.randint(1, 1000)
    correct = integerFirst + integerSecond

    # 足し算の出題
    val = input(str(integerFirst) + " + " + str(integerSecond) + " = ")

    # 答え合わせ
    if correct == int(val):
        print('great!')
    else:
        print('Your answer is not correct. Correct answer is' + str(correct))

    # 続ける？続けない？
    more = input('Do you want play more? (y/n)')

    return more


# 足し算ゲーム実行処理
while True:
    flag = quiz()
    if flag == 'n':
        print('bye! thank you for playing!')
        break

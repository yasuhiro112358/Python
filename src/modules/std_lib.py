import random


def practice_02():
    print("practice_02")

    n = random.random() # 0.0 <= n < 1.0
    print(n)

    n = random.randint(1, 6) # 1 <= n <= 6
    print(n)

def practice_03():
    print("practice_03")

    name = ["Taro", "Jiro", "Saburo", "Shiro", "Goro"]
    random.shuffle(name) # 破壊的メソッド
    print(name)

    winner = random.choice(name)
    print(winner)

    # winners = random.choices(name, k=3) # 重複あり
    winners = random.sample(name, k=3) # 重複なし
    print(winners)

    names = ["Taro", "Taro", "Taro", "Taro", "Taro", "Taro", "Taro", "Taro", "Taro", "Taro", "Taro", "Taro", "Jiro", "Saburo", "Shiro", "Goro"]
    names = list(set(names)) # 重複削除 => setにした段階で重複が削除される
    print(names)
    winners = random.sample(name, k=3) # 重複なし
    print(winners)

def practice_04():
    print("practice_04")





def run():
    print("std_lib.py")

    # practice_02()
    # practice_03()
    practice_04()

    # practice_06()
    # practice_07()
    # practice_08()
    # practice_10()
    # practice_11()
    # practice_12()
    # practice_13()
    # practice_15()
    # practice_17()
    # practice_18()
    # practice_19()
    # practice_20()
    # practice_22()
    # practice_23()
    # practice_24()

if __name__ == "__main__":
    run()
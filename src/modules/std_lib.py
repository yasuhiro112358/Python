import random
import math
from math import pi as PI
from math import e as E
import datetime
import calendar
import os
from pprint import pprint
from collections import defaultdict
from collections import Counter

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

    print(PI) # 円周率
    print(E) # ネイピア数
    print(math.sin(PI / 2)) # 1.0
    print(math.cos(PI)) # -1.0
    print(math.tan(PI / 4)) # 1.0
    print(math.sqrt(2)) # 1.4142135623730951
    print(math.log(2)) # 0.6931471805599453
    print(math.log(8, 2)) # 3.0
    print(math.exp(2)) # 7.3890560989306495
    print(math.pow(2, 3)) # 8.0
    # 数直線上で大きい方の整数を返す
    print(math.ceil(3.2)) # 4
    print(math.ceil(-3.2)) # -3
    # 数直線上で小さい方の整数を返す
    print(math.floor(3.2)) # 3
    print(math.floor(-3.2)) # -4
    # 数直線上で0に近い方の整数を返す（よく言われる切り捨て）
    print(math.trunc(3.2)) # 3
    print(math.trunc(-3.2)) # -3
    print(math.fabs(-3.2)) # 3.2
    print(math.modf(3.2)) # (0.20000000000000018, 3.0)
    print(math.fmod(3, 2)) # 1.0
    print(math.fmod(-3, 2)) # -1.0
    print(math.remainder(3, 2)) # -1.0
    print(math.remainder(-3, 2)) # 1.0
    # GCD (Greatest Common Divider): 最大公約数
    print(math.gcd(12, 18)) # 6
    # LCM (Least Common Multiple): 最小公倍数
    print(math.lcm(12, 18)) # 36
    
    # 要注意：round()は四捨五入ではなく、偶数への丸めを行う
    print(round(3.5)) # 4
    print(round(2.5)) # 2

    # 0.1 * 3 は 0.3 にならない（誤差）
    print(0.1 * 3 == 0.3) # False
    # math.isclose()を使うと誤差を考慮して比較できる（デフォルトでは1e-09）
    print(math.isclose(0.1 * 3, 0.3)) # True

def practice_06():
    print("practice_06")

    now = datetime.datetime.now()
    print(now) 
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.microsecond)
    print(now.weekday()) # 0: 月曜日, 1: 火曜日, 2: 水曜日, 3: 木曜日, 4: 金曜日, 5: 土曜日, 6: 日曜日
    now_formatted = now.strftime("%B %d %A, %Y")
    print(now_formatted)

    birthday = datetime.datetime(1989, 5, 8)
    print(birthday)

    birthday = datetime.datetime.strptime("1989-05-08", "%Y-%m-%d")
    print(birthday)

def practice_08():
    print("practice_08")

    day1 = datetime.datetime(year=2000, month=4, day=11)
    day2 = datetime.datetime(year=2001, month=1, day=1)
    diff = day2 - day1 # timedelta
    diff_days = diff.days
    print(diff_days)

    delta = datetime.timedelta(days=3, hours=5) # timedelta
    day3 = day1 + delta
    print(day3)

def practice_09():
    print("practice_09")

    calendar.setfirstweekday(calendar.SUNDAY)
    cal_str = calendar.month(2001, 1)
    print(cal_str)

    cal_data = calendar.monthcalendar(2001, 1)
    print(cal_data)

    # 2000年は閏年
    print(calendar.isleap(2000)) # True
    print(calendar.isleap(2001)) # False

def practice_10():
    print("practice_10")

    output_dir = os.path.join(os.path.dirname(__file__), "../../output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path =  os.path.join(output_dir, "names.txt")

    # f = open(file_path, mode="w")
    # f.write("Taro\n")
    # f.close()

    with open(file_path, mode="w") as f: # withブロックを抜けると自動的にcloseされる
        f.write("Taro\n")
        f.write("Jiro\n")
        f.write("Saburo\n")

def practice_11():
    print("practice_11")

    output_dir = os.path.join(os.path.dirname(__file__), "../../output")
    file_path =  os.path.join(output_dir, "names.txt")

    # if not os.path.isfile(file_path): # ファイルが存在しない場合
    #     with open(file_path, mode="w") as f:
    #         f.write("Saburo\n")
    # else: 
    #     print("File exists!")

    try:
        with open(file_path, mode="x") as f: # x: ファイルが存在しない場合のみ書き込み
            f.write("Saburo\n")
    except FileExistsError:
        print("File exists!")

def practice_12():
    print("practice_12")

    names = ["Taro", "Jiro", "Saburo", "Shiro", "Goro"]

    output_dir = os.path.join(os.path.dirname(__file__), "../../output")
    file_path =  os.path.join(output_dir, "names.txt")

    with open(file_path, mode="a") as f:
        for name in names:
            f.write(f"{name}\n")

def practice_13():
    print("practice_13")

    output_dir = os.path.join(os.path.dirname(__file__), "../../output")
    file_path =  os.path.join(output_dir, "names.txt")

    with open(file_path, mode="r") as f:
        names = f.read()
        print(names)
        
    with open(file_path, mode="r") as f:
        names = f.read().splitlines()
        print(names)
    
def practice_14():
    print("practice_14")

    scores = [
        {"name": "Taro", "math": 70, "english": 82},
        {"name": "Jiro", "math": 67, "english": 61},
        {"name": "Saburo", "math": 81, "english": 58},
        ]
    print(scores)
    pprint(scores) # pretty print

def practice_15():
    print("practice_15")

    results = ["pass", "fail", "pass", "fail", "pass", "fail", "pass", "fail", "pass", "pass"]

    # stats = {}
    # for result in results:
    #     if result not in stats:
    #         stats[result] = 0
    #     stats[result] += 1


    # def init():
    #     return 0
        
    # stats = defaultdict(init) # 初期値を設定
    # for result in results:
    #     stats[result] += 1

    
    stats = defaultdict(lambda: 0) # 初期値を設定
    for result in results:
        stats[result] += 1


    print(dict(stats))

def practice_17():
    print("practice_17")

    results = ["pass", "fail", "pass", "fail", "pass", "fail", "pass", "fail", "pass", "pass"]
    stats = Counter(results)

    print(dict(stats))

def practice_18():
    print("practice_18")

    results = [
        ("pass", "Taro"),
        ("fail", "Jiro"),
        ("pass", "Saburo"),
        ("fail", "Shiro"),
        ("pass", "Goro"),
        ("fail", "Rokuro"),
        ("pass", "Shichiro"),
        ("fail", "Hachiro"),
        ("pass", "Kuro"),
        ("pass", "Juro"),
    ]

    stats = defaultdict(list)

    for result, name in results:
        stats[result].append(name)

    print(dict(stats))

def practice_19():
    print("practice_19")


def run():
    print("std_lib.py")

    # practice_02()
    # practice_03()
    # practice_04()
    # practice_06()
    # practice_08()
    # practice_09()
    # practice_10()
    # practice_11()
    # practice_12()
    # practice_13()
    # practice_14()
    # practice_15()
    # practice_17()
    # practice_18()
    practice_19()
    
if __name__ == "__main__":
    run()
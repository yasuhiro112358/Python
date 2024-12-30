def practice_02():
    print("practice_02")

    scores = [10, 20, 30]
    print("scores")
    print(scores)
    print()

    print("scores[0]")
    print(scores[0])
    print()

    print("scores[1]")
    print(scores[1])
    print()

    print("scores.append(60)")
    scores.append(60)
    print("scores")
    print(scores)
    print()

    print("scores.extend([70, 80])")
    scores.extend([70, 80])
    print("scores")
    print(scores)
    print()

    print("scores += [110, 120]")
    scores += [110, 120]
    print("scores")
    print(scores)
    print()

    print("scores *= 3")
    scores *= 3
    print("scores")
    print(scores)
    print()

    print("scores.insert(1, 15)")
    scores.insert(1, 15)
    print("scores")
    print(scores)
    print()

    print("scores.remove(20)")
    scores.remove(20)
    print("scores")
    print(scores)
    print()

    print("popped_item = scores.pop(3)")
    popped_item = scores.pop(3)
    print("popped_item")
    print(popped_item)
    print("popped_item = scores.pop()")
    popped_item = scores.pop()
    print("popped_item")
    print(popped_item)
    print("scores")
    print(scores)
    print()

    print("del scores[0]")
    del scores[0]
    print("scores")
    print(scores)
    print()

    print("scores.clear()")
    scores.clear()
    print("scores")
    print(scores)
    print()

def practice_06():
    print("practice_06")
    
    scores = [10, 20, 30, 20, 40]

    print(len(scores)) # 5
    print(min(scores)) # 10
    print(max(scores)) # 40
    print(sum(scores)) # 120

    print(scores.count(20)) # 2
    print(scores.index(20)) # 1

    print(20 in scores) # True
    print(100 in scores) # False

def practice_07():
    print("practice_07")

    scores = [10, 20, 30, 20, 40]

    scores.reverse() # 破壊的
    print(scores) # [40, 20, 30, 20, 10]

    scores.sort() # 破壊的
    print(scores) # [10, 20, 20, 30, 40]

    scores.sort(reverse=True) # 破壊的
    print(scores) # [40, 30, 20, 20, 10]

    scores_sorted = sorted(scores, reverse=False) # 非破壊的
    print(scores) # [40, 30, 20, 20, 10]
    print(scores_sorted) # [10, 20, 20, 30, 40]

def practice_08():
    print("practice_08")

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums[2:5] = [200, 300, 400]
    print(nums) # [0, 1, 200, 300, 400, 5, 6, 7, 8, 9]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums[2:2] = [1.5]
    print(nums) # [0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums[:3] = []
    print(nums) # [3, 4, 5, 6, 7, 8, 9]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums[3:] = []
    print(nums) # [0, 1, 2]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = nums[2:5]
    print(nums) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sliced_list) # [2, 3, 4]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = nums[2:8:2]
    print(sliced_list) # [2, 4, 6]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = nums[8:2:-2]
    print(sliced_list) # [8, 6, 4]


    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = nums[::2]
    print(sliced_list) # [0, 2, 4, 6, 8]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = nums[::-1]
    print(sliced_list) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def practice_10():
    print("practice_10")

    prices = [100, 200, 150, 200, 100]

    for price in prices:
        print(price * 1.1)

    for index, price in enumerate(prices):
        print(f"{index}: {price *1.1:.2f}")

def practice_11():
    print("practice_11")

    prices = [100, 200, 150, 200, 100] 
    prices_with_tax = [price * 1.1 for price in prices] # リスト内包表記
    print(prices_with_tax)

def practice_12():
    print("practice_12")

    prices = [100, 200, 150, 200, 100] 

    # prices_with_tax =[]
    # for price in prices:
    #     if price != 200:
    #         prices_with_tax.append(price * 1.1)

    prices_with_tax = [price * 1.1 for price in prices if price != 200]

    print(prices_with_tax)

def practice_13():
    print("practice_13")

    tokyo = ("JPY", 36, 140)
    print(tokyo)
    print(tokyo[0])

    tokyo = list(tokyo)
    print(tokyo)
    tokyo[0] = "YEN"
    print(tokyo)
    tokyo = tuple(tokyo)
    print(tokyo)

    tokyo = ("JPY", 36, 140)
    currency, lat, lng = tokyo
    print(currency)
    print(lat)
    print(lng)

    tokyo = ("JPY", 36, 140)
    currency, *coords = tokyo
    print(currency)
    print(coords)

    tokyo = ("JPY", 36, 140)
    _, lat, lng = tokyo
    print(lat)
    print(lng)

    tokyo = ("JPY", 36, 140)
    currency, *_ = tokyo
    print(currency)

def practice_15():
    print("practice_15")

    # シーケンス型
    scores = [10, 20, 30, 20, 40]
    tokyo = ("JPY", 36, 140)
    name = "Taro Yamada" # タプルと同様に要素の変更はできない

    print(name[0])
    print(name[:4])

    replaced_string = name.replace("Taro", "Jiro") # 非破壊
    upper_string = name.upper() # 非破壊
    print(replaced_string)
    print(upper_string)
    print(name)

    birthday = "1989-05-08"
    print(birthday.split("-")) # ['1989', '05', '08']

    year, month, day = birthday.split("-")
    print(year)
    print(month)
    print(day)

    birthday2 = ["1992", "02", "29"]
    # joinメソッドは文字列にしか使えない
    print("-".join(birthday2)) # 1992-02-29

    birthday3 = [1992, 2, 29]
    print("-".join([str(n) for n in birthday3])) # 1992-2-29

def practice_17():
    print("practice_17")

    scores = {"math": 62, "english": 91, "physics": 84}
    scores["math"] = 100
    scores["history"] = 88

    del scores["physics"]

    popped_item = scores.pop("english")

    print(scores)
    print(scores["math"])

    print(popped_item)

def practice_18():
    print("practice_18")

    scores = {"math": 62, "english": 91, "physics": 84}

    for key in scores.keys():
        print(key)

    for value in scores.values():
        print(value)

    for item in scores.items():
        print(item)
        key, value = item
        print(f"{key:8} {value:3}")

    for key, value in scores.items():
        print(f"{key:8} {value:3}")

def practice_19():
    print("practice_19")

    # 集合
    members = {"Taro", "Jiro", "Saburo", "Taro"}
    print(members) # {'Jiro', 'Taro', 'Saburo'}
    print(len(members)) # 3
    print("Jiro" in members) # True

    members.add("Shiro")
    print(members) # {'Jiro', 'Taro', 'Shiro', 'Saburo'}

    members.remove("Taro")
    print(members) # {'Jiro', 'Shiro', 'Saburo'}

    frozen_members = frozenset(members)
    print(frozen_members) # frozenset({'Jiro', 'Shiro', 'Saburo'})

def practice_20():
    print("practice_20")

    # リスト
    eng_members_list = ["Taro", "Jiro", "Saburo"]
    math_members_list = ["Jiro", "Saburo", "Shiro"]

    # リストから集合に変換
    eng_members_set = set(eng_members_list)
    math_members_set = set(math_members_list)

    # 集合の演算
    print(eng_members_set | math_members_set) # 和集合
    print(eng_members_set & math_members_set) # 積集合
    print(eng_members_set - math_members_set) # 差集合
    print(math_members_set - eng_members_set) # 差集合

def practice_22():
    print("practice_22")

    nums = [10, 20, 30]
    # nums_copy = nums # 参照渡し（値のコピーはされない）
    nums_copy = nums.copy()
    nums[0] = 100

    print(nums) # [100, 20, 30]
    print(nums_copy) # [10, 20, 30]

def practice_23():
    print("practice_23")

    keys = ["math", "english", "physics"]
    values = [62, 91, 84]

    scores = {}

    # for item in zip(keys, values):
    #     print(item)
    #     key, value = item
    #     scores[key] = value

    # for key, value in zip(keys, values):
    #     scores[key] = value

    scores = {key: value for key, value in zip(keys, values)}

    print(scores)

def practice_24():
    print("practice_24")

    scores = [
        {"name": "Taro", "math": 70, "english": 82},
        {"name": "Jiro", "math": 67, "english": 61},
        {"name": "Saburo", "math": 81, "english": 58},
        ]
    
    # def compare(score):
    #     return score["math"]
    
    # scores.sort(key=compare, reverse=True)
    
    scores.sort(key=lambda score: score["math"], reverse=True)



    print("Name     Math     English")
    print("-------- -------- --------")

    for score in scores:
        print(f"{score['name']:8} {score['math']:8} {score['english']:8}")

        # for value in score.values():
        #     print(f"{value:8} ", end="")
        # print()



def run():
    print("data_struct.py")
    # practice_02()
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
    practice_24()

if __name__ == "__main__":
    run()
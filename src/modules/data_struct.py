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


def run():
    print("data_struct.py")
    # practice_02()
    # practice_06()
    # practice_07()
    # practice_08()
    # practice_10()
    # practice_11()
    practice_12()


if __name__ == "__main__":
    run()
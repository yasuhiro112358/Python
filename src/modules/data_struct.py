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
    
    scores.reverse()
    print(scores) # [40, 20, 30, 20, 10]

    
def run():
    print("data_struct.py")
    # practice_02()
    # practice_06()
    practice_07()

if __name__ == "__main__":
    run()
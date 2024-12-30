def run():
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



if __name__ == "__main__":
    run()
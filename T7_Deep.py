question = input("What is the Answer to the Great Question of Life,the Universe, and Everything? ")

match question:
        case "42" | "forty-two" | "forty two":
            print("YES")
        case _:
            print("NO")
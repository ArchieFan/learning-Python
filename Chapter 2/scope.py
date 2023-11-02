name = "Archie"
count = 1


def another():
    color = "black"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Archie Fan")


another()
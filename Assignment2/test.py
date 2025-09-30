x = 0 # global

def changex():
    global x
    x = 14

def main():
    print(x)
    changex()
    print(x)


main()
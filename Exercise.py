def show_star(n):
    if n > 0:
        for x in range(1, n+1):
            print(x*"*")
    else:
        print("bạn nhập số không đúng")
        input("hãy nhập lại số n")


def show_number(n):
    for x in range(n):
        if x % 2 == 0:
            print(x, "EVEN")
        else:
            print(x, "ODD")


if __name__ == '__main__':
    n = int(input("hãy nhập số n:"))
    print("---------Bài 1 --------")
    show_star(n)
    print("---------Bài 2 --------")
    show_number(n)

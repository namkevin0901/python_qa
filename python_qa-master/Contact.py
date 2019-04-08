def contact(lst, name, phone):
    lst.append({
        'name': name,
        'phone': phone
    })
    return lst

if __name__ == "__main__":
    lst = []
    while True:
        name = input("Input your name:")
        phone = input("Input your phone:")
        s = input("Do you want more?")
        lst = contact(lst, name, phone)
        if s == "N":
            ss = input("Do you want to check contact?")
            if ss == "Y":
                n = input("What's contact?")
                print(lst[int(n)-1])
            break

def checkspeed(speed):
    if speed <= 70:
        print('Ok!!')
    else:
        _checkspeed = (speed - 70) // 5
        if _checkspeed >= 12:
            print('License suspended')
        else:
            print('Point: ', _checkspeed + 1)


if __name__ == "__main__":
    speed = int(input("Your speed is:"))
    checkspeed(speed)

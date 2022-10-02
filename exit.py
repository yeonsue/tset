def echo():
    a = input("입력하세요")
    print(a)
    return 0
def exit():
    while True:
        a = input("입력하세요")
        if a=="exit":
            print("프로그램을 종료합니다")
            break
        else:
            print(a)
exit()
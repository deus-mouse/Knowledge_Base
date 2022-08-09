
# мультимножество сможет содержать одинаковые элементы
def multy_set():
    setsize = 10
    myset = [[] for _ in range(setsize)]
    print(f'{myset=}')


    def add(x):
        myset[x % setsize].append(x)


    def find(x):
        for now in myset[x % setsize]:
            if now == x:
                return True
        return False


    def delete(x):
        xlist = myset[x % setsize]
        for i in range(len(xlist)):
            if xlist[i] == x:
                # xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]  # swap, но он лишний
                xlist[i] = xlist[len(xlist) - 1]  # можно же просто присвоить 1 раз, ибо ниже мы удалим последний элемент
                xlist.pop()
                return


# множество правильное
def my_set():
    setsize = 10
    myset = [[] for _ in range(setsize)]
    print(f'{myset=}')


    def add(x):
        if not find(x):
            myset[x % setsize].append(x)


    def find(x):
        for now in myset[x % setsize]:
            if now == x:
                return True
        return False


    def delete(x):
        xlist = myset[x % setsize]
        for i in range(len(xlist)):
            if xlist[i] == x:
                # xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]  # swap, но он лишний
                xlist[i] = xlist[len(xlist) - 1]  # можно же просто присвоить 1 раз, ибо ниже мы удалим последний элемент
                xlist.pop()
                return


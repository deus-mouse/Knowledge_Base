

x = 2
y = 6

try:
    x = int(x)
    y = int(y)

    res = x/y

except ZeroDivisionError as z:
    res = z
except ValueError as v:
    res = v
else:
    print('ELSE')


print(res)



def foo():
    counter = 0
    try:
        counter += 1
        # return counter
    except Exception as ex:
        print('except')
    else:
        print('else')
    finally:
        print('finally')


print(foo())
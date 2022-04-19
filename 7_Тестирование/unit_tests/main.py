'''
https://www.youtube.com/watch?v=ptssYZR4kus
'''

# На 100 г мяса
#
# Нитратная соль 10
# Поваренная соль 15
# Стартовые культуры 0.5
# Моносахара 5
# 2 дня каждые 500 г

def nitro_salt(m):
    # 1000 ^ 10 = m : x
    try:
        m = int(m)
    except:
        m = 0
    x = int(10 * m / 1000)
    return x
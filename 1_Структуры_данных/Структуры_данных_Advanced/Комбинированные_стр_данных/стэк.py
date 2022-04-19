class FILO:  # стэк
    def __init__(self):
        self.queue = []

    def put(self, value):
        self.queue.append(value)

    def get(self):
        return self.queue.pop()  # последний элемент


filo = FILO()
filo.put(1)
filo.put(2)
print(f'{filo.get()=}')
print(f'{filo.get()=}')

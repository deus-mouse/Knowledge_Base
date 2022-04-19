# Реализация Python класса узла, используемая для создания объектов узла


class Node(object):
	def __init__(self, item):
		# Информационная область
		self.item = item
		# Ссылка на домен
		self.next = None


# Реализация Python связанного списка, используемая для создания объектов связанного списка
class LinkList(object):
	def __init__(self):
		# Записать головной узел, сохранить объект узла
		self.head = None

	def is_empty(self):
		# Если головной узел пуст, связанный список пуст
		# Потому что головной узел хранит объект узла
		return self.head is None

	def add(self, item):
		# Создать объект узла
		node = Node(item)
		# объект узла указывает на текущий головной узел
		node.next = self.head
		# head хранит объект head-узла
		self.head = node

	def append(self):
		# Создать объект узла
		node = Node(item)
		# Связанный список пуст, непосредственно хранится в голове
		if self.is_empty():
			self.head = node
		# Перейдите связанный список до конца и добавьте
		else:
			cur = self.head
			# Поле ссылки последнего элемента связанного списка - Нет
			while cur.next:
				cur = cur.next
			cur.next = node

	def insert(self, position, item):
		# Вставка позиции
		# 0, то есть вставка головного узла, вызов метода add
		if position == 0:
			self.add(item)
		# Вставить узел в любую позицию
		elif 0 < position <= self.len():
			node = Node(item)
			count = 0
			cur = self.head
			while cur:
				if position == count + 1:
					# Вставить узел
					node.next = cur.next
					cur.next = node
				cur = cur.next
				count += 1
		# Контроль дальности, исключение за пределы границ
		else:
			raise 'index out of range'

	def len(self):
		cur = self.head
		count = 0
		# Счетчик обхода
		while cur:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		# Взять элемент
		cur = self.head
		while cur:
			print(cur.item, end='-->')
			cur = cur.next
		print('None')

	def remove(self, item):
		# Текущий узел
		cur = self.head
		# Сохранить предыдущий узел текущего узла
		cur_pre = None
		while cur:
			# Траверс равный
			if cur.item == item:
				# Если это головной узел
				if cur_pre is None:
					self.head = cur.next
				# В других случаях удалить текущий узел
				else:
					cur_pre.next = cur.next
			cur_pre = cur
			cur = cur.next

	def search(self, item):
		cur = self.head
		while cur:
			# Найти истину
			if cur.item == item:
				return True
			cur = cur.next
		# Конец обхода, возврат False
		return False

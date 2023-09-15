'''
Команда
Шаблоны программирования не придумывают, их обнаруживают. Они существуют, программист просто должен найти их и использовать.

Иногда требуется разделить во времени подготовку операции и ее совершение. Все подготовительные шаги объединяются в одной Команде. Это позволяет добавлять дополнительные функциональные возможности. Так можно реализовать отмену совершенного действия или его повтор.
'''

class RenameFileCommand(object):
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)

class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
history.undo()
history.undo()
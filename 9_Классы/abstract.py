import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self,):
        raise NotImplementedError


class NewAbstractRepository(AbstractRepository):
    def none_add(self):
        raise NotImplementedError



new = NewAbstractRepository()
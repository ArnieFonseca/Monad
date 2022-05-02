"""Maybe Functor/Monad implementation"""
from typing import Any, Callable
from abc import ABC

class Maybe(ABC):
    """Forward Referece Class"""

class Maybe(ABC):
    """Abstract class that represet the presence of a value Some/Just or absence of it None/Nothing"""

    def is_has_value(self):
        """Function to check is the instance has a value or not"""

    def map(self, func:Any)->Maybe:
        """Tranformation to another Functor"""

    def match(self,fn_just:Callable,fn_nothing:Callable)->Maybe:
        """Method to unwrap the value for Just or None"""

    def bind(self,func)->Maybe:
        """Method to unwrap and call another function """

    def __str__(self)->str:
        """Method for string representation"""

    def __or__(self, func:Any):
        pass

class Just(Maybe):
    """Just derive class that represet the existance of the value"""

    def __init__(self, value):
        self.value = value

    def is_has_value(self):
        return True
    def map(self, func):
        try:
            result = func(self.value)
            return Just(result)
        except Exception:
            return Nothing()
    def match(self,fn_just,fn_nothing):
        return fn_just(self.value)
    def bind(self,func)->Maybe:
        return func(self.value)
    def __str__(self)->str:
        return 'Just(' + str(self.value) + ')'
    def __or__(self, func):
        return self.map(func)

class Nothing(Maybe):
    """Nothing derive class the represet the absence of a value"""
    def __init__(self):
        pass
    def is_has_value(self):

        return False
    def map(self, func):

        return Nothing()
    def match(self,fn_just,fn_nothing):
        return fn_nothing (None)
    def bind(self,func):
        return Nothing()
    def __str__(self)->str:
        return 'Nothing()'
    def __or__(self, func):
        return self.map(func)

def tryCatch(func:Callable)->Maybe:
    """Generalized Try/Catch The input function will be evaluate, onsucess an embelished/elevated
    result will be returned otherwise Nothing\n
    tryCatch:: func:Callable -> Maybe"""
    try:
        return Just(func())
    except:
        return Nothing()

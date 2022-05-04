"""Either Functor/Monad implementation"""
from typing import Any, Callable
from abc import ABC

class Either(ABC):
    """Forward Referece Class"""

class Either(ABC):
    """Abstract class that represet the presence of a value Some/Right
     or absence of it None/Left"""

    def is_left(self):
        """Function to check is the instance is Left"""
    
    def is_right(self):
        """Function to check is the instance is Right"""

    def map(self, func:Any)->Either:
        """Tranformation to another Functor"""

    def match(self,fn_Right
    :Callable,fn_Left:Callable)->Either:
        """Method to unwrap the value for Right
         or None"""

    def bind(self,_:Any)->Either:
        """Method to unwrap and call another function """

    def __str__(self)->str:
        """Method for string representation"""

    def __or__(self, _:Any):
        pass
    
    @staticmethod
    def tryCatch(func:Callable)->Either:
        """Generalized Try/Catch The input function will be evaluate, onsucess an embelished/elevated
        result will be returned otherwise Left\n
        tryCatch:: func:Callable -> Either"""
        try:
            return Right(func())
        except Exception:
            x = func.__code__.co_filename.rfind("\\")
            name = func.__code__.co_filename[x+1:]
            error = "Error in file {0} line number {1}".format(name, func.__code__.co_firstlineno)
            return Left(error)

class Right(Either):
    """Right derive class that represet the existance of the value"""

    def __init__(self, value):
        self.value = value

    def is_left(self):
        """Function to check is the instance is Left"""
        return False

    def is_right(self):
        """Function to check is the instance is Right"""
        return True

    def map(self, func):
        try:
            result = func(self.value)
            return Right(result)
        except Exception:
            return Left("Unable to map")
    def match(self,fn_Right ,fn_Left):
        return fn_Right(self.value)
    def bind(self,func)->Either:
        return func(self.value)
    def __str__(self)->str:
        return 'Right(' + str(self.value) + ')'
    def __or__(self, func):
        return self.map(func)

class Left(Either):
    """Left derive class the represet the absence of a value"""
    def __init__(self, value):
        self.value = value

    def is_left(self):
        """Function to check is the instance is Left"""
        return True
    def is_right(self):
        """Function to check is the instance is Right"""
        return False
    def map(self, func):
        return Left(self.value)
    def match(self,fn_Right ,fn_Left):
        return fn_Left (self.value)
    def bind(self,func):
        return Left(self.value)
    def __str__(self)->str:
        return 'Left()'
    def __or__(self, func):
        return self.map(func)

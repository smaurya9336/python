from abc import abstractmethod,ABC
class test(ABC):
    @abstractmethod
    def msg(self):
        pass

class c(test):
    def msg(self):
        print("HELLO I AM FROM ABSTRACT METHOD")



x=c()
x.msg()
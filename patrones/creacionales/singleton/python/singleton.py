class SingletonMeta(type):
    _instances = {}
    
    def __call__(self, *args, **kwards):
        if self not in self._instances:
            instance = super().__call__(*args, **kwards)
            self._instances[self] = instance
        return self._instances[self]

class Singleton(metaclass = SingletonMeta):

    def some_logic():
        pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")



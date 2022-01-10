from threading import Lock, Thread

class SingletonMeta(type):
    _instance = {}
    _lock: Lock = Lock()

    def __call__(self, *args, **kwards):
        with self._lock:
            if self not in self._instance:
                instance = super().__call__(*args, **kwards)
                self._instance[self] = instance
        return self._instance[self]

class Singleton(metaclass = SingletonMeta):
    value: str = None
    def __init__(self, value: str) -> None:
        self.value = value
    
    def some_business_logic(self):
        pass

def test_singleton(value: str)->None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    process1 = Thread(target=test_singleton, args = ("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()


from threading import Lock, Thread

class InstitucionEducativoMeta(type):

    _instancia: dict = {}

    _lock: Lock = Lock()

    def __call__(self, *args, **kwards):
        with self._lock:
            if self not in self._instancia:
                instancia = super().__call__(*args, **kwards)
                self._instancia[self] = instancia
        return self._instancia[self]
    

class InstitucionEducativa(metaclass = InstitucionEducativoMeta):

    def __init__(self, name):
        self.name = name



def test_singleton(name):
    i_educativa1 = InstitucionEducativa(name)
    print(i_educativa1.name)

if __name__ == "__main__":
    hilo1 = Thread(target = test_singleton, args=('Gotitas del saber',))
    hilo2 = Thread(target = test_singleton, args=('Gotitas del saber',))
    hilo1.start()
    hilo2.start()



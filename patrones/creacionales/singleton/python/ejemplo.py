class InstitucionEducativoMeta(type):

    _instance: dict = {}

    def __call__(self, *args, **kwards):
        if self not in self._instance:
            instance = super().__call__(*args, **args)
            self._instance[self] = instance
        return self._instance[self]

def InstitucionEducativo(metaclass = InstitucionEducativoMeta):

    name: str = None
    def __init__(self, name: str)-> None:
        self.name = name

if __name__ == '__main__':
    i_educativo1 = InstitucionEducativo('Educativos')
    i_educativo2 = InstitucionEducativo('Gotitat Saber')

    if id(i_educativo1) == id(i_educativo2):
        print(f"Singleton works, both variables contain the same instance. {id(i_educativo1)} - {id(i_educativo1)}")
    else:
        print("Singleton failed, variables contain different instances.") 
class Producto():
    def __init__(self, descripcion = "", precio = 0, tipo = ""):
        self._descripcion = descripcion
        self._precio = precio 
        self._tipo = tipo

    @property
    def descripcion(self):
        return self._descripcion 

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion 

    @property
    def tipo(self):
        return self._tipo 

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def precio(self):
        return self._precio 

    @precio.setter
    def precio(self, precio):
        self._precio = precio
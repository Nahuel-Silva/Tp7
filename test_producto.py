import unittest
from producto import Producto
from productoServices import ProductoService
from repositorios import Repositorios
from parameterized import parameterized

class TestProducto(unittest.TestCase):
    maxDiff = None

    def test_uso_property(self):
        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras'})

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras'})

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras'),
            ("samsung s10", 200000, 'celular'),
            ("samsung s20", 400000, 'celular'),
            ("acer", 6000500, 'computadoras'),
            ("HP", 6000000, 'computadoras'),
        ])
    # Agregar un producto
    def test_add_producto(self, descripcion, precio, tipo):
        producto = Producto(descripcion, precio, tipo)
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto. __dict__)
    
    @parameterized.expand([
            ("ascendente",  {0: {'_descripcion': 'samsung s10', '_precio': 200000,'_tipo': 'celular'}, 1: {'_descripcion': 'samsung s20', '_precio': 400000, '_tipo': 'celular'}, 2: {'_descripcion': 'lenovo t490', '_precio': 6000000, '_tipo': 'computadoras'}, 3: {'_descripcion': 'HP', '_precio': 6000000, '_tipo': 'computadoras'}, 4: {'_descripcion': 'acer', '_precio': 6000500, '_tipo': 'computadoras'}}),
            ("descendente", {0: {'_descripcion': 'acer', '_precio': 6000500, '_tipo': 'computadoras'}, 1: {'_descripcion': 'lenovo t490', '_precio': 6000000, '_tipo': 'computadoras'}, 2: {'_descripcion': 'HP', '_precio': 6000000, '_tipo': 'computadoras'}, 3: {'_descripcion': 'samsung s20', '_precio': 400000, '_tipo': 'celular'}, 4: {'_descripcion': 'samsung s10', '_precio': 200000, '_tipo': 'celular'}}),
        ])
    def test_insertion_sort_precio(self, tipo_orden, list_ordenada):
        lista_ordenada = ProductoService().\
         insertion_sort_precio(Repositorios.productosList, tipo_orden)
        print("*****************************************")
        print (lista_ordenada)
        self.assertDictEqual(lista_ordenada, list_ordenada)

    # Eliminar un producto
    def test_delete_producto(self):
        producto = Producto("HP", 45555, 'computadora')
        productoKey = ProductoService().add_producto(producto)
        ProductoService().delete_producto(productoKey)
        self.assertEqual(Repositorios.productosList.get(productoKey), None)

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras')
    ])
    # Verificar la exeptionfrom person import Person
    def test_delete_producto_value_error(self, descripcion, precio, tipo):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().delete_producto(long_list+1)

if __name__ == '__main__':
    unittest.main()
from producto import Producto
from productoServices import ProductoService

"#menu"


class Menu():

    def menu_inicio(self):
        print("\n\n1. Entrar al menu")
        print("2. No entrar al menu")
        return int(input("Elija una opción: "))

    def menu_producto(self):
        print("\n\n1. Agregar producto")
        print("2. Modificar datos del producto")
        print("3. Eliminar producto")
        print("4. Listar producto")
        print("5. terminar operaciones")
        return int(input("Elija una opción: "))


if __name__ == '__main__':
    productService = ProductoService()
    menu = Menu()
    opcion = Menu.menu_inicio({})
    while True:
        if opcion == 1:
            numero = Menu.menu_producto({})
            if numero == 1:
                p1 = Producto()
                p1 = productService.crearProducto()
                productService.add_producto(p1)
            if numero == 2:
                clave = int(input(
                    'Elija la key del producto que desea modificar: '
                ))
                productService.update_producto(clave)
            if numero == 3:
                clave = int(input(
                    'Elija la clave del producto que desea eliminar: '
                ))
                productService.delete_producto(clave)
            if numero == 4:
                print(productService.get_productosList())
            if numero == 5:
                break
        if opcion == 2:
            break
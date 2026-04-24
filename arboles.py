from bigtree import print_tree
from bigtree import Node

def buscar(nodo,nom):
    if nodo.name==nom:
        return nodo
    else:
        for i in nodo.children:
            encon=buscar(i,nom)
            if encon:
                return encon

cent=0
while cent!=6:
    opc=int(input("1. Vacuidad, 2. Cantidad de elementos, 3. Imprimir el arbol, 4. Ingresar, 5. Buscar, 6. Salir: "))
    if opc==1:
        if Node is None:
            print("El arbol esta vacio")
        else:
            print("El arbol no esta vacio")
    elif opc==2:
        cont=0
        for i in root.descendants:
            cont+=1
        print(f"Hay {cont+1} nodos")
    elif opc==3:
        print_tree(root)
    elif opc==4:
        a=int(input("Digite el nombre del nodo: "))
        root=Node(a)
        cent2=0
        for i in range (0,1):
            a=int(input("Digite el nombre del nodo: "))
            Node(a,parent=root)
        root.children
        while cent2!=2:
            print("Desea continuar añadiendo nodos?")
            opc2=int(input("1. Continuar, 2. Salir: "))
            if opc2==1:
                a=int(input("Digite el nombre del nodo: "))
                nombre=int(input("Digite el padre del nodo: "))
                padre=buscar(root,nombre)
                if padre:
                    Node(a,parent=padre)
                else:
                    print("Padre no encontrado")
            elif opc2==2:
                cent2=2
            else:
                print("Opcion invalida")    
    elif opc==5:
        bus=int(input("Digite el nodo a buscar: "))
        node=buscar(bus)
        if node is None:
            print(f"El nodo {bus} no existe")
        else:
            print(f"El nodo {bus} si existe")
    elif opc==6:
        cent=6
    else:
        print("Opcion invalida")

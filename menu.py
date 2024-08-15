import json

def abrirMenu():
    Menu=[]
    with open('Menu.json','r',encoding='utf-8') as openfile:
        Menu = json.load(openfile)  
    return Menu

def guardarMenu(miMenu): 
    with open("Menu.json","w",encoding='utf-8') as outfile:
        json.dump(miMenu,outfile,indent=4)


print("\n1.menu \n2.pedido\n3.pagos")
x=int(input("elije una opcion :"))

print("")

menu = abrirMenu()

if(x==1):
    menus=1
    print("")
     
    print("MENU")

    select=int(input("1. entradas\n2.platos fuertes\n3.bebidas\n\nque deseas agregar a tu pedido : "))
    if select==1:
        for i in menu:
            if i["categoria"] == "entrada":
                print(f"id : {i["id"]}")
                print(f"categoria : {i["categoria"]}")
                print(f"nombre : {i["nombre"]}")
                print(f"precio : {i["precio"]}")
            
                print("")
            

    e=int(input("elije con un numero el plato que deseas :"))   
    for i in menu:
     if e == i["id"]:
        print(f"id :{i["id"]}")
        print(f"categoria : {i["categoria"]}")
        print(f"nombre : {i["nombre"]}")
        print(f"precio : {i["precio"]}")


    if select==2:
         for i in menu:
            if i["categoria"] == "plato_fuerte":
                print(f"id : {i["id"]}")
                print(f"categoria : {i["categoria"]}")
                print(f"nombre : {i["nombre"]}")
                print(f"precio : {i["precio"]}")
                print("")
           


    e=int(input("elije con un numero el plato que deseas :"))
    for i in menu:
        if e == i["id"]:
            print(f"id :{i["id"]}")
            print(f"categoria : {i["categoria"]}")
            print(f"nombre : {i["nombre"]}")
            print(f"precio : {i["precio"]}")

    if select==3:
        for i in menu:
            if i["categoria"] == "bebida":
                print(f"id : {i["id"]}")
                print(f"categoria : {i["categoria"]}")
                print(f"nombre : {i["nombre"]}")
                print(f"precio : {i["precio"]}")
                print("")

    e=int(input("elije con un numero el plato que deseas :"))
    for i in menu:
        if e == i["id"]:
            print(f"id :{i["id"]}")
            print(f"categoria : {i["categoria"]}")
            print(f"nombre : {i["nombre"]}")
            print(f"precio : {i["precio"]}")
             


                


   

    
    
    




    
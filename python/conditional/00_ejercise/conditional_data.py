# tres chicos quieren comprar una consola, pero hay un problema, los precios no estan alado de los estantes, ellos quieren comprar la consola mas cara.
#tenemos que solicitar eldinero que tiene cada uno, si hay dos consolas con el mismo precio mostrar las dos consolas y mostrar el vuelto 
fran_cash=150.000
pablo_cash=200.000
lucas_cash=160.000

console = {
    "xbox360": 200.000,

    "Play5" : 150.000,

    "wii" : 130.000,

    "Play4" : 150.000
}

if fran_cash <= console["Play5"]:
    print(f"fran te podes comprar la consola play5 que vale ${console["Play5"]}")

elif fran_cash <= console["wii"] and fran_cash<= console["xbox360"]:
    print(f"fran te podes comprar la consola xbox360 que vale ${console["xbox360"]}")
elif pablo_cash <= console["xbox360"] and pablo_cash<= console["xbox360"]:
    print(f"pablo te podes comprar la consola xbox360 que vale ${console["xbox360"]}")
elif lucas_cash <= console["play4"] and lucas_cash<= console["play4"]:
    print(f"lucas te podes comprar la consola play4 que vale ${console["xbox360"]}")
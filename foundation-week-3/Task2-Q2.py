chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}

choco=input("What item do you want to buy? white/milk/dark/vegan")
print(choco+ ": " +str(chocolates[choco]))
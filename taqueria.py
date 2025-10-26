menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def price(sum):
    print(f'Total: ${sum}')
    while True:
        try:
            m=input("Item: ")
            if not m.isalpha():
                break
            price(sum + menu[m.title()])
        except KeyError:
            price(sum)
        

        
    
   

price(0)
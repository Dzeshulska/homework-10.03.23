emty_set = set()
def show_product (list_of_stores) :
   for product in list_of_stores: 
        print("\n")
        
while is_running :
    user_choose = input("""
        1) Show products 
        2) Buy products
        3) Quit
    Answer : """).lower()

    if user_choose == "1" :
        show_products(store)

    elif user_choose == "2":
        show_products(store)

        prefer_product = input("Choose product which you want to buy")

        buy_product(prefer_product ,store)
    
    if user_choose == "3" :
         result = is_exit()
         if result == "yes" :
            is_running = False
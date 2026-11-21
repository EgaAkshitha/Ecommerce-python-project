class User:
    def __init__(self,id,username,password,role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def user_dedtails(self):
        return f'{self.id},{self.username},{self.password},{self.role}\n'

class Authentication:
    def register(self):
        id = int(input("Enter your ID: "))
        username = input("Enter you Username: ")
        password = input('Enter your Password: ')
        role = input('Enter your role: ')

        with open('user.txt','r') as file:
            lines = file.readlines()
        is_found = False
        for line in lines:
            details = line.strip().split(',')
            if username == details[1]:
                is_found = True
                break
        if is_found == True:
            print('User Already Exists!')
        else:
            user = User(id,username,password,role)
            with open('user.txt','a') as file:
                file.write(user.user_dedtails())
                print('Successfully Registered!')

    def login(self):
        username = input("Enter you Username: ")
        password = input('Enter your Password: ')

        with open('user.txt', 'r') as file:
            lines = file.readlines()
        is_found = False
        for line in lines:
            details = line.strip().split(',')
            if username == details[1] and password == details[2]:
                print('Login Successfull!')
                return details[0],details[-1]
        if is_found == False:
            print('Invalid Credentials!')

class Product:
    def __init__(self,id,prod_name,price,quantity):
        self.id = id
        self.prod_name = prod_name
        self.price = price
        self.quantity = quantity

    def prod_details(self):
        return f'{self.id},{self.prod_name},{self.price},{self.quantity}\n'

class Admin:
    def add_product(self):
        id = int(input('Enter Product ID: '))
        name = input('Enter Product Name: ')
        price = int(input('Enter Product Price: '))
        quantity = int(input('Enter Product Quantity: '))

        with open('product.txt','r') as file:
            lines = file.readlines()

        with open('product.txt','w') as file:
            is_found = False
            for line in lines:
                details = line.strip().split(',')
                if details[1] == name:
                    is_found = True
                    quantity = int(details[3])+quantity
                    file.write(f'{details[0]},{details[1]},{details[2]},{quantity}')
                else:
                    file.write(line)
        if is_found == False:
            with open('product.txt','a') as file:
                product = Product(id,name,price,quantity)
                file.write(product.prod_details())
                print('Product Added Successfully!')

    def update_product(self):
        id = int(input('Enter id to update product: '))

        with open('product.txt','r') as file:
            lines = file.readlines()

        with open('product.txt','w') as file:
            is_found = False
            for line in lines:
                details = line.strip().split(',')
                if int(details[0]) == id:
                    is_found = True
                    name = input(f'change {details[1]} to: ')
                    price = int(input(f'change {details[2]} to: '))
                    quantity = int(input(f'change {details[3]} to: '))
                    file.write(f'{details[0]},{name},{price},{quantity}\n')
                else:
                    file.write(line)
            if is_found:
                print('Product Updated Successfully!')
            else:
                print('Product with this is does not exist!')

    def remove_product(self):
        id = int(input('Enter id to remove product: '))

        with open('product.txt','r') as file:
            lines = file.readlines()

        with open('product.txt','w') as file:
            is_found = False
            for line in lines:
                details = line.strip().split(',')
                if int(details[0]) == id:
                    is_found = True
                else:
                    file.write(line)
            if is_found:
                print('Product Removed Successfully!')
            else:
                print('Product with this id does not exist!')

    def view_all_products(self):
        with open('product.txt','r') as file:
            lines = file.readlines()
        print('----------------------------------------')
        print('|ID   |NAME      |PRICE     |QUANTITY  |')
        print('----------------------------------------')
        for line in lines:
            details = line.strip().split(',')
            print(f'|{details[0] + ' '*(5-len(details[0]))}|{details[1]+' '*(10-len(details[1]))}|{details[2]+' '*(10-len(details[2]))}|{details[3]+' '*(10-len(details[3]))}|')
        print('----------------------------------------')

    def search_product(self):
        id = int(input('Enter id to search product: '))
        with open('product.txt','r') as file:
            lines = file.readlines()
        is_found = False
        for line in lines:
            details = line.strip().split(',')
            if int(details[0]) == id:
                is_found = True
                print('----------------------------------------')
                print('|ID   |NAME      |PRICE     |QUANTITY  |')
                print('----------------------------------------')
                print(f'|{details[0] + ' '*(5-len(details[0]))}|{details[1]+' '*(10-len(details[1]))}|{details[2]+' '*(10-len(details[2]))}|{details[3]+' '*(10-len(details[3]))}|')
                print('----------------------------------------')
        if not is_found:
            print('Product with this id does not exist!')

class Cart(Admin):
    def __init__(self,user_id):
        self.user_id = user_id

    def add_product_to_cart(self):
        prod_name = input('Enter Product Name: ')

        with open('product.txt','r') as file:
            lines = file.readlines()

        with open('product.txt','w') as file:
            new_product = []
            is_found = False
            for line in lines:
                details = line.strip().split(',')
                if details[1] == prod_name:
                    is_found = True
                    new_product = details
                    quantity = int(details[-1])-1
                    file.write(f'{details[0]},{details[1]},{details[2]},{quantity}\n')
                    print('Product added to the cart successfully!')
                else:
                    file.write(line)
            if is_found:
                new_product.insert(0,self.user_id)
                new_product[-1] = '1'

                with open('cart.txt','r') as file:
                    lines = file.readlines()

                is_found = False
                with open('cart.txt','w') as file:
                    for line in lines:
                        details = line.strip().split(',')
                        if details[2] == prod_name and details[0] == self.user_id:
                            is_found = True
                            quantity = int(details[-1])+1
                            file.write(f'{details[0]},{details[1]},{details[2]},{details[3]},{quantity}\n')
                        else:
                            file.write(line)
                if not is_found:
                    with open('cart.txt','a') as file:
                        file.write(','.join(new_product)+'\n')
            else:
                print('Out of stock!')

    def decrease_quantity(self):
        prod_name = input('Enter Product Name: ')

        with open('cart.txt','r') as file:
            lines = file.readlines()

        with open('cart.txt','w') as file:
            is_found = False
            for line in lines:
                details = line.strip().split(',')
                if details[2] == prod_name and details[0] == self.user_id:
                    is_found = True
                    quantity = int(details[-1])-1
                    if quantity > 0:
                        file.write(f'{details[0]},{details[1]},{details[2]},{details[3]},{quantity}\n')
                else:
                    file.write(line)
            if is_found:
                with open('product.txt','r') as file:
                    lines = file.readlines()

                with open('product.txt','w') as file:
                    for line in lines:
                        details = line.strip().split(',')
                        if details[1] == prod_name:
                            quantity = int(details[-1])+1
                            file.write(f'{details[0]},{details[1]},{details[2]},{quantity}\n')
                        else:
                            file.write(line)
            else:
                print('Product Not Found!')
    def view_cart(self):
        with open('cart.txt','r') as file:
            lines = file.readlines()
        is_found = False
        for line in lines:
            details = line.strip().split(',')
            if details[0] == self.user_id:
                is_found = True
        if is_found:
            print('----------------------------------')
            print('|NAME      |PRICE     |QUANTITY  |')
            print('----------------------------------')
            total_price = 0
            for line in lines:
                details = line.strip().split(',')
                if details[0] == self.user_id:
                    print(f'|{details[2]+' '*(10-len(details[2]))}|{details[3]+' '*(10-len(details[3]))}|{details[4]+' '*(10-len(details[4]))}|')
                    total_price += int(details[3]) * int(details[-1])
            print('----------------------------------')
            print(f'              Total Price:{total_price}/-')
        else:
            print('No Products in the Cart!')

def admin_login():
    while True:
        print('1) ADD PRODUCT')
        print('2) UPDATE PRODUCT')
        print('3) REMOVE PRODUCT')
        print('4) VIEW ALL PRODUCTS')
        print('5) SEARCH PRODUCT')
        print('6) LOGOUT')
    
        choice = int(input('Enter your choice: '))
        admin = Admin()
        match choice:
            case 1: admin.add_product()
            case 2: admin.update_product()
            case 3: admin.remove_product()
            case 4: admin.view_all_products()
            case 5: admin.search_product()
            case 6: 
                print('Logged out successfully!')
                return
            case _: print('Invalid choice, Try again..!')

def user_login(user_id):
    while True:
        print('1) ADD PRODUCT TO THE CART')
        print('2) DECREASE QUANTITY')
        print('3) VIEW ALL PRODUCTS')
        print('4) VIEW CART')
        print('5) LOGOUT')

        cart = Cart(user_id)
        choice = int(input('Enter your choice: '))
        match choice:
            case 1: cart.add_product_to_cart()
            case 2: cart.decrease_quantity()
            case 3: cart.view_all_products()
            case 4: cart.view_cart()
            case 5:
                print('Logged out successfully!')
                return
            case _: print('Invalid choice, Try again..!')
    
print('<------ WELCOME TO THE ECOMMERCE WEBSITE ------>')

def home():
    while True:
        print('1) REGISTER')
        print('2) LOGIN')
        print('3) EXIT')
    
        choice = int(input('Enter your choice: '))
        match choice:
            case 1: Authentication().register()
            case 2: 
                    user_details= Authentication().login()
                    if user_details[1] == 'admin':
                        admin_login()
                    elif user_details[1] == 'user':
                        user_login(user_details[0])
            case 3: 
                print('THANK YOU, VISIT AGAIN!')
                break
            case _: print('Invalid choice, Try again..!')
home()



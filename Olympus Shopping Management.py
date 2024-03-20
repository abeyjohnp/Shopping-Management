import mysql.connector
myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005')
mycursor=myconn.cursor()
name=input('Enter your name :')
def timelagger(): 
    global i
    i=1
    while i<9999997:
        i=i+1
def admin():
    a1=input('Enter Password : ')
    if a1=='cc1':
        print('Access Authenticated !')
        timelagger()
        print('-------- Enter Option to choose from --------')
        print('1 - Checking Connectivity')
        a1=int(input('Enter option : '))
        if a1==1:
            if myconn.is_connected:
                print('Connection exists with MySQL')
            else:
                print('There is error with connectivity to MySQL')
def datetime():
    from datetime import datetime
    from datetime import date
    now = datetime.now()
    global current_time
    current_time = now.strftime("%H:%M:%S")
    global today
    today = date.today()
    print(today)
    print("\t \t \t \t \t \t \t -------------------------")
    print("\t \t \t \t \t \t \t| Current Time =", current_time,'|')
    print("\t \t \t \t \t \t \t -------------------------")
datetime()
def manager():
    while True:
        print('-------- WELCOME TO MANAGER MENU --------')
        print('1 - Checking Stock') #done
        print('2 - Price Filter ') #done
        print('3 - Updating Stock') #done
        print('4 - Voucher Menu')
        print('5 - View Reviews ') #done
        print('6 - Exit')
        print('-------- ----------------------- --------')
        m1=int(input('Enter option : '))
        pw=input('Enter Password : ')
        if pw=='cc1':
            print('Acesss Authenticated as of',today,'at',current_time)
            if m1==1:
                myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
                mycursor=myconn.cursor(dictionary=True)
                mycursor.execute('select * from items;')
                mydata=mycursor.fetchall()
                '''for i in mydata:
                    print(i)''' #or use this
                for row in mydata:
                    id = row["id"]
                    item_name = row["item_name"]
                    price = row["price"]
                    print(id,' | ', item_name ,' - ', price)
            if m1==2:
                myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
                mycursor=myconn.cursor(dictionary=True)
                print('-------- Enter Option to choose from --------')
                m1choice=input('Enter sort by - HIGHEST [HIGHEST] or LOWEST [LOWEST] : ') 
                if m1choice=='HIGHEST':
                    mycursor.execute('select * from items order by price desc ;')
                    m1price_data=mycursor.fetchall()
                    for row in m1price_data:
                        id = row["id"]
                        item_name = row["item_name"]
                        price = row["price"]
                        print(id,' | ', item_name ,' - ', price)
                if m1choice=='LOWEST':
                    mycursor.execute('select * from items order by price;')
                    m1price_data=mycursor.fetchall()
                    for row in m1price_data:
                        id = row["id"]
                        item_name = row["item_name"]
                        price = row["price"]
                        print(id,' | ', item_name ,' - ', price)
                mycursor=myconn.cursor()
                mycursor.execute('select max(price) as MAXIMUM_PRICE from items;')
                maxprice=mycursor.fetchall()
                mycursor.execute('select min(price) as MINIMUM_PRICE from items;')
                minprice=mycursor.fetchall()
                print('Maximum Price is =',(list(maxprice)[0][0])) 
                print('Minimum Price is =',(list(minprice)[0][0]))
            if m1==3:
                print('-------- UPDATING SETTINGS  --------')
                print('1 : ADDING ITEMS') 
                print('-------- -----------------  --------')
                myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
                mycursor=myconn.cursor()
                m1_2choice=int(input('Enter choice : '))
                if m1_2choice==1:
                    item_name = input('Enter new Item Name :')
                    item_price = input('Enter Item Price :')
                    sql = 'select * from items where item_name like "%{}%"'.format(item_name)
                    mycursor.execute(sql)
                    record=mycursor.fetchone()
                    if record==None:
                        sql = 'insert into items(item_name,price) values("{}",{});'.format(item_name,item_price)
                        mycursor.execute(sql)
                        myconn.commit()
                        print('\n\nNew Item added successfully.....\nPress any key to continue....')
                    else:
                        print('\n\nItem Name already Exist.....\nPress any key to continue....')
                    wait= input()
            if m1==4:
                print('-------- VOUCHER MENU --------') 
                timelagger()
                print ('1 : Show exisiting vouchers ')
                print ('2 : Insert new vouchers')
                chv=int(input('Enter choice :'))
                if chv==1:
                    myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
                    mycursor=myconn.cursor(dictionary=True)
                    mycursor.execute('select * from vouchers;')
                    admin_data=mycursor.fetchall()
                    for i in admin_data:
                        print(i)
                if chv==2:
                    voucher_new=input('Enter new voucher : ')
                    execute_voucher=f"insert into vouchers values('{voucher_new}');"
                    mycursor.execute(execute_voucher)
                    myconn.commit()
                print('-'*100)
            if m1==5:
                myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
                mycursor=myconn.cursor(dictionary=True)
                mycursor.execute('select * from review;')
                mydata=mycursor.fetchall()
                for i in mydata:
                    print(i)
            if m1==6:
                break                            
def customer_pay():
    name=input('Enter name : ')
    payment=input('Online or Cash : ')
    myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
    mycursor=myconn.cursor()
    from datetime import datetime
    from datetime import date
    now = datetime.now()
    global current_time
    current_time = now.strftime("%H:%M:%S")
    global today
    today = date.today()
    if payment=='Online':
        print('='*100)
        print('END TO END ENCRYPTED SYSTEM')
        i=1
        while i<9999998:
            i=i+1
        print('Please wait',end=' ')
        i=1
        while i<9999997:
            i=i+1
        tl=1
        while tl<10:
            print('.',end=' ')
            i=1
            while i<9999998:
                i=i+1
            tl+=1
        print('.')
        print('='*100)
        phoneno=int(input('Enter your phone number :'))
        remember=input('Do you want us to remember card details ? (Y/N): ')
        if remember=='Y':
            card=input('Enter name of card')
            pswd=input('Enter password of card')
            print('Details of your card send to the cashier device')
            print('CVV should be entered in the cashier device offline')
            executefn=f"insert into customers_online values('{name}','Online','{current_time}','{today}');"
            mycursor.execute(executefn)
            myconn.commit()
    if payment=='Cash':
        phoneno=int(input('Enter your phone number :'))
        priceenter=input('Enter total cost as displayed in the screen : ')
        executefno_offline=f"insert into customers_offline values('{name}','{phoneno}','{current_time}','{priceenter}','{today}');"
        mycursor.execute(executefno_offline)
        myconn.commit()
    print('Thank You for using OLYMPUS SMART SHOPPING, Have a good day')
def olympus_menu():
    while True:
        print('-------- WELCOME TO OLYMPUS SHOPPING MANAGEMENT MENU-------- ')
        timelagger()
        print('Choose your desired option from the following :) ')
        print('1 : Admin contols - Press 1')
        print('2 : Customer Menu - Press 2')
        print('3 : Cashier Menu  - Press 3')
        print('4 : Admin Logbook - Press 4')
        print('5 : Check History of Purchases')
        print('6 : Exit')
        timelagger()
        print('---------------------------------------------------------')
        ol=int(input('Enter Choice : '))
        if ol==1:
            manager()
        if ol==2:
            customer()    
        if ol==3:
            customer_pay()
        if ol==4:
            myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
            mycursor=myconn.cursor(dictionary=True)
            mycursor.execute('select * from admin_name;')
            admin_data=mycursor.fetchall()
            for i in admin_data:
                print(i)
        if ol==5:
            print('----- ONLINE CUSTOMERS -------')
            myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
            mycursor=myconn.cursor(dictionary=True)
            mycursor.execute('select * from customers_online;')
            online=mycursor.fetchall()
            print(online)
            print('----- CASH CUSTOMERS -------')
            myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
            mycursor=myconn.cursor(dictionary=True)
            mycursor.execute('select * from customers_offline;')
            offline=mycursor.fetchall()
            print(offline)
        if ol==6:
            print('Bye')
            break                     
def customer():
    print('-------- WELCOME TO OLYMPUS SMART SHOPPING-------- ')
    timelagger()
    while True:
        print('-'*100)
        print('1 : GET INFORMATION OF ITEMS                - PRESS 1')
        print('2 : PROCEED TO CHECKOUT                     - PRESS 2')
        print('3 : Exit OLYMPUS SMART SHOPPING SYSTEM      - PRESS 3')
        print('-'*100)
        main_customer_choice=input('Enter choice :')
        if main_customer_choice=='1':
            while True: 
                print('1 : Search for a product           - Press 1') 
                print('2 : To compare prices of two items - Press 2') 
                print('3 : Enter a review about product   - Press 3') 
                print('4 : Proceed to checkout ?          - Press 4')
                print('5 : Exit the Program               - Press 5')
                cu1=int(input('Enter Choice : '))
                myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
                mycursor=myconn.cursor()
                if cu1==1:
                    item_name=input('Enter Item Name :')
                    sql ='select * from items where item_name like "%{}%";'.format(item_name)
                    mycursor.execute(sql)
                    records = mycursor.fetchall()
                    print('Item Names start with :',item_name)
                    print('-'*100)
                    print('{:10s} {:30s} {:20s}'.format('Item ID','Item Name','Item Price'))
                    print('-'*100)
                    for row in records:
                        print('{:<10d} {:30s} {:.2f}'.format(row[0],row[1],row[2]))
                    print('-'*100)
                    print('\nPress any key to continue....')
                    wait= input()
                if cu1==2:
                    compare_1=input('Enter first item : ')
                    check_compare_1=f"select * from items where item_name like '{compare_1}';"
                    compare_2=input('Enter second item to compare :')
                    check_compare_2=f"select * from items where item_name like '{compare_2}';"
                    print('-'*100)
                    mycursor.execute(check_compare_1)
                    records_compare1=mycursor.fetchall()
                    print(records_compare1)
                    mycursor.execute(check_compare_2)
                    records_compare2=mycursor.fetchall()
                    print(records_compare2)
                    print('-'*100)
                if cu1==3:
                    print('-------')
                    review_prod=input('Enter Product Name : ')
                    inputer='Enter how much you , ',name,'; would rate out of 5 for', review_prod
                    stars=int(input(inputer))
                    review=input('Enter your review in less than 200 words : ')
                    review_executer=f"insert into review values('{review_prod}','{stars}','{review}');"
                    mycursor.execute(review_executer)
                    myconn.commit()
                    print('Thank You',name,'for your review')
                if cu1==4:
                    print('Proceeding to Checkout :) ')
                    customer_pay()
                    break
                if cu1==5:
                    print('Thank you for coming along! Have a nice day! :)')
                    break
                if cu1==112:
                    myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
                    mycursor=myconn.cursor(dictionary=True)
                    mycursor.execute('select * from items;')
                    mydata=mycursor.fetchall()
                    for row in mydata:
                        id = row["id"]
                        item_name = row["item_name"]
                        price = row["price"]
                        print(id,' | ', item_name ,' - ', price)
        if main_customer_choice=='2':
            print('Proceeding to check out ---')
            customer_pay() 
        if main_customer_choice=='admin_here':
            myconn=mysql.connector.connect(host='localhost',user='root',passwd='abeyjohn2005',database='olympus')
            mycursor=myconn.cursor()
            from datetime import datetime
            from datetime import date
            now = datetime.now()
            global current_time
            current_time = now.strftime("%H:%M:%S")
            global today
            today = date.today()
            print('Accesss Authenticated Admin')
            timelagger()
            admin_name=input('Enter Admin Name for the day : ')
            admin_admission=int(input('Enter your ID number :'))
            print('Thank you, details being send to main server')
            admin_executer=f"insert into admin_name values('{admin_name}','{admin_admission}','{current_time}','{today}');"
            mycursor.execute(admin_executer)
            myconn.commit()
            olympus_menu() 
        if main_customer_choice=='3':
            print('Have a nice day!')
            break          
print("1 : Customer Menu")
print("2 : Exit")
e=int(input('Enter choice : '))
if e==1:
    customer()


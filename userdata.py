import mysql.connector
import itertools
import secrets
import string

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sreeja@17',
    database="onlinerest"
)

mc = db.cursor() 
mc.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        ordertotal DECIMAL(10,2),
        paymentmethod VARCHAR(255),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
""")
db.commit()
mc.execute("""
    CREATE TABLE IF NOT EXISTS orderitems (
        orderitem_id INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        item_name VARCHAR(255),
        quantity INT,
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
    )
""")
db.commit()

def login(email, password):
    mc.execute(f"SELECT user_id, password FROM users WHERE email = '{email}'")
    details = mc.fetchall()
    try:
        user_id, passw = details[0]
        if passw == password:
            return True, user_id
        else:
            return False, None
    except:
        return False, None
  
def signup(email, name, address ,phnumber,sign_password):
    pz = ''
    mc.execute(f"INSERT INTO users (user_id,email, name, password, address, phonenumber) VALUES (DEFAULT, '{email}','{name}', '{sign_password}', '{address}', '{phnumber}')")
    # mc.execute(f"INSERT INTO USER (USER_ID, USER_NAME, PASSWORD) VALUES ('{id}', '{name}','{password}') ")
    db.commit()
    return True

def get_details(email):
    mc.execute(f"SELECT user_id, name, address, phonenumber, email FROM users WHERE email = '{email}'")
    details = mc.fetchall()
    return [details[0][0], details[0][1], details[0][2], details[0][3], details[0][4]]
    
def place_order(user_id, total_amt, paymentmethod ,food_list, qty_list):
    try :
        mc.execute(f"INSERT INTO orders( user_id, ordertotal, paymentmethod) VALUES ( '{user_id}', '{total_amt}', '{paymentmethod}') " )
        mc.execute("SELECT LAST_INSERT_ID()")
        order_idd= mc.fetchone()[0]
        
        for (food, qty) in zip(food_list, qty_list):
            mc.execute(f"INSERT INTO orderitems ( order_id, item_name, quantity ) VALUES ('{order_idd}', '{food}', '{qty}')")
        db.commit()
        return True
    except:
        return False
    
def get_user_data():
    mc.execute("SELECT user_id, email, name, address, phonenumber FROM users")
    details = mc.fetchall() 
    detail_dict = {'User Id': [i[0] for i in details ],
                   'Email Id' : [i[1] for i in details],
                   'Name' :[i[2] for i in details],
                   'Address':[i[3] for i in details],
                   'Phone Number' : [i[4] for i in details]}
    return detail_dict

    
def get_order_data():
    mc.execute("SELECT * FROM orders")
    details = mc.fetchall()
    details_dict = {'Order Id':[i[0] for i in details],
                  'User Id': [i[1] for i in details],
                  'Total Amount' :[i[2] for i in details],
                  'Payment Method':[i[3] for i in details]}
    return details_dict

def get_orderitem_data():
    mc.execute("SELECT * FROM orderitems")
    details = mc.fetchall()
    details_dict = {'order_id' : [i[0] for i in details],
                    'Food Item' : [i[1] for i in details],
                    'QTY':[i[2] for i in details]}
    return details_dict

def update_details(user_id, email, name ,address, number):
    mc.execute(f"UPDATE users SET email = '{email}', name ='{name}', address ='{address}', phonenumber = '{number}' WHERE user_id ={user_id} ")
    db.commit()
    return True

def update_password(user_id, password):
    mc.execute(f"UPDATE users SET password ='{password}' WHERE user_id={user_id} ")
    db.commit()
    return True

def get_orderitem_detail(order_id):
    mc.execute(f"SELECT * FROM orderitems WHERE order_id = '{order_id}'")
    details = mc.fetchall()
    detail_dict = {'order_id' : [i[0] for i in details],
                    'Food Item' : [i[1] for i in details],
                    'QTY':[i[2] for i in details]}
    return detail_dict

def delete_user(user_id):
    try:
        # Start a transaction
        db.start_transaction()

        # Delete from orderitems table
        mc.execute(f"DELETE FROM orderitems WHERE order_id IN (SELECT order_id FROM orders WHERE user_id = {user_id})")

        # Delete from orders table
        mc.execute(f"DELETE FROM orders WHERE user_id = {user_id}")

        # Delete from users table
        mc.execute(f"DELETE FROM users WHERE user_id = {user_id}")

        # Commit the transaction
        db.commit()
        
        return True
    except Exception as e:
        # Rollback the transaction in case of an error
        db.rollback()
        print(f"Error: {e}")
        return False
    finally:
        # Reset FOREIGN_KEY_CHECKS to 1
        mc.execute("SET FOREIGN_KEY_CHECKS=1")

from tkinter import Image
import streamlit as st
from admin_login import user_data_table 
from userdata import get_order_data, login, signup, get_details, update_details, update_password, delete_user
import pandas as pd 
import time 
from PIL import Image

st.set_page_config(
    page_title="Online Food Ordering System",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
    }
)
st.markdown(
    """
    <h1 style=' font-family: sans-serif;'>Welcome to my Streamlit Application!!😋</h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style=' font-family: sans-serif;'>🎉🍔Online Food Ordering System🍔🎉</h1>
    """,
    unsafe_allow_html=True
)
img = Image.open("main2.jpg")
st.image(img,width=600)

st.subheader(":green[About this Application:✨]")
st.write('''***An online food ordering app is a software application that allows users to browse through a menu of various food items offered by local restaurants or food establishments, select their preferred dishes, and place orders for delivery or pickup. These apps have become increasingly popular, especially in recent years, due to their convenience and ease of use.***''')

# st.title("")
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
checkoutSection = st.container()

food_list=[None, None, None ,None,None,None,None,None,None]
qty_list=[None, None, None,None,None ,None,None,None,None]
amt_list=[None, None, None,None,None,None,None,None,None]

order = {
    'Food Name':food_list,
    'Qty' : qty_list,
    'Amount':amt_list
}

cart = pd.DataFrame(order)
# List of available food items
available_food_items = ["Pizza", "Burger", "Noodles", "Hotdog", "Sandwich","Biriyani","fried-rice","tandoori","soft-drinks"]

st.sidebar.title("Our Online Food Ordering App🍔")
st.sidebar.write("***A short clip:***")

video_file = open('app.mp4', 'rb')
video_bytes = video_file.read()
st.sidebar.video(video_bytes)

st.sidebar.title(":green[Feedback]")

feedback = st.sidebar.text_area("Leave your feedback here:")

if st.sidebar.button(":blue[Submit Feedback]"):
    st.sidebar.success("Thank you for your feedback!")

st.sidebar.title(":green[Rate This]")

rating = st.sidebar.slider("Rate from 1 to 5", 1, 5)

st.sidebar.write(f"You rated this {rating} out of 5.")

st.sidebar.subheader("Contact Information")
st.sidebar.write("Email: support@example.com")
st.sidebar.write("Phone: +123-456-7890")

st.sidebar.subheader("Support")
st.sidebar.write("[Support Page](https://example.com/support)")

def show_checkout_page():
    with checkoutSection:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        st.success(f"Hey {st.session_state['details'][1]}, Your Order has been placed Successfully")
        st.balloons()
        st.subheader(f"Your Order will arrive to your address = {st.session_state['details'][2]}")
        st.subheader(f"and our rider will contact you on = {st.session_state['details'][3]}")
        
def update_user_details(user_id, email, name ,address, number):
    if update_details(user_id, email, name ,address, number):
        st.info("User Information Updated Successfully, you will be logged out now")
        LoggedOut_Clicked()
    else:
        st.info("Error Detected while updating")

def update_user_password(user_id, password):
    if update_password(user_id, password):
        st.info("Password updated successfully, you will be logged out now")
        LoggedOut_Clicked()
    else:
        st.info("Eroor Detected while updating password")
    
def show_main_page():
    with mainSection:
        
        st.header(f" Welcome {st.session_state['details'][1]}")
        
        menu, cart, myaccount= st.tabs([':green[Menu]', ':green[Cart]', ':green[My Account]'])

        with menu:
            st.subheader('select the food you want to order') 
            search_item = st.text_input("Search for a food item:")

            # Check if the entered item is in the available food items
            if search_item:
                item_lower = search_item.lower()
                if item_lower in [item.lower() for item in available_food_items]:
                    st.success(f"{search_item} is available. You can order it!")
                    for i, food_item in enumerate(available_food_items):
                        if item_lower == food_item.lower():
                            st.image(f'{food_item.lower()}.jpg',width=200)
                            st.text(f"{food_item} {'🍕' if food_item != 'Biriyani' else '🍚'}")

                            if food_item == "Biriyani":
                                st.write('Order Biriyani @ ₹250')
                                st.write("Please specify the quantity:")
                                c_biriyani = st.number_input(label="", min_value=1, key=99)
                                food_list[i] = food_item
                                qty_list[i] = int(c_biriyani)
                                amt_list[i] = int(c_biriyani) * 250  
            
            # Display the food item and allow ordering
                    if search_item.lower() == "pizza":
                        st.write("pizza is available")
                        
                # Display and order pizza
                    elif search_item.lower() == "burger":
                        st.write("pizza is available")

                # Display and order burger
                    elif search_item.lower() == "noodles":
                        st.write("pizza is available")
                # Display and order noodles
                    elif search_item.lower() == "hotdog":
                        st.write("pizza is available")
                # Display and order hotdog
                    elif search_item.lower() == "sandwich":
                        st.write("pizza is available")
                # Display and order sandwich
                else:
                    st.error(f"{search_item} is currently out of stock. Please select another food item.")
            
            col1, col2, col3,col4,col5,col6,col7,col8 = st.columns(8)
            col1.image('pizza.jpg')
            col1.text("Pizza 🍕")
            if col1.checkbox(label ='Order Pizza @ ₹199',key =1):
                col1.text('Enter QTY. -')
                c_pizza = col1.number_input(label="", min_value=1, key = 79)
                food_list[0] = 'pizza'
                qty_list[0] = int(c_pizza)
                amt_list[0] = int(c_pizza)*199
                      
            col2.image('burger.jpg')
            col2.text("Burger 🍔")
            if col2.checkbox('Order Buger @ ₹99',key =2):
                col2.text('Enter QTY. -')
                c_burger = col2.number_input(label="", min_value=1, key = 89)
                
                food_list[1] = 'burger'
                qty_list[1] = int(c_burger)
                amt_list[1] = int(c_burger)*99             
                       
            col3.image('noodles.jpg')
            col3.text("Noodles 🍜")
            if col3.checkbox('Order noodles @ ₹149',key =3):
                col3.text('Enter QTY. -')
                c_noodles = col3.number_input(label="", min_value=1, key = 69)
                food_list[2] = 'noodles'
                qty_list[2] = int(c_noodles)
                amt_list[2] = int(c_noodles)*149 
                         
            col4.image('hotdog.jpg')
            col4.text("Hotdog 🌭")
            if col4.checkbox('Order hotdog @ ₹99', key=4):
                col4.text('Enter QTY. -')
                c_hotdog = col4.number_input(label="", min_value=1, key=70)
                food_list[3] = 'hotdog'
                qty_list[3] = int(c_hotdog)
                amt_list[3] = int(c_hotdog) * 99


            col5.image('sandwitch.jpg')
            col5.text("Sandwitch 🥪")
            if col5.checkbox('Order sandwich @ ₹129', key=5):
                col5.text('Enter QTY. -')
                c_sandwich = col5.number_input(label="", min_value=1, key=71)
                food_list[4] = 'sandwich'
                qty_list[4] = int(c_sandwich)
                amt_list[4] = int(c_sandwich) * 129


            col6.image('fried-rice.jpg')
            col6.text("fried-rice")
            if col6.checkbox('Order fried-rice @ ₹100', key=6):
                col6.text('Enter QTY. -')
                c_friedrice = col6.number_input(label="", min_value=1, key=72)
                food_list[5] = 'sandwich'
                qty_list[5] = int(c_friedrice)
                amt_list[5] = int(c_friedrice) * 100

            col7.image('tandoori.jpg')
            col7.text("tandoori")
            if col7.checkbox('Order tandoori @ ₹170', key=7):
                col7.text('Enter QTY. -')
                c_tandoori = col7.number_input(label="", min_value=1, key=73)
                food_list[6] = 'sandwich'
                qty_list[6] = int(c_tandoori)
                amt_list[6] = int(c_tandoori) * 170

            col8.image('soft-drinks.jpg')
            col8.text("soft-drinks")
            if col8.checkbox('Order soft-drinks @ ₹50', key=8):
                col8.text('Enter QTY. -')
                c_softdrinks = col8.number_input(label="", min_value=1, key=74)
                food_list[7] = 'sandwich'
                qty_list[7] = int(c_softdrinks)
                amt_list[7] = int(c_softdrinks) * 50
 
            with cart:
                hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                 """
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                
                order = {
                        'Food Name':food_list,
                        'Qty' : qty_list,
                        'Amount':amt_list
                    }
                
                cart = pd.DataFrame(order)
                cart_final = cart.dropna()
                cart_final['Qty'].astype(int)
                st.table(cart_final)
                total_amt = [ amt for amt in amt_list if amt!=None]
                total_item = [food for food in food_list if food !=None]
                total_qty = [qty for qty in qty_list if qty!=None]
                total_sum = sum(total_amt)
                st.subheader(":green[Your Total Amout to be paid]" + ' --  Rs.'+ str(total_sum) )

                st.header("Payment Information")
                payment_mode = st.selectbox(":green[Select Payment Mode]", ["UPI", "Credit Card", "Debit Card", "Cash on Delivery"])

                if payment_mode in ["Credit Card", "Debit Card"]:
                    st.subheader(":green[Card Information]")
                    card_number = st.text_input(":green[Card Number]", "")
                    card_holder_name = st.text_input(":green[Card Holder Name]", "")
                    expiration_date = st.text_input(":green[Expiration Date (MM/YY)]", "")
                    cvc_number = st.text_input(":green[CVC Number]", "")

                if payment_mode == "UPI":
                    st.subheader(":green[UPI Information]")
                    upi_id = st.text_input(":green[UPI ID]", "")
                    bank_account = st.selectbox(":green[Select Bank Account]", ["PNB", "SBI", "HDFC", "Axis"])
                    upi_pin = st.text_input(":green[UPI PIN]", type="password")

                st.header(":blue[Delivery Information]")
                delivery_address = st.text_input(":green[Enter Delivery Address]", "")
                delivery_pincode = st.text_input(":green[Enter Pincode]", "")

                if st.button(":red[Place Your Order]"):
        
                    if payment_mode == "Credit Card" and (not card_number or not card_holder_name or not expiration_date or not cvc_number):
                        st.error("Please fill in all credit card details.")
                    elif payment_mode == "Debit Card" and (not card_number or not card_holder_name or not expiration_date or not cvc_number):
                        st.error("Please fill in all debit card details.")
                    elif payment_mode == "UPI" and (not upi_id or not bank_account or not upi_pin):
                        st.error("Please fill in all UPI details.")
                    elif not delivery_address or not delivery_pincode:
                        st.error("Please fill in delivery address and pincode.")
                    elif payment_mode == "UPI" and (len(upi_pin) != 6 or not upi_pin.isdigit()):
                        st.error("UPI PIN must be a 6-digit number.")
                    else:
                        total_cost = 0
                        order_details = []
                        st.success("Order Placed Successfully!!!")
                        st.header("Payment Information")
                        st.write(f":blue[Payment Mode: ]{payment_mode}")
                        if payment_mode in ["Credit Card", "Debit Card"]:
                            st.write("Card Information:")
                            st.write(f":blue[Card Number: ]{card_number}")
                            st.write(f":blue[Card Holder Name: {card_holder_name}]")
                            st.write(f":blue[Expiration Date: ]{expiration_date}")
                        if payment_mode == "UPI":
                            st.write("UPI Information:")
                            st.write(f":blue[UPI ID:] {upi_id}")
                            st.write(f":blue[Bank Account: ]{bank_account}")
                            st.write(":blue[UPI PIN:] **** (hidden for privacy)")

                        st.header("Delivery Information")
                        st.write(f":blue[Delivery Address: ]{delivery_address}")
                        st.write(f":blue[Pincode:] {delivery_pincode}")
                
            with myaccount:
                st.header('Update your details here')
                st.subheader("Enter updated email")
                up_email = st.text_input(label="", value = str(st.session_state['details'][4]))
                st.subheader("Enter updated name")
                up_name = st.text_input(label="", value=str(st.session_state['details'][1]))
                st.subheader("Enter updated address")
                up_address = st.text_input(label="", value=str(st.session_state['details'][2]))
                st.subheader("Enter updated phone number")
                up_number = st.text_input(label="", value=str(st.session_state['details'][3]))
                
                st.button('Update User Details', on_click = update_user_details , args=(st.session_state['details'][0], up_email, up_name, up_address, up_number))

                if st.checkbox(":red[Do you want to change the password ?]"):
                    st.subheader('Write Updated Password :')
                    up_passw =st.text_input (label="", value="",placeholder="Enter updated password", type="password", key = 256)
                    up_conf_passw = st.text_input (label="", value="",placeholder="Enter updated password", type="password", key =257)
                    if up_passw == up_conf_passw:
                        st.button(':red[Update Password]', on_click=update_user_password, args=(st.session_state['details'][0], up_passw))
                        # st.success("Password Matched!!")
                    else :
                        st.info('Password does not match ')
                        
                if st.checkbox(":red[Do you want to Delete your account ? ]"):
                    st.subheader(":red[Are you sure you want to delete your account ?]")
                    st.text(st.session_state['details'][0])
                    st.button(':red[DELETE MY ACCOUNT]', on_click = delete_user_show, args =(st.session_state['details'][0],))

                if(st.button("CANCEL ORDER")):
                    
                    st.success("order cancelled successfully!")                
        
def delete_user_show(urd_id):
    delete_user(urd_id)
    LoggedOut_Clicked()
    st.success("Account Deleted Successfuly")

def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    st.session_state['details'] = None
    st.session_state['checkout'] = False
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
        

def LoggedIn_Clicked(email_id, password):
    if login(email_id, password):
        st.session_state['loggedIn'] = True
        st.session_state['details'] = get_details(email_id)
        st.balloons()
    else:
        st.session_state['loggedIn'] = False;
        st.session_state['details'] = None
        st.error("Invalid user name or password")
        

def validate_email(email):
    if not email.endswith('@gmail.com'):
        return False
    return True

def signup_clicked(email, name, address ,phnumber,sign_password):
    try :
        if signup(email, name, address ,phnumber,sign_password):
            st.success("Signup successful ")
            st.balloons()
    except:
        st.warning('Invalid User ID or user ID already taken')

        
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            
            login, signup= st.tabs([":green[Login]", ":green[Signup to Create Account]"])
            with login:
                st.subheader('Login Here 🎉')         
                email_id = st.text_input (label="", value="", placeholder="Enter your Email")
                password = st.text_input (label="", value="",placeholder="Enter password", type="password")
                st.button (":green[Login]", on_click=LoggedIn_Clicked, args= (email_id, password))
                
            with signup:
                st.subheader('Signup 🫶')
                email = st.text_input(label="", value="", placeholder="Enter your Email-ID", key=10)
                name = st.text_input(label="", value="", placeholder="Enter your Name", key=9)
                address = st.text_input(label="", value="", placeholder="Enter your Address:", key=13)
                phnumber = st.text_input(label="", value="", placeholder='Enter your Phone Number', key=14)
                sign_password = st.text_input(label="", value="", placeholder="Enter password", type="password", key=11)
                cnf_password = st.text_input(label="", value="", placeholder="Confirm your password", type="password", key=12)

                if st.button(":green[Sign UP]"):
                    if not (email and name and address and phnumber and sign_password and cnf_password):
                        st.warning("Please fill in all the details.")
                    elif not validate_email(email):
                        st.warning("Invalid email. Please use a valid Gmail address.")
                    # elif not validate_phone_number(phnumber[3:]):  # Extracting digits from phone number
                    #     st.warning("Invalid phone number. Please enter a 10-digit number.")
                    elif sign_password != cnf_password:
                        st.warning('Password does not match')
                    else:
                        signup_clicked(email, name, address, phnumber, sign_password)

            st.write("Note: User can't proceed without filling all the details properly.")

with headerSection:
    # st.title("Online Food Ordering System 😋")
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    if 'checkout' not in st.session_state:
        st.session_state['checkout'] = False
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()
        elif st.session_state['checkout']:
            show_logout_page()
            show_checkout_page()
        else:
            show_login_page()

            
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Add admin credentials
admin_username = "admin"
admin_password = "adminpassword"

# Function to check admin login
def admin_login(username, password):
    return username == admin_username and password == admin_password

# Admin tabs
users_tab, orders_tab = st.tabs(["Users", "Orders"])

# Check if admin is logged in
if st.session_state.get('admin_logged_in', False):
    if users_tab:
        # Display user details in the "Users" tab
        users_data = user_data_table()  # Assuming you have a function to get user data
        st.table(users_data)
    elif orders_tab:
        # Display order details in the "Orders" tab
        order_data = get_order_data()  # Assuming you have a function to get order data
        st.table(order_data)
    # Add logout button for admin
    if st.button("Admin Logout"):
        st.session_state['admin_logged_in'] = False
else:
    # Admin login section
    admin_login_section = st.expander("Admin Login")
    with admin_login_section:
        admin_username_input = st.text_input("Admin Username:")
        admin_password_input = st.text_input("Admin Password:", type="password")
        if st.button("Admin Login"):
            if admin_login(admin_username_input, admin_password_input):
                st.session_state['admin_logged_in'] = True
            else:
                st.error("Invalid admin credentials")


















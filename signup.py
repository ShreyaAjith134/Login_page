from PIL import Image, ImageTk
import mysql.connector
import tkinter as tk
import tkinter.messagebox

root= tk.Tk()
root.state('zoomed')
root.title("Login")
name_var=tk.StringVar()
passw_var=tk.StringVar()
newname_var=tk.StringVar()
newpassw_var=tk.StringVar()
def page_bg(bg_location):
    #Open image using Image module
    img = Image.open(bg_location)
    test = ImageTk.PhotoImage(img)
    

    #Resize the Image using resize method
    resized_image = img.resize((root.winfo_screenwidth(),root.winfo_screenheight()), Image.LANCZOS)
    new_image = ImageTk.PhotoImage(resized_image)
    label1 = tkinter.Label(image=new_image)
    label1.image = new_image

    # Position image
    label1.place(x=0, y=0)

def signup():
    name = newname_var.get()
    passw = newpassw_var.get()
    
    try:
        # Establishing the connection
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MySQL1234",
            database="login"
        )
        mycursor = mydb.cursor()

        # Check if the user already exists
        mycursor.execute("SELECT * FROM existing_users WHERE username = %s", (name,))
        result = mycursor.fetchone()
        
        if result:
            tk.messagebox.showerror("Error", "Username already exists!")
        else:
            # Insert new user
            mycursor.execute("INSERT INTO existing_users VALUES('{}','{}')".format(name, passw))
            mydb.commit()
            tk.messagebox.showinfo("Success", "User registered successfully!")

    except mysql.connector.errors.IntegrityError as err:
        tk.messagebox.showerror("Error", "An error occurred: {}".format(err))

    finally:
        mycursor.close()
        mydb.close()

    
def signup_page():

    page_bg("D:\\Shreya\\GitHub\\Login_page\\bg.jpg")
    # declaring string variable for storing name and password
            
    # creating a label for name using widget Label
    name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold')).place(x=500, y=200)

    # creating a entry for input name using widget Entry
    name_entry = tk.Entry(root,textvariable = newname_var, font=('calibre',10,'normal')).place(x=600, y=200)

    # creating a label for password
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold')).place(x=500, y=300)

    # creating a entry for password
    passw_entry=tk.Entry(root, textvariable = newpassw_var, font = ('calibre',10,'normal'), show = '*').place(x=600, y=300)

    # creating a signup button using the widget 
    # Button that will call the signup function 
    signup_btn=tk.Button(root,text = 'Sign up', height = 1, width = 17, command = signup)
    signup_btn.place(x=350, y=500)
    signup_btn.config(font=('Bahnschrift Light SemiCondensed',15))

    backtologin_btn=tk.Button(root,text = 'Back to Login', height = 1, width = 17, command = login_page)
    backtologin_btn.place(x=750, y=500)
    backtologin_btn.config(font=('Bahnschrift Light SemiCondensed',15))    


def loggedin_page():
    page_bg("D:\\Shreya\\GitHub\\Login_page\\bg.jpg")
    name_label = tk.Label(root, text = 'YOU HAVE LOGGED IN!!!', font=('calibre',15, 'bold')).place(x=550, y=250)


# defining a function that will get the name and password and print them on the screen
def login():
    con = mysql.connector.connect(user='root', password='MySQL1234', host='127.0.0.1', database='login')
    mycursor = con.cursor()
    mycursor.execute("Select * from existing_users;")
    ans = mycursor.fetchall()
    for i in ans:
        if i[0]==name_var.get() and i[1]==passw_var.get():
            loggedin_page()
        else:
            tk.messagebox.showerror("Error", "Incorrect Username or Password!")
	
def login_page():
    page_bg("D:\\Shreya\\GitHub\\Login_page\\bg.jpg")
    # creating a label for name using widget Label
    name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold')).place(x=500, y=200)

    # creating a entry for input name using widget Entry
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal')).place(x=600, y=200)

    # creating a label for password
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold')).place(x=500, y=300)

    # creating a entry for password
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*').place(x=600, y=300)

    # creating a login button using the widget Button that will call the login function 
    login_btn=tk.Button(root,text = 'Login', height = 1, width = 17, command = login)
    login_btn.place(x=350, y=500)
    login_btn.config(font=('Bahnschrift Light SemiCondensed',15))

    # creating a signup button using the widget Button that will call the signup function 
    signupnow_btn=tk.Button(root,text = 'Sign up Now', height = 1, width = 17, command=signup_page)
    signupnow_btn.place(x=750, y=500)
    signupnow_btn.config(font=('Bahnschrift Light SemiCondensed',15))

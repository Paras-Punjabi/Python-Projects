from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview,Style
from pymongo import *
from Todos import Todo

class App():
    def __init__(self):
        '''
        DataBase: TodoApp-Tkinter
        Collections: users,todos
        '''

        self.root = Tk()
        self.root.geometry("1200x600")    
        self.root.title("Todo App")

        self.starting_frame = Frame(self.root)
        self.signIn_frame = Frame(self.root)
        self.login_frame = Frame(self.root)
        self.error_frame = Frame(self.root)

        self.user_home_page_frame = Frame(self.root)
        self.all_todo_frame = Frame(self.root)
        self.update_todo_frame = Frame(self.root)
        self.menubar = Menu(self.root)

        self.db = None
        self.collection = None
        self.client = None

        self.startingPage()
        self.root.mainloop()

    def connectToDataBase(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017")
            self.db = self.client["TodoApp-Tkinter"]

        except Exception as e:
            self.errorPage(message="Cannot Connect to Database")
    
    def deleteAccount(self,identity):
        response = messagebox.askyesno(title="Delete Account",message="Are you sure you want to delete your account?")
        if response:
            try:
                self.collection = self.db["todos"]
                self.collection.delete_many({"identity":identity})

                self.collection = self.db["users"]
                self.collection.delete_one({"email":identity})
                messagebox.showinfo(title="Success",message="Your Account is permanently deleted")
                self.startingPage()
            except Exception as e:
                self.errorPage("Server Error")
    
    def logout(self):
        self.startingPage()
    
    def createMenuBar(self,identity):
        self.menubar = Menu(self.root)
        home = Menu(self.menubar,tearoff=False)
        about = Menu(self.menubar,tearoff=False)

        self.menubar.add_cascade(label="Home",menu=home)
        self.menubar.add_cascade(label="About",menu=about)
        
        home.add_cascade(label="New",command=lambda:self.userHomePage(identity))
        home.add_cascade(label="View All",command=lambda:self.showAllTodos(identity))
        home.add_separator()
        home.add_cascade(label="Logout",command=lambda:self.logout())
        home.add_cascade(label="Delete Account",command=lambda:self.deleteAccount(identity))
        home.add_separator()
        home.add_cascade(label="Exit",command=self.root.destroy)

        about.add_cascade(label="About",command=lambda:messagebox.askokcancel(title="About",message="This is a Todo's App made by Paras Punjabi"))

        self.root.config(menu=self.menubar)
    
    def addTodo(self,title,data,identity):
        todo = Todo(title,data,identity)
        try:
            self.collection = self.db["todos"]
            self.collection.insert_one(todo.toDict())
            self.showAllTodos(identity)
        except Exception as e:
            self.errorPage("Server Error")
    
    def fetchAllTodo(self,identity):
        try:
            self.collection = self.db["todos"]
            array = list(self.collection.find({"identity":identity}))
            return array
        except Exception as e:
            self.errorPage("Server Error")
            return None
    
    def deleteTodo(self,table,array):
        try:
            index = table.focus()
            if index == "":
               return
            obj = array[int(index)]
            self.collection= self.db["todos"]
            self.collection.find_one_and_delete(obj)
            self.showAllTodos(obj["identity"])
        except Exception as e:
            self.errorPage("Server Error")

    def updateTodo(self,obj,newTitle,newData):
        try:
            self.collection = self.db["todos"]
            self.collection.find_one_and_update({"_id":obj["_id"]},{"$set":{"title":newTitle,"data":newData}})
            self.showAllTodos(obj["identity"])
        except Exception as e:
            self.errorPage("Server Error")

    def showAllTodos(self,identity):
        self.all_todo_frame.destroy()
        self.all_todo_frame = Frame(self.root)
        self.user_home_page_frame.pack_forget()
        self.update_todo_frame.pack_forget()
        Label(self.all_todo_frame,text="All Todos".upper(),font=("monospace",20,"bold")).pack(side="top",pady=20)

        array = self.fetchAllTodo(identity)

        if(len(array) == 0):
            Label(self.all_todo_frame,text="No Todos".upper(),font=("monospace",20,"bold")).pack(side="top",pady=20)
            self.all_todo_frame.pack()
            return
        
        table = Treeview(self.all_todo_frame,style="mystyle.Treeview",selectmode="extended",height=20)
        table['columns'] = ("Index","Title","Description","Date")

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('monospace', 13))
        style.configure("mystyle.Treeview.Heading", font=('monospace', 15,'bold'))
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        table.column("#0", width=0,stretch=NO)
        table.column("Index",anchor=CENTER,width=100)
        table.column("Title",anchor=CENTER,width=200)
        table.column("Description",anchor=CENTER,width=700)
        table.column("Date",anchor=CENTER,width=100)

        table.heading("#0",text="",anchor=CENTER)
        table.heading("Index",text="Index",anchor=CENTER)
        table.heading("Title",text="Title",anchor=CENTER)
        table.heading("Description",text="Description",anchor=CENTER)
        table.heading("Date",text="Date",anchor=CENTER)

        for index,items in enumerate(array):
            table.insert(parent="",index="end",text="",iid=index,values=(str(index+1),items["title"],items["data"],items["date"]),open=True)

        scroll = Scrollbar(self.all_todo_frame)
        scroll.pack(side="right",fill=Y)
        scroll.config(command=table.yview)

        table.pack()
        Button(self.all_todo_frame,text="Delete",font=("monospace",15,"bold"),command=lambda:self.deleteTodo(table,array)).pack(side="left",padx=100,pady=20)
        Button(self.all_todo_frame,text="Update",font=("monospace",15,"bold"),command=lambda:self.updateTodoPage(table,array)).pack(side="right",padx=100,pady=20)
        self.all_todo_frame.pack()
    
    def updateTodoPage(self,table,array):
        index = table.focus()
        if index == "":
            return
        obj = array[int(index)]
        self.all_todo_frame.pack_forget()

        self.createMenuBar(obj["identity"])
        Label(self.update_todo_frame,text=f"Update Todo",font=("monospace",20,"bold")).grid(row=1,column=2)

        title = StringVar()
        data = StringVar()
        title.set(obj["title"])
        data.set(obj["data"])

        Label(self.update_todo_frame,text="Title",font=("monospace",20,"bold")).grid(row=2,column=1,padx=10,pady=20)
        titleInput = Entry(self.update_todo_frame,textvariable=title,width=30,font=("monospace",20,"bold"))
        titleInput.grid(row=2,column=2,padx=10,pady=20)

        Label(self.update_todo_frame,text="Description",font=("monospace",20,"bold")).grid(row=3,column=1,padx=10,pady=20)
        titleInput = Entry(self.update_todo_frame,textvariable=data,width=30,font=("monospace",20,"bold"))
        titleInput.grid(row=3,column=2,padx=10,pady=20)

        Button(self.update_todo_frame,font=("monospace",20,"bold"),text="Update",command=lambda:self.updateTodo(obj,title.get(),data.get())).grid(row=4,column=2,pady=20,padx=10)

        self.update_todo_frame.pack()

    def userHomePage(self,identity):
        self.signIn_frame.pack_forget()
        self.user_home_page_frame.pack_forget()
        self.all_todo_frame.pack_forget()
        self.update_todo_frame.pack_forget()
        self.error_frame.pack_forget()

        self.createMenuBar(identity)
        self.collection = self.db["users"]
        dataObj = self.collection.find_one({"email":identity})
        self.root.title("Home - " + dataObj["username"])
        Label(self.user_home_page_frame,text=f"Welcome {dataObj['username']}",font=("monospace",20,"bold")).grid(row=1,column=2)

        title = StringVar()
        data = StringVar()

        Label(self.user_home_page_frame,text="Title",font=("monospace",20,"bold")).grid(row=2,column=1,padx=10,pady=20)
        titleInput = Entry(self.user_home_page_frame,textvariable=title,width=30,font=("monospace",20,"bold"))
        titleInput.grid(row=2,column=2,padx=10,pady=20)

        Label(self.user_home_page_frame,text="Description",font=("monospace",20,"bold")).grid(row=3,column=1,padx=10,pady=20)
        titleInput = Entry(self.user_home_page_frame,textvariable=data,width=30,font=("monospace",20,"bold"))
        titleInput.grid(row=3,column=2,padx=10,pady=20)

        Button(self.user_home_page_frame,font=("monospace",20,"bold"),text="Add Todo",command=lambda:f"{self.addTodo(title.get(),data.get(),identity)} {data.set('')} {title.set('')}").grid(row=4,column=2,pady=20,padx=10)

        Button(self.user_home_page_frame,font=("monospace",20,"bold"),text="Reset",command=lambda:f"{data.set('')} {title.set('')}").grid(row=4,column=1,pady=20,padx=10)

        self.user_home_page_frame.pack()

    def loginUser(self,dict):
        try:
            self.connectToDataBase()
            if(dict["email"] == "" or dict["password"] == ""):
                messagebox.showwarning(title="Warning",message="Fill all entries")
            else:
                self.collection = self.db["users"]
                data = self.collection.find_one(dict)
                if(data):
                    self.userHomePage(identity=dict["email"])
                else:
                    messagebox.showerror(title="Error",message="You are not authorized!")
                    self.startingPage()
        except Exception as e:
            self.errorPage("Cannot Connect to Database")
        
    def signInUser(self,dict):
        self.connectToDataBase()
        try:
            if dict["email"] == "" or dict["password"] == "" or dict["username"] =="":
                messagebox.showwarning(title="Warning",message="Fill all entries")
            else:
                self.collection = self.db["users"]

                if(self.collection.find_one({"email":dict["email"]})):
                    messagebox.showwarning(title="Warning",message="Try to fill with different entries")
                    self.signInPage()

                else:
                    self.collection.insert_one(dict)
                    messagebox.askokcancel(title="Login Form",message="You are successfully loged in. Try signing in to add your todos")

                    self.startingPage()
        except Exception as e:
            self.errorPage("Cannot perform Login")
    
    def loginPage(self):
        self.starting_frame.pack_forget()
        self.login_frame.pack_forget()
        self.error_frame.pack_forget()

        if(self.client):
            self.client.close()
            self.client = None

        email = StringVar()
        password = StringVar()
        self.root.title("Login Form")

        Label(self.signIn_frame,text="Login",font=("monospace",20,"bold")).grid(column=2,row=0,pady=10)

        Label(self.signIn_frame,text="Email",font=("monospace",20,"bold")).grid(column=1,row=1,pady=10,padx=5)
        emailInput = Entry(self.signIn_frame,textvariable=email,font=("monospace",20,"bold"),width=30)
        emailInput.grid(row=1,column=2,pady=10,padx=5)

        Label(self.signIn_frame,text="Password",font=("monospace",20,"bold")).grid(column=1,row=2,padx=5,pady=10)
        emailInput = Entry(self.signIn_frame,textvariable=password,show="*",font=("monospace",20,"bold"),width=30)
        emailInput.grid(row=2,column=2,padx=5,pady=10)

        Button(self.signIn_frame,text="Home",font=("monospace",20,"bold"),command=self.startingPage).grid(row=3,column=1,pady=20,padx=5)

        Button(self.signIn_frame,text="Submit",font=("monospace",20,"bold"),command=lambda:self.loginUser({"email":email.get(),"password":password.get()})).grid(row=3,column=2,pady=20,padx=5)
        self.signIn_frame.pack()

    def signInPage(self):
        self.starting_frame.pack_forget()
        self.signIn_frame.pack_forget()
        self.error_frame.pack_forget()

        if(self.client):
            self.client.close()
            self.client = None

        email = StringVar()
        password = StringVar()
        name = StringVar()
        self.root.title("Sign In Form")

        Label(self.login_frame,text="Sign In",font=("monospace",20,"bold")).grid(column=2,row=0,pady=10)

        Label(self.login_frame,text="Username",font=("monospace",20,"bold")).grid(column=1,row=1,pady=10,padx=5)
        nameInput = Entry(self.login_frame,textvariable=name,font=("monospace",20,"bold"),width=30)
        nameInput.grid(row=1,column=2,pady=10,padx=5)

        Label(self.login_frame,text="Email",font=("monospace",20,"bold")).grid(column=1,row=2,pady=10,padx=5)
        emailInput = Entry(self.login_frame,textvariable=email,font=("monospace",20,"bold"),width=30)
        emailInput.grid(row=2,column=2,pady=10,padx=5)

        Label(self.login_frame,text="Password",font=("monospace",20,"bold")).grid(column=1,row=3,padx=5,pady=10)
        emailInput = Entry(self.login_frame,textvariable=password,show="*",font=("monospace",20,"bold"),width=30)
        emailInput.grid(row=3,column=2,padx=5,pady=10)

        Button(self.login_frame,text="Home",font=("monospace",20,"bold"),command=self.startingPage).grid(row=4,column=1,pady=20,padx=5)

        Button(self.login_frame,text="Submit",font=("monospace",20,"bold"),command=lambda:self.signInUser({"username":name.get(),"email":email.get(),"password":password.get()})).grid(row=4,column=2,pady=20,padx=5)

        self.login_frame.pack()
    
    def errorPage(self,message):
        self.starting_frame.pack_forget()
        self.signIn_frame.pack_forget()
        self.login_frame.pack_forget()
        self.user_home_page_frame.pack_forget()
        self.all_todo_frame.pack_forget()
        self.update_todo_frame.pack_forget()
        self.menubar.destroy()

        if(self.client):
            self.client.close()
            self.client = None

        self.root.title("Internal Server Error - 500")
        Label(self.error_frame,text="Internal Server Error",font=("monospace",20,"bold")).grid(column=2,row=1,pady=20)
        Label(self.error_frame,text="Status Code - 500",font=("monospace",20,"bold")).grid(row=2,column=2,pady=20)
        Label(self.error_frame,text=message,font=("monospace",20,"bold")).grid(row=3,column=2,pady=20)
        Button(self.error_frame,text="Home",font=("monospace",20,"bold"),command=self.startingPage).grid(row=4,column=2,pady=20,padx=5)

        self.error_frame.pack()

    def startingPage(self):
        self.signIn_frame.pack_forget()
        self.login_frame.pack_forget()
        self.error_frame.pack_forget()
        self.menubar.destroy()
        self.user_home_page_frame.pack_forget()
        self.all_todo_frame.pack_forget()
        self.update_todo_frame.pack_forget()
        self.root.title("Todo App")

        if(self.client):
            self.client.close()
            self.client = None

        Label(self.starting_frame,text="Welcome to Todo's App".upper(),font=("monospace",20,"bold")).grid(column=2,row=1,pady=20)

        signIn = Button(self.starting_frame,text="Login",font=("monospace",20,"bold"),command=self.loginPage)
        signIn.grid(column=2,row=2,padx=100,pady=10)

        login = Button(self.starting_frame,text="Sign In",font=("monospace",20,"bold"),command=self.signInPage)
        login.grid(column=2,row=3,padx=100,pady=10)

        close = Button(self.starting_frame,text="Exit",font=("monospace",20,"bold"),command=self.root.destroy)
        close.grid(column=2,row=4,padx=100,pady=10)

        self.starting_frame.pack()


if __name__ == '__main__':
    #** creating object of this class
    app  = App()


    #! for converting this app to exe file
    #* pyinstaller --onefile -w TodosApp.py
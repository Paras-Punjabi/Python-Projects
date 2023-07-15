import socket
import threading
from tkinter import *
from tkinter import messagebox

class Client:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Chatting App")
        self.name = None
        self.client = None
        self.PORT = 3000
        self.menu = Menu(self.root)
        self.frame = Frame(self.root)
        self.message_frame = Frame(self.root)
        self.chat_frame = Frame(self.root,width=self.root.winfo_screenwidth(),height=self.root.winfo_screenheight()-30)
        self.createFrontPage()
        self.root.mainloop()
    
    def connection(self,name):
        try:
            self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            host = socket.gethostbyname(socket.gethostname())
            self.client.connect((host,self.PORT))
            self.name = name
            self.client.send(name.encode("utf-8"))
            self.recieveMessage()
        except Exception as e:
            print("Not Connected to Server")
            self.createMessageContainer(self.chat_frame,"Disconnected From Server","#ff726f")
            self.client.close()

    def connectToServer(self,name):
        if name!="":
            t = threading.Thread(target=lambda:self.connection(name))
            t.start()
            self.root.title(self.name)
            self.chatRoom()
        else:
            messagebox.askokcancel(title="Name",message="Fill the details from which you have to join the chat")

    def createMessageContainer(self,frame,message,color):
        Label(frame,text=message,font=("monospace",15,"bold"),background=color).pack(side=TOP,pady=2)
    
    def sendMessage(self,text):
        try:
            self.createMessageContainer(self.chat_frame,f"You: {text}","yellow")
            self.client.send(f"{self.name}: {text}".encode("utf-8"))
        except Exception as e:
            self.createMessageContainer(self.chat_frame,"Messages cannot be send","#ff726f")
    
    def recieveMessage(self):
        try:
            self.createMessageContainer(self.chat_frame,"You joined the chat","yellow")
            while True:
                msg = self.client.recv(1024).decode("utf-8")
                self.createMessageContainer(self.chat_frame,msg,"pink")
        except Exception as e:
            self.createMessageContainer(self.chat_frame,"Cannot recieve Message","#ff726f")
            print(e)
        self.client.close()

    def chatRoom(self):
        self.message_frame.pack_forget()
        self.chat_frame.pack_forget()
        self.frame.pack_forget()
        self.menu.pack_forget()
        self.menu = Menu(self.root)
        self.createMenuBar()

        self.root.protocol("WM_DELETE_WINDOW",self.closeConnection)

        self.message_frame = Frame(self.root)
        self.chat_frame = Frame(self.root)
        message = StringVar()
        inputBox = Entry(self.message_frame,textvariable=message,font=("monospace",15,"bold"),width=55,background="#FCFCFC")
        inputBox.grid(row=0,column=0,padx=5)

        Button(self.message_frame,text="Send",font=("monospace",15,"bold"),command=lambda:f"{self.sendMessage(message.get())} {message.set('')}").grid(row=0,column=1,padx=5)
        self.message_frame.pack(side=BOTTOM,pady=5)
        
        self.chat_frame.pack()

    def createFrontPage(self):
        self.chat_frame.pack_forget()
        self.frame.pack_forget()
        self.menu.destroy()
        self.message_frame.pack_forget()
        self.frame = Frame(self.root)
        Label(self.frame,text="Chatting App - Client Interface",font=("monospace",25,"bold")).grid(row=0,column=2,pady=10)
        Label(self.frame,text="Name",font=("monospace",18,"bold")).grid(row=1,column=1,pady=2)
        clientName = StringVar()
        Entry(self.frame,textvariable=clientName,font=("monospace",18,"bold"),width=35).grid(row=1,column=2,pady=20)

        Button(self.frame,text="Join Chat",font=("monospace",25,"bold"),command=lambda:self.connectToServer(clientName.get())).grid(row=2,column=2,pady=20)
        self.frame.pack()
    
    def leaveChat(self):
        self.client.close()
        self.createFrontPage()
    
    def createMenuBar(self):
        self.menu = Menu(self.root)
        home = Menu(self.menu,tearoff=False)
        self.menu.add_cascade(label="Options",menu=home)
        home.add_cascade(label="Leave Chat",command=self.leaveChat)
        home.add_separator()
        home.add_cascade(label="Exit",command=self.close)
        self.root.config(menu=self.menu)
        
    def closeConnection(self):
        response = messagebox.askyesno(title="Leaving Chat Room",message="Are you sure you want to leave the chat?")
        if response:
            if self.client:
                self.client.close()
            self.root.destroy()
            exit()
    
    def close(self):
        if self.client:
            self.client.close()
        self.root.destroy()
        exit()

if __name__ == '__main__':
    Client()
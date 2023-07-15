import socket
from tkinter import *
import threading

class Server:
    def __init__(self):
        self.root = Tk()
        self.root.title("Server")
        self.root.geometry("400x400")

        self.server = None
        self.clients = []
        self.names = []
        self.events = []
        self.PORT = 3000
        self.__isOpen = True
        self.__serverThread = None

        self.frame = Frame(self.root)
        self.message_frame = Frame(self.root)
        self.createMenuBar()
        self.createFrontPage()
        self.root.mainloop()
    
    def handleClient(self,client):
        connected = True
        name = None
        try:
            while connected:
                message = client.recv(1024).decode("utf-8")
                if message == "!DISCONNECT":
                    connected = False
                    name = self.names[self.clients.index(client)]
                    self.names.remove(self.names[self.clients.index(client)])
                    self.clients.remove(client)
                    break
                for item in self.clients:
                    if client is not item:
                        item.send(message.encode("utf-8"))
        except:
            Label(self.frame,text=f"{self.names[self.clients.index(client)]} disconnects",font=("monospace",10,"bold")).pack(side=TOP,pady=2)
            self.events.append(f"{self.names[self.clients.index(client)]} disconnects")
            name = self.names[self.clients.index(client)]
            self.names.remove(self.names[self.clients.index(client)])
            self.clients.remove(client)
            self.sendMessageFromServer(None,f"{name} left the chat")
        client.close()
    
    def sendMessageFromServer(self,client,message):
        if message != "":
            for items in self.clients:
                if items != client:
                    items.send(message.encode("utf-8"))

    def createServer(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = socket.gethostbyname(socket.gethostname())
        self.server.bind((host,self.PORT))
        self.server.listen()
        print("Server Started on port " + str(self.PORT))
        try:
            while self.__isOpen:
                client,address = self.server.accept()
                name = client.recv(1024).decode("utf-8")
                self.names.append(name)
                self.clients.append(client)
                
                Label(self.frame,text=f"{name} joined the chat with IP {address[0]}",font=("monospace",10,"bold")).pack(side=TOP,pady=2)
                self.events.append(f"{name} joined the chat with IP {address[0]}")
                self.sendMessageFromServer(client,f"{name} joined the chat")

                try:
                    thread = threading.Thread(target=lambda:self.handleClient(client))
                    thread.start()
                except Exception as e:
                    pass
        except Exception as e:
            print("Server Closed")
    
    def startServer(self,event):
        if(event.widget.cget("text") == "Start Server"):
            event.widget.config(text="Close Server")
            self.__serverThread = threading.Thread(target=self.createServer)
            self.__serverThread.start()

        elif (event.widget.cget("text") == "Close Server"):
            event.widget.config(text="Start Server")
            for items in self.clients:
                items.close()
            self.__isOpen = False
            self.server.close()
            self.server = None
    
    def createMessageInterface(self):
        self.frame.pack_forget()
        self.message_frame.pack_forget()

        self.message_frame = Frame(self.root)
        msg =StringVar()
        Label(self.message_frame,text="Message Interface",font=("monospace",22,"bold")).pack(side=TOP,pady=10)
        Entry(self.message_frame,textvariable=msg,font=("monospace",18,"bold"),width=25).pack(side=TOP,pady=20)
        Button(self.message_frame,text="Send",font=("monospace",18,"bold"),command=lambda:f"{self.sendMessageFromServer(None,f'Server: {msg.get()}')} {msg.set('')}").pack(side=TOP,pady=10)
        self.message_frame.pack()
            
    def createFrontPage(self):
        self.message_frame.pack_forget()
        self.frame.pack_forget()

        self.frame = Frame(self.root)
        Label(self.frame,text="Server Interface",font=("monospace",25,"bold")).pack(side="top",pady=10)

        btn = Button(self.frame,text="Start Server",font=("monospace",18,"bold"))
        btn.bind("<Button-1>",self.startServer)
        btn.pack(side=TOP,pady=5)

        if self.server !=None:
            btn.config(text="Close Server")
        
        Button(self.frame,text="Exit",font=("monospace",18,"bold"),command=self.close).pack(side=TOP,pady=5)

        for items in self.events:
            Label(self.frame,text=items,font=("monospace",10,"bold")).pack(side=TOP,pady=2)

        self.frame.pack()
    
    def createMenuBar(self):
        menu = Menu(self.root)
        home = Menu(menu,tearoff=False)

        menu.add_cascade(label="Options",menu=home)

        home.add_cascade(label="Server Interface",command=self.createFrontPage)
        home.add_cascade(label="Send Message to Clients",command=self.createMessageInterface)
        home.add_separator()
        home.add_cascade(label="Exit",command=self.close)

        self.root.config(menu=menu)
    
    def close(self):
        if self.server:
            self.server.close()
        self.root.destroy()
        self.clients = []
        self.names = []
        self.events = []
        exit()

if __name__ == '__main__':
    s = Server()
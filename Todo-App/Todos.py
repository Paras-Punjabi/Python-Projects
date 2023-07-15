import datetime
class Todo:
    def __init__(self,title,data,identity):
        self.title = title
        self.data = data
        self.identity = identity
        self.date = datetime.datetime.now().strftime("%d-%m-%Y")
    
    def toDict(self):
        return {"title":self.title,"data":self.data,"identity":self.identity,"date":self.date}


    
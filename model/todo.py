class Todo:
    def __init__(self,id,title:str ,done:int):
        self.title =  title
        self.done = done
        self.id = id

    def serialize(self):
        return {
            'id':self.id,
            'title': self.title,
            'done': self.done
        }
import  sqlite3

def getConnection():
    return sqlite3.connect("todo.db")
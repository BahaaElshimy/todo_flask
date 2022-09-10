import  sqlite3

connection  = sqlite3.connect('todo.db')
cursor = connection.cursor()

todo_table =  'create table if not exists todo (id INTEGER primary key ,  title text , done int default 0)'

cursor.execute(todo_table)
cursor.execute('insert into todo (title, done) values (?,?)' , ('finish python course' ,  0))

connection.commit()

for row in cursor.execute('select  * from todo'):
    print(row)

connection.close()
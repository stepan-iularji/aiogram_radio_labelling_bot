import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def chat_exists (self , chat_id):
    	"""Проверяем, есть ли уже chat в базе"""
    	with self.connection:
            result = self.cursor.execute('SELECT * FROM `tab_1` WHERE `chat_id` = ?', (chat_id,)).fetchall()
            return bool(len(result))

    def add_chat(self, chat_id, status = True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute('''INSERT INTO 
                tab_1 (chat_id , stage ) VALUES(? , ?)''', (chat_id , 0))

    def up_stage(self , chat_id , stage):
        with self.connection:
            return self.cursor.execute("UPDATE tab_1 SET stage = ? WHERE chat_id = ?" , (stage , chat_id))

    def get_stage (self , chat_id):
        with self.connection:
            return self.cursor.execute("SELECT stage FROM tab_1 WHERE chat_id = ? " , (chat_id , )).fetchall()[0][0]
     

    def add_input(self , chat_id , val):
        with self.connection:
            return self.cursor.execute("UPDATE tab_1 SET input = (SELECT input FROM tab_1 WHERE chat_id = ?) || ? WHERE chat_id = ?" , (chat_id , val , chat_id))

    def clr_input (self , chat_id):
        with self.connection:
            return self.cursor.execute("UPDATE tab_1 SET input = '' WHERE chat_id = ?" , (chat_id ,  ))

    def get_input(self , chat_id):
        with self.connection:
            return  self.cursor.execute("SELECT input FROM tab_1 WHERE chat_id = ?" , (chat_id , )).fetchall()[0][0]

    def get_file_id(self , id_):
        with self.connection:
            return  self.cursor.execute("SELECT file_id FROM file_ids WHERE id = ?" , (id_ , )).fetchall()[0][0]
        
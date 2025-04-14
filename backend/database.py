import mysql.connector

class Notesdatabase():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='35.232.159.63',
            port='3306',
            user='test',
            password='Suj782001@',
            database='UserData',
            charset='utf8mb4'
        )

        self.cursor = self.conn.cursor()


    def add_note(self, username, note):
        query = "INSERT INTO `UserData`.`t_user_notes` (username, notes) values ('test', 'test_note','')"
        insert_query = """
            INSERT INTO UserData.t_user_notes (username, notes)
            VALUES (%s,%s)
        """
        values = (username,note)

        self.cursor.execute(insert_query, values)
        self.conn.commit()  
        # self.cursor.execute(query)
        # self.cursor.close()
        print("added")


            

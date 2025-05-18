import mysql.connector
from flask import Flask, request, jsonify

class Notesdatabase():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='34.10.146.177',
            port='3306',
            user='root2',
            password='123456789',
            database='NotesAPP',
            charset='utf8mb4'
        )

        self.cursor = self.conn.cursor()

    def add_user(self,username, password):
        try:
            insert_query = """
                INSERT INTO NotesAPP.users (user_name,user_password)
                VALUES (%s,%s)
            """
            values = (username,password)

            self.cursor.execute(insert_query, values)
            self.conn.commit() 
            print
            return jsonify({
                "message":"new user added successsfully",
                "result":"success"
            })
        except Exception as error:
            print(str(error))
            return jsonify({
                "result":"fail"
            }), 500

    def get_user(self,username):
        try:
            select_query = """
                SELECT user_id,user_name from NotesAPP.users where user_name=(%s)
            """
            values = (username,)

            self.cursor.execute(select_query, values)
            result = self.cursor.fetchone()
            if result is None:
                return jsonify({
                    "result":"No user found"
                })
            return jsonify({
                "id":result[0],
                "username":result[1],
                "result":"success"
            })
        except Exception as error:
            print(str(error))
            return jsonify({
                "result":"fail"
            }), 500


    def login_user(self,username):
        try:
            select_query = """
                SELECT * from NotesAPP.users where user_name=(%s)
            """
            values = (username,)

            self.cursor.execute(select_query, values)
            result = self.cursor.fetchone()
            if result is None:
                return jsonify({
                    "result":"No user found"
                })
            return {
                "id":result[0],
                "username":result[1],
                "userpassword":result[2],
                "result":"success"
            }
        except Exception as error:
            print(str(error))
            return jsonify({
                "result":"fail"
            }), 500



    def add_note(self, username, note):
        query = "INSERT INTO `NotesAPP`.`userdata` (username, usernotes) values ('test', 'test_note','')"
        insert_query = """
            INSERT INTO NotesAPP.userdata (username, usernotes)
            VALUES (%s,%s)
        """
        values = (username,note)

        self.cursor.execute(insert_query, values)
        self.conn.commit()  
        # self.cursor.execute(query)
        # self.cursor.close()
        print("added")

    # def get_notes(self, username):
        # query = "SELECT * from `NotesAPP`.`t_user_notes` where username = %s"
        # self.cursor.execute(query, (username,))
        # rows = self.cursor.fetchall()
        
        # notes = []
        # for row in rows:
        #     notes.append({
        #         'id': row[0],
        #         'username': row[1],
        #         'note': row[2],
        #         'created_at': row[3]
        #     })

        # return notes


            

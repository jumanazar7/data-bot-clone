import sqlite3


class Database:
    def __init__(self, path_to_db="C:/Users/Jumanazar/Desktop/DATA bot/DATAbot/data/main1.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    def create_table_users(self):
        sql = """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            tg_id INTEGER NOT NULL UNIQUE,
            full_name VARCHAR(255) NOT NULL,
            username TEXT UNIQUE,
            language VARCHAR(5)
            );"""
        self.execute(sql, commit=True)

        
    def create_curses_table(self):
        sql = """
        CREATE TABLE Curses (
            id INTEGER PRIMARY KEY,
            title VARCHAR(30) NOT NULL,
            slog varchar(30) NOT NULL,
            puli REAL NOT NULL,
            malumot VARCHAR(300) NOT NULL,
            imageurl TEXT NULL
            );"""
        self.execute(sql, commit=True)
 
    def create_ustozlar_table(self):
        sql = """
        CREATE TABLE Ustozlar (
            id INTEGER PRIMARY KEY,
            title VARCHAR(30) NOT NULL,
            slog VARCHAR(30) NOT NULL,
            tajribasi VARCHAR(400) NOT NULL,
            image_url TEXT NULL,
            sub_curses_id INTEGER NOT NULL
            );"""
        self.execute(sql, commit=True)
    
    def create_curses_table_maonth(self):
        sql = """
        CREATE TABLE Curses_manth (
            id INTEGER PRIMARY KEY,
            slog VARCHAR(30) NOT NULL,
            oylik_reja varchar(4000) NOT NULL,
            sub_curses_id INTEGER NOT NULL
            );"""
        self.execute(sql, commit=True)

    def create_curses_table_video(self):
        sql = """
        CREATE TABLE Cuorses_video (
            id INTEGER PRIMARY KEY,
            slog VARCHAR(150) NOT NULL,
            caopshin VARCHAR(850) NOT NULL,
            file_id varchar(400) NOT NULL,
            sub_curses_id INTEGER NOT NULL,
            name VARCHAR(30) NOT NULL
            );"""
        self.execute(sql, commit=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self,tg_id : int,full_name: str, username: str, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(tg_id, full_name, username, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(tg_id, full_name, username, language), commit=True)
    
    def add_curses(self,title : str,slog: str, puli: str, malumot: str,imge_url:str):
        sql = """
        INSERT INTO Curses(title, slog, puli, malumot, imageurl) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(title, slog, puli, malumot,imge_url), commit=True)
    
    
    def add_curses_math(self,slog : str,oylik_reja: str, sub_id: str,):
        sql = """
        INSERT INTO Curses_manth(slog, oylik_reja,sub_curses_id) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(slog,oylik_reja,sub_id), commit=True)
    
    def add_ustozlar(self,title: str ,slog : str,tajribasi: str,imge_url:str, sub_id: str,):
        sql = """
        INSERT INTO Ustozlar(title,slog,tajribasi,image_url,sub_curses_id) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(title,slog,tajribasi,imge_url,sub_id), commit=True)

    def add_video(self,slog : str,tajribasi: str,file_id:str, sub_id : str, name : str,):
        sql = """
        INSERT INTO Cuorses_video(slog,caopshin,file_id,sub_curses_id,name) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(slog,tajribasi,file_id,sub_id,name), commit=True)

    def select_all_video(self):
        sql = """
        SELECT * FROM Cuorses_video
        """
        return self.execute(sql, fetchall=True)


    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)
    
    def select_all_Ustozlar(self):
        sql = """
        SELECT * FROM Ustozlar
        """
        return self.execute(sql, fetchall=True)

    def select_all_curses(self):
        sql = """
        SELECT * FROM Curses
        """
        return self.execute(sql, fetchall=True)

    def select_all_curses_ustozlar(self, **kwargs):
        sql = """
        SELECT * FROM Curses WHERE
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters, fetchone=True)

    
    def select_all_curses_id(self, **kwargs):
        sql = """
        SELECT id FROM Curses WHERE
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters, fetchone=True)

    def select_all_Ustozlar_id(self, **kwargs):
        sql = """
        SELECT id FROM Ustozlar WHERE
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters, fetchone=True)

    def select_all_math(self, **kwargs):
        sql = """
        SELECT * FROM Curses_manth WHERE
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters, fetchall=True)

    def select_video(self, **kwargs):
        sql = """
        SELECT * FROM Cuorses_video WHERE
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters, fetchall=True)

    def select_all_ustozlar(self, **kwargs):
        sql = """
        SELECT * FROM Ustozlar WHERE
        """
        sql,parameters = self.format_args(sql,kwargs)
        return self.execute(sql,parameters=parameters, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def delete_ustozlar(self, id):
        sql = "DELETE FROM Ustozlar WHERE id=?"
        return self.execute(sql, parameters=(id, ), commit=True)

    def delete_ustozlar_sub(self, id):
        sql = "DELETE FROM Ustozlar WHERE sub_curses_id=?"
        return self.execute(sql, parameters=(id, ), commit=True)
    def delete_curses(self, id):
        sql = "DELETE FROM Curses WHERE id=?"
        return self.execute(sql, parameters=(id, ), commit=True)

    def delete_curses_math(self, sub_curses_id):
        sql = "DELETE FROM Curses_manth WHERE sub_curses_id=?"
        return self.execute(sql, parameters=(sub_curses_id, ), commit=True)

    def count_curses(self):
        return self.execute("SELECT COUNT(*) FROM Curses;", fetchone=True)
    
    # def update_user_email(self, email, id):
    #     # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

    #     sql = f"""
    #     UPDATE Users SET email=? WHERE id=?
    #     """
    #     return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    

def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")

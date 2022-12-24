
import sqlite3
# connect sqlite3 database
class DataBase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('database.db',check_same_thread=False)
        self.c = self.conn.cursor()
    
    def find_user_with_email(self, email,password):
        #dict cursor
        
        query = "SELECT * FROM User WHERE Email = ? AND Password = ?"
        try:
          
          self.conn.row_factory = sqlite3.Row
          things = self.conn.execute(query, (email,password)).fetchall()
          unpacked = [{k: item[k] for k in item.keys()} for item in things]
          return unpacked[0]
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return []
    
    def get_categories(self):
        query = "SELECT * FROM Category"
        try:
          self.conn.row_factory = sqlite3.Row
          things = self.conn.execute(query).fetchall()
          unpacked = [{k: item[k] for k in item.keys()} for item in things]
          return unpacked
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return []
    def add_user(self,name,email,password):
        query = "INSERT INTO User (Name,Email,Password) VALUES (?,?,?)"
        try:
          self.conn.execute(query,(name,email,password))
          self.conn.commit()
          return True
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return False
    def get_ringtones(self):
        query = "select * from Ringtones join Category C on Ringtones.Ringtone_category_id = C.Category_id;"
        try:
          self.conn.row_factory = sqlite3.Row
          things = self.conn.execute(query).fetchall()
          unpacked = [{k: item[k] for k in item.keys()} for item in things]
          return unpacked
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return []
    
if __name__ == '__main__':
    db = DataBase()
    print(db.find_user_with_email('mail1@dd','6060'))
    print(db.get_categories())
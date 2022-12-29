
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
    def add_to_cart(self,user_id,ringtone_id):
        query = "INSERT INTO UserBasket (User_id,Ringtone_id) VALUES (?,?)"
        try:
          self.conn.execute(query,(user_id,ringtone_id))
          self.conn.commit()
          return True
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return False
          
    def get_cart(self,user_id):
        query = "select * from UserBasket join Ringtones R on UserBasket.Ringtone_id = R.Ringtone_id where User_id = ?"
        try:
          self.conn.row_factory = sqlite3.Row
          things = self.conn.execute(query,(user_id,)).fetchall()
          unpacked = [{k: item[k] for k in item.keys()} for item in things]
          return unpacked
        except Exception as e:
            print(f"Failed to execute. Query: \n with error:\n{e}")
            return []
    def delete_from_cart(self,user_id,ringtone_id):
      query = "DELETE FROM UserBasket WHERE User_id = ? AND Ringtone_id = ?"
      try:
        self.conn.execute(query,(user_id,ringtone_id))
        self.conn.commit()
        return True
      except Exception as e:
          print(f"Failed to execute. Query: \n with error:\n{e}")
          return False
        
    def buy_cart(self,user_id,ringtone_ids):
      for ringtone_id in ringtone_ids:
        self.delete_from_cart(user_id,ringtone_id)
        query = "INSERT INTO OwnedRingtones (Userid,Ringtoneid) VALUES (?,?)"
        try:
          self.conn.execute(query,(user_id,ringtone_id))
          self.conn.commit()
        except Exception as e:
          print(f"Failed to execute. Query: \n with error:\n{e}")
    
    def get_rintone_ids_cart(self,user_id):
      query = "select Ringtone_id from UserBasket where User_id = ?"
      try:
        self.c = self.conn.cursor()
        things = self.conn.execute(query,(user_id,)).fetchall()
        ids = [item[0] for item in things]
        return ids
      except Exception as e:
          print(f"Failed to execute. Query: \n with error:\n{e}")
          return []
    
if __name__ == '__main__':
    db = DataBase()
    #print(db.find_user_with_email('mail1@dd','6060'))
    #print(db.get_categories())
    #print(db.add_to_cart(1,5))
    #print(db.get_cart(1))
    #print(db.delete_from_cart(1,2))
    #print(db.buy_cart(1,[1,5]))
    print(db.get_rintone_ids_cart(1))
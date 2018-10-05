from flask_bcrypt import Bcrypt

class User:
   def __init__(self, data = {}):
        self.user_id = data.get('user_id')
        self.username = data.get('username')
        self.email = data.get('email')
        self.b_crypt = Bcrypt()
        if data.get('password'):
            self.password = self.b_crypt.generate_password_hash(data.get('password')).decode('utf-8')
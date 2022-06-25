from flask import Flask
from helpers.file import get_users
app = Flask(__name__)

with app.app_context():
    from routes.main import *
search_keyword = 'tes'
users = get_users()
search_result = []
for user in users:
    print(str(user.values()))
    if str(search_keyword).lower() in str(user.values()).lower():
        search_result.append((user))
print('-------------------------------------------------------')
print(search_result)

if __name__ == "__main__":
    app.run(port=5000,  host='0.0.0.0', debug=True)
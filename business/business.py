from flask import Flask, request, Response
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'USER'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)



def get_user_by_id(user_id, cursor):
    cursor.execute('SELECT * FROM USERS WHERE id = "{}"'.format(user_id))
    res =  cursor.fetchone()
    user_id, user_username = res[0], res[1]
    print('User {} is asking for a partner...'.format(user_username))
    return user_id, user_username

def get_user_random(cursor):
    cursor.execute('SELECT * FROM USERS ORDER BY RAND() LIMIT 1')
    res =  cursor.fetchone()
    user_id, user_username = res[0], res[1]
    return user_id, user_username

def add_partnership(cursor, user1_id, user2_id):
    cursor.execute('INSERT INTO PARTNERSHIP(user1,user2) VALUES ("{}", "{}")'.format(user1_id, user2_id))
    return cursor.lastrowid

def make_partnership(user_id, conn):
    cursor = conn.cursor()
    user1 = get_user_by_id(user_id, cursor)
    user2 = get_user_random(cursor)
    partnership_id = add_partnership(cursor, user1[0], user2[0])
    conn.commit()
    message =  '<part_no:' + str(partnership_id) + '>' + user1[1] + '&' + user2[1] + ' are now parteners'
    return message


@app.route('/test/', methods=['GET', 'POST'])
def test():

    print('Got request on/test/', flush=True)
    conn = mysql.connect()
    print('Opened connection:')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * from USERS")
        data = cursor.fetchone()
        print(data)
    except Exception as e:
        print(str(e))
    return str('!!!OK')

@app.route('/partnership/', methods=['POST'])
def partnership():
    """Get the user and another random user to make a partnership
    Returns: partnership details
    """
    print('Got request on /partnership/', flush=True)
    request_user = int(request.json['user_id'])
    print('Open connection to db....')
    conn = mysql.connect()
    print('Opened connection:')
    try:
        partnership_message = make_partnership(request_user, conn)
    except Exception as e:
        partnership_message = "The partnership can not be made"
        print(str(e))
    finally:
        conn.close()
    return partnership_message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
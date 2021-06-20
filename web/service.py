import tensorflow as tf
import psycopg2
import os

server_env = os.environ.get('SERVER_ENV', 'DEV')

if server_env == 'PROD':
    pg_db = os.environ['PG_DB']
    pg_user = os.environ['PG_USER']
    pg_pwd = os.environ['PG_PWD']
    pg_host = os.environ['PG_HOST']
    pg_port = os.environ['PG_PORT']
    conn = psycopg2.connect(database=pg_db, user=pg_user,password=pg_pwd, host=pg_host, port=pg_port)
else:
    conn = psycopg2.connect(database="what_to_eat", user="postgres",password="align", host="localhost", port="5432")


def load_users_foods(users, foods):
    default_users_foods = tf.constant(
        [
            [4, 3, 3, 0, 2, 0],
            [0, 10, 4, 0, 6, 8],
            [10, 3, 3, 0, 3, 2],
            [10, 9, 0, 10, 0, 2]
        ], dtype=tf.float32
    )

    print(default_users_foods)

    return default_users_foods


def load_foods_features(foods, features):
    # movie has features
    default_foods_features = tf.constant([
        [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]
    ], dtype=tf.float32)

    print(default_foods_features)
    return default_foods_features


def load_foods():
    cursor = conn.cursor()
    cursor.execute("select name from restauarants")
    rows = cursor.fetchall()
    cursor.close()

    result = []
    for row in rows:
        result.append(row[0])

    #return ['桃源春卷', '三圣面', '大食代', '高级茶餐厅', '海底捞', '山西手工面']

    print(result)
    return result


def load_features():
    cursor = conn.cursor()
    cursor.execute("select feature from features")
    rows = cursor.fetchall()
    cursor.close()

    result = []
    for row in rows:
        result.append(row[0])
    return result


def load_users():
    cursor = conn.cursor()
    cursor.execute("select name from users")
    rows = cursor.fetchall()
    cursor.close()

    result = []
    for row in rows:
        result.append(row[0])
    # return ['清淡,25,ANY', '重口,25,ANY', '清淡,50,中餐', '清淡,100,ANY']
    return result


def save_user(name):
    cursor = conn.cursor()
    cursor.execute("select * from users")
    rows = cursor.fetchall()
    cursor.close()

    for row in rows:
        print('id = ',row[0], 'name = ', row[1], '\n')
        if row[1] == name:
            return name

    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name) values('{}')".format(name))
    conn.commit()

    return True

# conn.close()

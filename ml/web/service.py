import tensorflow as tf


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
    return ['桃源春卷', '三圣面', '大食代', '高级茶餐厅', '海底捞', '山西手工面']


def load_features():
    return ['清淡', '重口', '辣椒', '健康', '减肥餐', '我爱面食', '我爱米饭', '特色', '本地', '网红', '价格低', '价格中', '价格高']


def load_users():
    return ['清淡,25,ANY', '重口,25,ANY', '清淡,50,中餐', '清淡,100,ANY']
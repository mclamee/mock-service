import flask
import service

from flask import request, jsonify

from recomm import Recomm

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    # default_users = ['清淡,25,ANY', '重口,25,ANY', '清淡,50,中餐', '清淡,100,ANY']
    # default_foods = ['桃源春卷', '三圣面', '大食代', '高级茶餐厅', '海底捞', '山西手工面']
    # default_features = ['清淡', '重口', '辣椒', '健康', '减肥餐', '我爱面食', '我爱米饭', '特色', '本地', '网红', '价格低', '价格中', '价格高']

    users = request.args.get('users').split('|')  # 清淡,25,ANY|重口,25,ANY|清淡,50,中餐|清淡,100,ANY

    all_users = service.load_users()
    foods = service.load_foods()
    features = service.load_features()

    users_foods = service.load_users_foods(all_users, foods)
    foods_features = service.load_foods_features(foods, features)

    top_foods = Recomm(all_users, foods, features, users_foods, foods_features).recomm()

    result = {}
    for i in range(len(all_users)):
        if all_users[i] in users:
            food_names = [foods[index] for index in top_foods[i]]
            result[all_users[i]] = food_names

    return jsonify(result)

app.run()

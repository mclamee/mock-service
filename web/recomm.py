#!/usr/bin/env python
# coding: utf-8

# In[4]:


# get_ipython().system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==2.2.3')


# In[69]:


import numpy as np
import tensorflow as tf

default_users = ['清淡,25,ANY', '重口,25,ANY', '清淡,50,中餐', '清淡,100,ANY']
default_foods = ['桃源春卷', '三圣面', '大食代', '高级茶餐厅', '海底捞', '山西手工面']
default_features = ['清淡', '重口', '辣椒', '健康', '减肥餐', '我爱面食', '我爱米饭', '特色', '本地', '网红', '价格低', '价格中', '价格高']

# user reates foods
default_users_foods = tf.constant(
    [
        [4, 3, 3, 0, 2, 0],
        [0, 10, 4, 0, 6, 8],
        [10, 3, 3, 0, 3, 2],
        [10, 9, 0, 10, 0, 2]
    ], dtype=tf.float32
)

# movie has features
default_foods_features = tf.constant([
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]
], dtype=tf.float32)


class Recomm:
    def __init__(self, users, foods, features, users_foods, foods_features):
        print(tf.__version__)
        self.users = users
        self.foods = foods
        self.features = features
        self.users_foods = users_foods
        self.foods_features = foods_features

    def recomm(self):

        num_users = len(self.users)
        num_foods = len(self.foods)
        num_features = len(self.features)
        num_recommdations = 3

        # Mattrix: the user rated features
        users_features = tf.matmul(self.users_foods, self.foods_features)
        users_features

        # scale up
        users_features = users_features / tf.reduce_sum(users_features, axis=1, keepdims=True)
        users_features

        # Rank the user rated features that each of the users like the most so far
        # nn = neural network
        top_users_features = tf.nn.top_k(users_features, num_features)[1]
        top_users_features  # indexes of which movie which user like the most

        for i in range(num_users):
            feature_names = [self.features[int(index)] for index in top_users_features[i]]
            print('{}: {}'.format(self.users[i], feature_names))

        users_ratings = tf.matmul(users_features, tf.transpose(self.foods_features))
        users_ratings

        top_foods = tf.nn.top_k(users_ratings, num_recommdations)[1]
        top_foods

        for i in range(num_users):
            movie_names = [self.foods[index] for index in top_foods[i]]
            print('{}: {}'.format(self.users[i], movie_names))

        users_ratings_new = tf.where(
            tf.equal(self.users_foods, tf.zeros_like(self.users_foods)),
            users_ratings,
            tf.zeros_like(tf.cast(self.users_foods, tf.float32))
        )
        users_ratings_new

        top_foods = tf.nn.top_k(users_ratings_new, num_recommdations)[1]
        top_foods

        for i in range(num_users):
            movie_names = [self.foods[index] for index in top_foods[i]]
            print('{}: {}'.format(self.users[i], movie_names))

        return top_foods


Recomm(default_users, default_foods, default_features, default_users_foods, default_foods_features).recomm()

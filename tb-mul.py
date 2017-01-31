#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import tensorflow as tf

#データフローグラフを構築
a=tf.constant(20,name="a")
b=tf.constant(30,name="b")

mull_op=a*b

#セッションを作成
sess=tf.Session()

# TensorBoardを使う
tw=tf.train.SummaryWriter("log_dir",graph=sess.graph)

#セッションを実行する
print(sess.run(mull_op))

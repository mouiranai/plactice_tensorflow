#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf

a=tf.constant(100,name="a")
b=tf.constant(200,name="b")
c=tf.constant(300,name="c")
v=tf.Variable(0,name="v")

calc_op=a+b*c
assign_op=tf.assign(v,calc_op)

sess=tf.Session()

tw=tf.train.SummaryWriter("log_dir",graph_def=sess.graph_def)

sess.run(assign_op)
print(sess.run(v))

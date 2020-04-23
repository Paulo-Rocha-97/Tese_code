# tensor flow tutorial of important features 

import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 
import matplotlib.pyplot as plt

# Placeholders are used to feed in data from outside the computational graph compute using feed_dict
 
# %% example of simple session

# v1 = tf.Variable(5.0)

# p1 = tf.placeholder(tf.float32)

# new_val = tf.multiply(v1, p1)

# update = tf.assign(v1, new_val)

# with tf.Session() as sess:
    
#     sess.run(tf.global_variables_initializer())
    
#     for _ in range(3):
    
#         sess.run(update, feed_dict={p1: 2.0})
        
#     print(sess.run(v1))
    
# %% 

X = np.random.rand(100).astype(np.float32)

a = 50
b = 40
Y = a * X + b

Y = np.vectorize(lambda y: y + np.random.normal(loc=0.0, scale=0.5))(Y)

# %%

plt.plot(X, Y);

a_var = tf.Variable(1.0)
b_var = tf.Variable(1.0)
y_var = a_var * X + b_var

# Mean Square error 
loss = tf.reduce_mean(tf.square(y_var - Y))

# Gradient Descent optimization
optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)

Train_steps = 3000

results = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(Train_steps):
        results.append(sess.run([train, a_var, b_var])[1:])
        
final_pred = results[-1]
a_hat = final_pred[0]
b_hat = final_pred[1]
y_hat = a_hat * X + b_hat

plt.plot(X, y_hat);

print("a:", a_hat, "b:", b_hat)


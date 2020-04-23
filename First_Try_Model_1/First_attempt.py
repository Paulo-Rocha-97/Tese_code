
# This script is a first attempt at model 1

# Input:  - Day Index 
#         - Temperature
#         - Humidity
#         - Precipitation
#         - Solar Radiation
#         - Pressure
#         - Station 544 outflow
#         - Station 546 outflow
        
# Output: - Inflow to the reservoir 

import pickle as pr 
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 

input_var, output_var = pr.load(open ('Data_model_1.p','rb'))

Input= np.asarray(input_var)
Output = np.asarray(output_var)
Output = Output.reshape(1655,1)

Train_in = Input[5:10,:]
Train_out = Output[5:10,:]

# %% Neural Network Model 

# Parameters
learning_rate = 0.001
training_epochs = 10
display_step = 1
batch_size = 1

# Network Parameters
n_hidden_1 = 10 # 1st layer number of neurons
n_hidden_2 = 10 # 2nd layer number of neurons
n_input = 40 # MNIST data input (img shape: 28*28)
n_output = 1 # MNIST total classes (0-9 digits)

# tf Graph input
X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_output])

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_output]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_output]))
}


# Create model
def multilayer_perceptron(x, weights, biases):
    
    # Hidden fully connected layer with 256 neurons
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    # layer_1 = tf.nn.relu(layer_1)
    
    # Hidden fully connected layer with 256 neurons
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    # layer_2 = tf.nn.relu(layer_2)
    
    # Output fully connected layer with a neuron for each class
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    
    return out_layer

# Construct model
Pred = multilayer_perceptron(X, weights, biases)

# Define loss and optimizer
cost = tf.reduce_mean( tf.square(Train_out - Pred) )

optimizer = tf.train.GradientDescentOptimizer(0.0001)

train_op = optimizer.minimize( cost )

# Initializing the variables
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        
        avg_cost = 0.
            
        # Run optimization op (backprop) and cost op (to get loss value)
        c = sess.run(cost, feed_dict={X: Train_in, Y: Train_out})
        _ = sess.run(train_op, feed_dict={X: Train_in, Y: Train_out})
        
        # Compute average loss
        avg_cost += c 

        # Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost={:.9f}".format(avg_cost))
            
    print("Optimization Finished!")

    # Test model
    correct_estimation = tf.equal(Pred, Y)
    
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_estimation, "float"))
    print("Accuracy:", accuracy)

import boundingBox
import predict_function as pf
import sys
import tensorflow as tf
from PIL import Image, ImageFilter
import os
import pickle
import glob
import pprint
import operator

sy = ['dots', 'tan', ')', '(', '+', '-', 'sqrt', '1', '0', '3', '2', '4', '6', 'mul', 'pi', '=', 'sin', 'pm', 'A',
'frac', 'cos', 'delta', 'a', 'c', 'b', 'bar', 'd', 'f', 'i', 'h', 'k', 'm', 'o', 'n', 'p', 's', 't', 'y', 'x', 'div']

slash_sy = ['tan', 'sqrt', 'mul', 'pi', 'sin', 'pm', 'frac', 'cos', 'delta', 'bar', 'div','^','_']

variable = ['1', '0', '3', '2', '4', '6', 'pi', 'A', 'a', 'c', 'b', 'd', 'f', 'i', 'h', 'k', 'm', 'o', 'n', 'p', 's', 't', 'y', 'x', '(', ')']
brules = {}
for i in range(0,len(sy)):
    brules[i] = sy[i]

def predictint():
    # Define the model (same as when creating the model file)
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 40]))
    b = tf.Variable(tf.zeros([40]))

    def weight_variable(shape):
      initial = tf.truncated_normal(shape, stddev=0.1)
      return tf.Variable(initial)

    def bias_variable(shape):
      initial = tf.constant(0.1, shape=shape)
      return tf.Variable(initial)

    def conv2d(x, W):
      return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(x):
      return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])

    x_image = tf.reshape(x, [-1,28,28,1])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    W_fc2 = weight_variable([1024, 40])
    b_fc2 = bias_variable([40])

    y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    init_op = tf.initialize_all_variables()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init_op)
        saver.restore(sess, os.getcwd()+"/model.ckpt")
        print ("Model restored.")
        nf = open("result.txt", 'w')
        updated_nf = open("updated_result.txt", 'w')

        number = 0
        hit = 0
        
        test_equal_path = "./data/annotated_test_Equal/"
        test_data_path = "./data/annotated_test_Equal_boxes/"
        result_data_path = "./data/annotated_test_result_boxes/"
        test_data_list = glob.glob(test_equal_path+ '/*.*')

        for test_data in test_data_list:
            nf.write("predict for equation %s\n" %(test_data)) # write the result
            updated_nf.write("predict for equation %s\n" %(test_data)) # write the result
            test_symbol_list = boundingBox.createSymbol(test_data)

            test_symbol_list = sorted(test_symbol_list, key=operator.itemgetter(2, 3))
            for i in range(len(test_symbol_list)):
                test_symbol = test_symbol_list[i]
                imvalue, image = pf.imageprepare(test_symbol[0])
                prediction = tf.argmax(y_conv, 1)
                predint = prediction.eval(feed_dict={x: [imvalue], keep_prob: 1.0}, session=sess)
                if test_symbol[1] != "dot":
                    predict_result = brules[predint[0]]
                else:
                    predict_result = "dot"
                test_symbol = (test_symbol[0], predict_result, test_symbol[2], test_symbol[3], test_symbol[4], test_symbol[5])
                test_symbol_list[i] = test_symbol
                nf.write("\t%s\t[%d, %d, %d, %d]\n" %(test_symbol[1], test_symbol[2], test_symbol[3], test_symbol[4], test_symbol[5])) # write the result
            
            updated_symbol_list = pf.update(test_data, test_symbol_list)
            for updated_symbol in updated_symbol_list:
                updated_nf.write("\t%s\t[%d, %d, %d, %d]\n" %(updated_symbol[1], updated_symbol[2], updated_symbol[3], updated_symbol[4], updated_symbol[5])) # write the result
                
            equation = pf.toLatex(updated_symbol_list)
            updated_nf.write("%s\n" %(equation)) # write the result
            
        nf.close()

        print "see result is in result.txt"
        print "see result is in updated_result.txt"
#         print "Accuracy is ", (hit/float(number))

def main():
    predint = predictint()

if __name__ == "__main__":
    main()

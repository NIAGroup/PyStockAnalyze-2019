import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

PYTHON36 = False #using python3.5 due to tensorflow

DEBUG = True
#DEBUG = False

USE_ADJ_CLOSE = True
#settings based on .csv downloaded from Yahoo
Close = 'Close'
CloseIdx = 3
if USE_ADJ_CLOSE:
    Close = 'Adj Close'
    CloseIdx = 4

#not used for now, for future extension
stocks_list = ["intc", "csco", "ibm", "msft"] #tech stocks for now, bigger ones with decades of stock data
stockidx = 0 #will loop on this in the future

#intc=pd.DataFrame.from_csv("data/INTC.csv")
intc_csv = pd.DataFrame.from_csv("INTC.csv") #INTC.csv downloaded from https://finance.yahoo.com/quote/INTC/history?p=INTC
intc_dict = intc_csv.to_dict()
intc = pd.DataFrame.from_dict(intc_dict) #eventually, the primary input of this .py would be intc_dict from another .py

if DEBUG:
    #print("1st opening price which is for {} is {}".format(intc.iloc[0].index, intc.iloc[0, 0]))
    #QUESTION: how to get/print "date"/index? above line of code did NOT work
    print(intc.iloc[0, 0]) # print the opening price of the first row
    print(intc.iloc[0, 3])  # print the closing price of the first row
    print(intc.iloc[0, 4])  # print the adjusted closing price of the first row
    print("closing price of the 1st row again is {}".format(intc['Close'][0])) #print the closing price of the 1st row
    print("opening price of the last row is {}".format(intc.iloc[-1, 0])) # print the opening price of the last row
    print("shape of the stock's pandas DataFrame is {}".format(intc.shape))
    numDaysOfStockData = intc.shape[0]
    print("total number of days of stock price data is {}".format(numDaysOfStockData))
    print(intc.describe())
    #intc_2015 = intc.loc['2015-01-01':'2015-12-31']
    intc_2019bestthenworst = intc.loc['4/20/2019':'5/14/2019']
    print(intc_2019bestthenworst.loc['4/23/2019'])
    plt.figure(figsize=(10, 8))
    #intc['Close'].plot()
    intc[Close].plot()
    plt.show()

#Create a new column PriceDiff in the DataFrame intc
#intc['PriceDiff'] = intc['Close'].shift(-1) - intc['Close']
intc['PriceDiff'] = intc[Close].shift(-1) - intc[Close]
if DEBUG:
    print(intc[Close].loc['5/14/2019'])
    print(intc[Close].loc['5/15/2019'])
    print(intc['PriceDiff'].loc['5/14/2019'])
#Create a new column Return in the DataFrame intc
#intc['Return'] = intc['PriceDiff'] /intc['Close']
intc['Return'] = intc['PriceDiff'] /intc[Close]

#Create a new column Direction.
#The List Comprehension means : if the price difference is larger than 0, denote as 1, otherwise, denote as 0,
#for every record in the DataFrame - intc
intc['Direction'] = [1 if intc['PriceDiff'].loc[ei] > 0 else 0 for ei in intc.index ]	#ei is a name for any Index
# Run the following code to show the price difference on 5/14/2019
print('Price difference on {} is {}, direction is {}'.format('5/14/2019', intc['PriceDiff'].loc['5/14/2019'], intc['Direction'].loc['5/14/2019']))

#different number of days to be used in moving averages later on
#MA = [10, 20, 30, 50, 100, 200]   #15 combos to try
#MA_2n = [8, 16, 32, 64, 128, 256] #15 combos to try
MA = [10, 20, 30, 50, 100]   #10 combos to try
MA_2n = [8, 16, 32, 64, 128] #10 combos to try

for MAidx in range(len(MA)-1, -1, -1):
    MAColName = "MA" + str(MA[MAidx])
    #intc['ma50'] = intc['Close'].rolling(50).mean()
    intc[MAColName] = intc[Close].rolling(MA[MAidx]).mean()
    print("just added moving average column to the pandas DataFrame : {}".format(MAColName))
intc['Close1'] = intc[Close].shift(-1)
intc_withNA = intc
#use dropna to remove any "Not a Number" data
intc = intc.dropna()

#plot the moving average
plt.figure(figsize=(10, 8))
intc['MA50'].loc['5/15/2018':'5/15/2019'].plot(label='MA50')
intc['MA100'].loc['5/15/2018':'5/15/2019'].plot(label='MA100')
intc[Close].loc['5/15/2018':'5/15/2019'].plot(label=Close)
plt.legend()
plt.show()

#loop here for differnt combos of MA durations
for longerMA in range(len(MA)-1, 0, -1):
    print("The longer range used for moving average is {}".format(MA[longerMA]))
    for shorterMA in range(longerMA-1, -1, -1):
        print(".. and the shorter range for moving average is {}".format(MA[shorterMA]))
        MAColNameShorter = "MA" + str(MA[shorterMA])
        MAColNameLonger = "MA" + str(MA[longerMA])
        BuyMA = "BuyMA" + str(MA[shorterMA]) + "above" + str(MA[longerMA])
        #Add a new column for "Buy", e.g. MA10>MA50, assign 1 (buy/long the stock), otherwise, 0 (do nothing)
        #intc['Buy'] = [1 if intc.loc[ei, 'MA10']>intc.loc[ei, 'MA50'] else 0 for ei in intc.index]
        intc[BuyMA] = [1 if intc.loc[ei, MAColNameShorter] > intc.loc[ei, MAColNameLonger] else 0 for ei in intc.index]
        '''
        need to fix this warning for the line of code above and other codes below:
        SettingWithCopyWarning: 
        A value is trying to be set on a copy of a slice from a DataFrame.
        Try using .loc[row_indexer,col_indexer] = value instead
        '''
        # Add a new column "Profit" using List Comprehension, for any rows in intc
        # if Buy=1, the profit is calculated as the close price of tomorrow - the close price of today
        # Otherwise the profit is 0
        ProfitMA = "Profit" + str(MA[shorterMA]) + "above" + str(MA[longerMA])
        intc[ProfitMA] = [(intc.loc[ei, 'Close1'] - intc.loc[ei, Close]) / intc.loc[ei, Close]
                           if intc.loc[ei, BuyMA] == 1 else 0 for ei in intc.index]

#Plot a graph to show the Profit/Loss
#intc['Profit'] = [intc.loc[ei, 'Close1'] - intc.loc[ei, 'Close'] if intc.loc[ei, 'Buy']==1 else 0 for ei in intc.index]
intc['Profit10above50'] = [(intc.loc[ei, 'Close1'] - intc.loc[ei, Close])/intc.loc[ei, Close] if intc.loc[ei, 'BuyMA10above50']==1 else 0 for ei in intc.index]
intc['Profit10above50'].plot()
plt.axhline(y=0, color='red')
#Use .cumsum() to calculate the accumulated wealth over the period
intc['TotalProfit'] = intc['Profit10above50'].cumsum()
print("intc.tail() is {}".format(intc.tail()))
#plot the wealth to show the growth of profit over the period
if PYTHON36: #somehow this does NOT work after switching to python3.5 (as tensorflow was not installing for python 3.6)
    intc['TotalProfit'].plot()
    plt.title('Assuming you invest $100 for each day you long the stock, total profit you made is {}'.format(intc.loc[intc.index[-2], 'TotalProfit'] * 100))
    print('Assuming you invest $100 for each day you long the stock, total profit you made is {}'.format(intc.loc[intc.index[-2], 'TotalProfit'] * 100))
    plt.show()

#todo
#need to print the range of dates
#also need to print the number of days you invest $100 for the stock and the #days you do NOT invest
#also print the average return for the days you invest (total return was shown above)
print(intc.groupby(['BuyMA10above50'])['Profit10above50'].mean())
print(intc.groupby(['BuyMA10above50'])['Profit10above50'].mean()[1])
print("Date of 1st INTC price available in the database {}".format(intc.index[0]))
print("Date of last INTC price available in the database {}".format(intc.index[-1]))
for longerMA in range(len(MA)-1, 0, -1):
    for shorterMA in range(longerMA-1, -1, -1):
        BuyMA = "BuyMA" + str(MA[shorterMA]) + "above" + str(MA[longerMA])
        ProfitMA = "Profit" + str(MA[shorterMA]) + "above" + str(MA[longerMA])
        print("The average daily return for buying when ...")
        print("{} days MA is above {} days MA (with {} days buying): {}".format(MA[shorterMA], MA[longerMA], intc[BuyMA].sum(), intc.groupby([BuyMA])[ProfitMA].mean()[1]))
#print("In this period, as a comparison, after buying on {} trading days, the stock's average daily return is : {}".format(intc.shape[0]-1, intc['Return'].mean()))
numDaysWithRet = intc.shape[0]-1
print("In this period, as a comparison, after buying on {} trading days, the stock's average daily return is : {}".format(numDaysWithRet, intc['Return'].sum()/numDaysWithRet))
#and compare this to the market's average daily return in the same time frame, like SPY

print(intc.describe())
intc.to_csv("intc_profit.csv")

#more todo's
#instead of buying when MA10 is above MA50, how about just on the days MA10 cross over MA50
#also, how about MA of other #days, like MA = [10, 20, 30, 50, 100, 200] => 15 combos to try
#or MA_2n = [8, 16, 32, 64, 128, 256] => 15 combos to try
#can also try EMA as well (SMA above by using panda's .mean())

##################################################
# ML/NN
##################################################
#supervised learning - use past 100 days' close's for prediction, use 1st 80% of data as training set, rest as test set
#will try Recurrent Neural Networks (RNNs) in the future
numDaysWithRet = intc_withNA.shape[0]-1
numDays = intc_withNA.shape[0]
PERCENT_TRAINING = 80
LongMADuration = 100
firstDayForTraining = LongMADuration - 1
lastDayForTraining = int(numDaysWithRet * PERCENT_TRAINING / 100)
print("firstDayForTraining set to {}".format(firstDayForTraining))
print("lastDayForTraining set to {}".format(lastDayForTraining))
firstDayForTesting = lastDayForTraining + 1
lastDayForTesting = numDaysWithRet - 1 #due to 0 indexing
print("firstDayForTesting set to {}".format(firstDayForTesting))
print("lastDayForTesting set to {}".format(lastDayForTesting))
NNtraining = pd.DataFrame(index=[i for i in range(firstDayForTraining, lastDayForTraining + 1)])
print("NNtraning - index of 1st day for training is {}".format(NNtraining.index[0]))
print("NNtraning - index of last day for training is {}".format(NNtraining.index[-1]))

NNtesting = pd.DataFrame(index=[i for i in range(firstDayForTesting, lastDayForTesting + 1)])
print("NNtesting - index of 1st day for testing is {}".format(NNtesting.index[0]))
print("NNtesting - index of last day for testing is {}".format(NNtesting.index[-1]))

for j in range(LongMADuration):
    whichDay = "Day" + str(j+1)
    NNtraining[whichDay] = [0 for i in range(firstDayForTraining, lastDayForTraining + 1)]
    NNtesting[whichDay] = [0 for i in range(firstDayForTesting, lastDayForTesting + 1)]
    #seems like pandas requires setting this to be a list of MANY default values 1st ? empty list does NOT work
NNtraining['ReturnPositive'] = [0 for i in range(firstDayForTraining, lastDayForTraining + 1)]
NNtesting['ReturnPositive'] = [0 for i in range(firstDayForTesting, lastDayForTesting + 1)]
print("shape of NNtraining is {}".format(NNtraining.shape))
print("shape of NNtesting is {}".format(NNtesting.shape))

trainingIdx = 0
print("1st closing price of the training data used is {}".format(intc_withNA.iloc[firstDayForTraining - LongMADuration + 1, CloseIdx]))
for i in range(firstDayForTraining, lastDayForTraining + 1):
    if i%100 == 0:
        print('.', end='', flush=True)
    if i%1000 == 0:
        print("preparing training data ... start of loop for i of {}".format(i))
    DayCol = 0
    for j in range(i - LongMADuration + 1, i+1):
        NNtraining.iloc[trainingIdx, DayCol] = intc_withNA.iloc[j, CloseIdx]
        ''' for debug only
        if trainingIdx == 0:
            print("trainingidx is {}, DayCol is {} and NNtraining.iloc[trainingIdx, DayCol] is {}".format(trainingIdx, DayCol, NNtraining.iloc[trainingIdx, DayCol]))
            print("Day1 column is {}".format(NNtraining['Day1']))
            exit()
        '''
        DayCol += 1
    NNtraining.iloc[trainingIdx, LongMADuration] = 1 if intc_withNA.iloc[i]['Return'] > 0 else 0 #for ReturnPositive
    trainingIdx += 1
    #if i > (lastDayForTraining - 100): # this is for debug only
        #print("end of loop for i of {}".format(i))

testingIdx = 0
print("1st closing price of the testing data used is {}".format(intc_withNA.iloc[firstDayForTesting - LongMADuration + 1, CloseIdx]))
for i in range(firstDayForTesting, lastDayForTesting + 1):
    if i%100 == 0:
        print('.', end='', flush=True)
    if i%1000 == 0:
        print("preparing testing data ... start of loop for i of {}".format(i))
    DayCol = 0
    for j in range(i - LongMADuration + 1, i+1):
        NNtesting.iloc[testingIdx, DayCol] = intc_withNA.iloc[j, CloseIdx]
        DayCol += 1
    NNtesting.iloc[testingIdx, LongMADuration] = 1 if intc_withNA.iloc[i]['Return'] > 0 else 0 #for ReturnPositive
    testingIdx += 1

print("printing for debug purpose:")
print("Day1 column for NNtraining is:\n{}".format(NNtraining['Day1']))#for debug, 1st item should still be 0.325521, INTC close price on 3/17/1980
print("Day1 column for NNtesting is:\n{}".format(NNtesting['Day1']))#for debug

print(NNtraining.describe())
print("NN training set's shape is ".format(NNtraining.shape))
NNtraining.to_csv("NNtraining.csv")
print(NNtesting.describe())
print("NN testing set's shape is ".format(NNtesting.shape))
NNtesting.to_csv("NNtesting.csv")

#####################################################################################
# NN - would try RNN in the future, data preparation above would need to be modified
#####################################################################################

import os
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Pull out columns for X (data to train with) and Y (value to predict)
X_training = NNtraining.drop('ReturnPositive', axis=1).values
Y_training = NNtraining[['ReturnPositive']].values
#for debug only:
print(X_training.shape)
print(Y_training.shape)
#X_training.to_csv("X_training.csv")
#Y_training.to_csv("Y_training.csv")

# Pull out columns for X (data to train with) and Y (value to predict)
X_testing = NNtesting.drop('ReturnPositive', axis=1).values
Y_testing = NNtesting[['ReturnPositive']].values

# All data needs to be scaled to a small range like 0 to 1 for the neural
# network to work well. Create scalers for the inputs and outputs.
X_scaler = MinMaxScaler(feature_range=(0, 1))
Y_scaler = MinMaxScaler(feature_range=(0, 1))

# Scale both the training inputs and outputs
X_scaled_training = X_scaler.fit_transform(X_training)
Y_scaled_training = Y_scaler.fit_transform(Y_training)

# It's very important that the training and test data are scaled with the same scaler.
X_scaled_testing = X_scaler.transform(X_testing)
Y_scaled_testing = Y_scaler.transform(Y_testing)

# Define model parameters
RUN_NAME = "run 1 with 100/100/50 nodes"
learning_rate = 0.001
training_epochs = 100

# Define how many inputs and outputs are in our neural network
number_of_inputs = 100
number_of_outputs = 1

# Define how many neurons we want in each layer of our neural network
layer_1_nodes = 100
layer_2_nodes = 100
layer_3_nodes = 50

# NN - Section One: Define the layers of the neural network itself
# Input Layer
#'''
with tf.variable_scope('input'):
    X = tf.placeholder(tf.float32, shape=(None, number_of_inputs))

# Layer 1
with tf.variable_scope('layer_1'):
    weights = tf.get_variable("weights1", shape=[number_of_inputs, layer_1_nodes], initializer=tf.contrib.layers.xavier_initializer())
    biases = tf.get_variable(name="biases1", shape=[layer_1_nodes], initializer=tf.zeros_initializer())
    layer_1_output = tf.nn.relu(tf.matmul(X, weights) + biases)

# Layer 2
with tf.variable_scope('layer_2'):
    weights = tf.get_variable("weights2", shape=[layer_1_nodes, layer_2_nodes], initializer=tf.contrib.layers.xavier_initializer())
    biases = tf.get_variable(name="biases2", shape=[layer_2_nodes], initializer=tf.zeros_initializer())
    layer_2_output = tf.nn.relu(tf.matmul(layer_1_output, weights) + biases)

# Layer 3
with tf.variable_scope('layer_3'):
    weights = tf.get_variable("weights3", shape=[layer_2_nodes, layer_3_nodes], initializer=tf.contrib.layers.xavier_initializer())
    biases = tf.get_variable(name="biases3", shape=[layer_3_nodes], initializer=tf.zeros_initializer())
    layer_3_output = tf.nn.relu(tf.matmul(layer_2_output, weights) + biases)

# Output Layer
with tf.variable_scope('output'):
    weights = tf.get_variable("weights4", shape=[layer_3_nodes, number_of_outputs], initializer=tf.contrib.layers.xavier_initializer())
    biases = tf.get_variable(name="biases4", shape=[number_of_outputs], initializer=tf.zeros_initializer())
    prediction = tf.matmul(layer_3_output, weights) + biases

# Section Two: Define the cost function of the neural network that will measure prediction accuracy during training

with tf.variable_scope('cost'):
    Y = tf.placeholder(tf.float32, shape=(None, 1))
    cost = tf.reduce_mean(tf.squared_difference(prediction, Y))

# Section Three: Define the optimizer function that will be run to optimize the neural network

with tf.variable_scope('train'):
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

# Create a summary operation to log the progress of the network
with tf.variable_scope('logging'):
    tf.summary.scalar('current_cost', cost)
    summary = tf.summary.merge_all()

saver = tf.train.Saver()

# Initialize a session so that we can run TensorFlow operations
with tf.Session() as session:

    # Run the global variable initializer to initialize all variables and layers of the neural network
    session.run(tf.global_variables_initializer())

    # Create log file writers to record training progress.
    # We'll store training and testing log data separately.
    training_writer = tf.summary.FileWriter('./logs/training', session.graph)
    testing_writer = tf.summary.FileWriter('./logs/testing', session.graph)

    # Run the optimizer over and over to train the network.
    # One epoch is one full run through the training data set.
    for epoch in range(training_epochs):

        # Feed in the training data and do one step of neural network training
        session.run(optimizer, feed_dict={X: X_scaled_training, Y: Y_scaled_training})

        # Every 5 training steps, log our progress
        if epoch % 5 == 0:
            # Get the current accuracy scores by running the "cost" operation on the training and test data sets
            training_cost, training_summary = session.run([cost, summary], feed_dict={X: X_scaled_training, Y:Y_scaled_training})
            testing_cost, testing_summary = session.run([cost, summary], feed_dict={X: X_scaled_testing, Y:Y_scaled_testing})

            # Write the current training status to the log files (Which we can view with TensorBoard)
            training_writer.add_summary(training_summary, epoch)
            testing_writer.add_summary(testing_summary, epoch)

            # Print the current training status to the screen
            print("Epoch: {} - Training Cost: {}  Testing Cost: {}".format(epoch, training_cost, testing_cost))

    # Training is now complete!

    # Get the final accuracy scores by running the "cost" operation on the training and test data sets
    final_training_cost = session.run(cost, feed_dict={X: X_scaled_training, Y: Y_scaled_training})
    final_testing_cost = session.run(cost, feed_dict={X: X_scaled_testing, Y: Y_scaled_testing})

    print("Final Training cost: {}".format(final_training_cost))
    print("Final Testing cost: {}".format(final_testing_cost))
    
#save_path = saver.save(session, "logs/trained_model.ckpt")
#print("Model saved: {}".format(save_path))
#'''

#even more todo's
#can extend using data beyond close prices
#other stocks, like csco, msft, ibm, ge, etc etc

print("\nEnd of Program reached!!")
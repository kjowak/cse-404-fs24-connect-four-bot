# cse-404-fs24-connect-four-bot
This is a class project for CSE 404 at Michigan State University, in which we will try to train a bot to player Connect Four using machine learning techniques

What is the setting of your project? is it supervised, unsupervised, or semisupervised? (I think everybody got supervision for this class though). 
    This model is supervised learning as it is being trained on labeled data representing the game state win, tie, or loss.

How you represent X (Features/Representation  and their explanation, justification)
    42 features of all the positions on a connect-4 board, either 1,0,-1, representing user 1, blank, user 2. A label of who won/lost the game is also inputted.
How do you represent Y (binary? multi-class? sequences? trees? graphs?)
    Y is a multi-classification, and can be -1,0,1  player 1 won, representing a tie, or player 2 won. 


Which libraries you will use?
    scikit-learn
    pandas
    torch
    numpy
    matplotlib
    juypiter




Results!!!!

Multilayer Perceptron models:

1. Simple 3 linear layer model:
    Epoch [10/50], Loss: 0.2390
    Epoch [20/50], Loss: 0.2356
    Epoch [30/50], Loss: 0.2293
    Epoch [40/50], Loss: 0.2197
    Epoch [50/50], Loss: 0.2090
    Loss on test set: 0.2404

    This model does not show much learning, Evaluating test set showed worse results then even the test set.

2. 9 linear layer model:
    Epoch [10/50], Loss: 0.2407
    Epoch [20/50], Loss: 0.2283
    Epoch [30/50], Loss: 0.2018
    Epoch [40/50], Loss: 0.1824
    Epoch [50/50], Loss: 0.1624
    Loss on test set: 0.1609

    This model actually demonstrated some learning. The test set showed imporved results with more observations and evaulating against the test set showed relativly low loss.

3. Simple CNN:
    Epoch [10/50], Loss: 0.2338
    Epoch [20/50], Loss: 0.2062
    Epoch [30/50], Loss: 0.1843
    Epoch [40/50], Loss: 0.1711
    Epoch [50/50], Loss: 0.1572
    Loss on test set: 0.1565

    This model seemed to show the best learning, loss went way down and the test set preformed very well with this model. While it still needs some work this method is very promising.




Reinforcement Learning Models:
    1. Simple Reinforcement Learning:
       - Learns by playing against a random moves,
         this bot learns by a reward system where it gets:
         - +10 points whenever it wins
         - -10 points when it loses
         - +5 points whenever it blocks an opponents 3 in a row
         - +1 whenever it ties
   2. DQN Approach:
      - Learns in the same way as the other model
      - Includes a Dueling DQN which separates value and advantage streams,
        which should be more efficient
   Both of these models train againt random moves-- as such, they learned the same strategy
   of placing in the same column repetatively as it is unlikely that the opponent will do anything
   to block it. In order to improve them before the final code, I will need to rework the reward system
   as well as make the bot it plays against be a little more intellegent.
   

Team Memebers:
Will Bray-Cotton
Joseph Khalaf
Kyle Nowak
Adam Cooper
Riley Moorman


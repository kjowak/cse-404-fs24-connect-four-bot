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

    This model seemed to show the best learning, loss went way down and the test set preformed very well with this model. While it still needs some work this method is very promising.




Team Memebers:
Will Bray-Cotton
Joseph Khalaf
Kyle Nowak
Adam Cooper
Riley Moorman

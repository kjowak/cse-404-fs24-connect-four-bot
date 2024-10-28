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

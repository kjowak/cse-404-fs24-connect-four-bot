# cse-404-fs24-connect-four-bot
This is a class project for CSE 404 at Michigan State University, in which we will try to train a bot to player Connect Four using machine learning techniques

What is the setting of your project? is it supervised, unsupervised, or semisupervised? (I think everybody got supervision for this class though). 
    This model is supervised learning as it is being trained on labeled data representing the game state win, tie, or loss.

How you represent X (Features/Representation  and their explanation, justification)
    42 features of all the positions on a connect-4 board, either 1,0,-1, representing user 1, blank, user 2. A label of who won/lost the game is also inputted.
How do you represent Y (binary? multi-class? sequences? trees? graphs?)
    Y is a multi-classification, and can be an integer 0-6 representing which move is the best to play in a given scenerio. 

Which libraries you will use?
    scikit-learn
    pandas
    torch
    numpy
    matplotlib
    juypiter

What types of models did we create?
1. CNN
2. MLP
3. SVM
4. Decision Tree
5. Reinforcement Learning

**CNN Model:**
How It's Made:
    - Built using convolutional neural networks.
    - Consists of:
        - 3 convolutional layers with tanh activation functions.
        - Each convolutional layer uses a 3x3 filter with padding='same' to preserve spatial dimensions.
        - 2 MaxPooling2D layers to downsample feature maps (pool size: 2x2).
        - 1 fully connected dense layer with 64 units and tanh activation.
        - A Dropout layer with 50% dropout rate for regularization.
    - Optimizer: Adam with a learning rate of 0.0001.
    - Loss Function: Categorical Crossentropy for multiclass classification.
    - Epochs: 100.
Results:
    - Training Accuracy: 87%.
    - Testing Accuracy: 84%.

**MLP Model**
How It's Made:
    - Built using a fully connected Multilayer Perceptron (MLP).
    - Consists of:
        - An input layer to process the flattened 42-cell Connect-4 board.
        - 2 hidden layers with:
            - 128 units in the first layer and 64 units in the second layer.
            - tanh activation for both layers.
        - A Dropout layer after each hidden layer with a 50% dropout rate for regularization.
        - An output layer with 7 units (one for each possible move) and softmax activation.
    - Optimizer: Adam with a learning rate of 0.0001.
    - Loss Function: Categorical Crossentropy for multiclass classification.
    - Epochs: 100.
Results:
    - Training Accuracy: 73%.
    - Testing Accuracy: 70%.


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


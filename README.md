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

NOTE: You can play against all of these models (except reinforcement learning) in the Play Game file.
NOTE: You can play against each reinforcement model in the Connect4_Reinforcement_Learning file.

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
    - Training Accuracy: 70.4%.
    - Testing Accuracy: 70.1%.

**SVM Model**
How It's Made:
    - Built using a support vector machine (SVM)
    - Hyperparameters:
        - Kernels of linear, polynomial, and rbf
        - C values of 0.01, 0.1, 1, 10
    - Loss Function: Hinge Loss function
Best Hyperparameters:
    - C = 10
    - Kernel = rbf
Results:
    - Training Accuracy: 97.37%
    - Testing Accuracy: 81.55%

**Decision Tree Model**
How It's Made:
    - Built using a Decision Tree Classifier
    - Hyperparameters: 
        - Gini, Entropy
        - Maximum Depth of Tree: None, 10, 20,30,40,50
        - Minimum number of samples to split a node: 2, 5, 10
        - Minimum number of sample leafs: 1, 2, 4
    - Loss functions: Gini & Entropy
Best Hyperparameters:
    - Gini
    - Max Depth: 20
    - Minimum Samples Leaf: 4
    - Min Samples Split: 10
Results:
    - Training Accuracy: 87.48%
    - Test Accuracy: 79.48%

**Reinforcement Learning Models**
How It's Made:
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
   3. Heuristic Opponent
      - Similar to Model 1, but instead of playing against random moves it plays against a smarter opponent
      - The opponent will now:
        - Play a move that gets 4 in a row when available
        - Block the bot's 4 in a row
        - If none of the moves do one of those two, it will play a random move
   4. Self-Play
      - Same rewards as model 1, but instead of playing against a random bot it will play against itself
Results:
   - Models 1 and 2 learned to stack on top of themselves repetatively. 
        - This is likely due to the opponent bot playing random moves, so by stacking repetatively it is very unlikely they will lose.
   - Model 3 plays mostly random moves. 
        - This is because the initial bot is too difficult. It does not get the opportunity to learn what will win as it gets blocked every time.
   - Model 4 Is the best model, it plays mostly random moves as well but with more time to train will likely be decent at playing.

Team Memebers:
Will Bray-Cotton
Joseph Khalaf
Kyle Nowak
Adam Cooper
Riley Moorman


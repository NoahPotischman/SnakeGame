# SnakeGame
A pixel version of googles snake game. 

Things to note:
1. The snake must eat one initial peice of food, then a second peice in order for the snake to grow by one. However, this is only the case for the first segment. Once the snake is composed of one white and one green square, it will grow as normal. The reason for this should be that because the head of the snake is always white, the code starts the green portion of the snake from inside the white square. The two reasons for the snake head being white were, #1 It can get hard to tell what is or isn't the head when the snake gets long, #2 I intended to using q-learning to automate it but decided not to. (This is important because the AI would think in single frames without memory. So, in theory, if the head wasn't white and an AI tried to play, the AI wouldn't know where the snakes head was, preventing it from learning) <--- According to my understanding

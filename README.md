# MineSweeper
Minesweeper is a one-player puzzle game. This game consists of a square (or rectangular) shaped board in which mines are placed in some of its houses. First, all the houses are hidden and the player has to find all the mines. In each move we can reveal a house that we guess does not contain mines. If our guess is correct, the total number of mines in neighboring houses will be displayed. If we mistakenly reveal houses that contain mines, we will lose the game. During the game, we mark the houses that we think contain mines with flags. If we can find all the mines on the screen correctly, we will win the game.
To implement the game, we need to store the information of the table houses. For example, the presence of mines, the presence of flags, whether they are visible or hidden, or others are all different characteristics about houses that should be saved in such a way.
In this code, for example, the board variable is used to maintain the state of the houses in terms of revealing and placing the flag. For instance, each house of this table can contain the number 0 meaning hidden, 1 meaning revealed, and 2 meaning placing the flag. The mines variable is also used to store mine locations.

Hints:
a)'#' character is sign of a house without a flag. 
b)'p' character is sign of a house with a flag.
c)'@' character is sign of a house with a mine.

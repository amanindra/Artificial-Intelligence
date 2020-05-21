Assignment completed by Manindra Kumar Anantaneni (mxa180038)

Implemented using Python 3

Requires Python 3.4 and above

The folder consists of main.py, output.txt, and readme.txt

Instructions:
    i. cd to the folder where main.py is present
    ii. execute the following command : 
        $ python3 main.py args   
            args can be 
                -> bfs (for breadth first search)
                -> ids (for iterative deepening)
                -> astar1 (for A* with heuristic1)
                -> astar2 (for A* with heuristic2)
        eg:
        $ python3 main.py bfs
    iii. input numbers in the range 1 to 8 (inclusive) and * to represent the empty tile, without any repititions, line by line
    eg:
    $ python3 main.py bfs
    *
    1
    3
    4
    2
    5
    7
    8
    6

    iv. Output contains the total number of states explored, the number of moves taken, and the sequence of the tiles to reach the goal node
    Sample output:
    States explored: 14
    Path to goal: 
      ⇓  
    * 1 3 
    4 2 5 
    7 8 6 
      ⇓  
    1 * 3 
    4 2 5 
    7 8 6 
      ⇓  
    1 2 3 
    4 * 5 
    7 8 6 
      ⇓  
    1 2 3 
    4 5 * 
    7 8 6 
      ⇓  
    1 2 3 
    4 5 6 
    7 8 * 
    Total No. of Moves: 4
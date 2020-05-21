# from __future__ import annotations
from enum import Enum
from collections import deque
import queue
import sys
import argparse
# from typing import List, Tuple


class Action(Enum):
    up = 1
    down = 2
    left = 3
    right = 4

class Node:
    """ Datastructure to store the state, depth, path cost, depth and parent """
    # def __init__(self, state: Tuple[Tuple[int]], path_cost : int, parent: Node, action : Action = None) -> Node:
    def __init__(self, state, path_cost, depth, parent, action=None):
        """ Initialize the object"""
        self.state = state
        self.__depth = depth
        self.__total_cost = path_cost
        self.parent = parent
        self.__action = action
        self.__empty_tile = []

    def set_depth(self, depth):
        self.__depth = depth
    
    def get_depth(self):
        return self.__depth
    
    def set_total_cost(self, cost):
        self.__total_cost = cost

    def get_total_cost(self):
        return self.__total_cost

    # def set_empty_tile(self, row : int, column : int):
    def set_empty_tile(self, row, column):
        self.__empty_tile.append(row)
        self.__empty_tile.append(column)
 
    # def get_empty_tile(self) -> List[int]:
    def get_empty_tile(self):
        return self.__empty_tile
    
    def __lt__(self, value):
        return self.__total_cost <= value.__total_cost

    def __str__(self):
        return ("State: {} \n Path Cost: {} \n Depth: {} \n Empty_tile: {}".format(self.state, self.__total_cost, self.__depth, self.__empty_tile))


# def goal_test(state : Tuple[Tuple[int]]) -> bool:
def goal_test(state):
    """ To check if the state has reached the goal node
        1 2 3
        4 5 6
        7 8 *
    """
    for i in range(0, 8) :
        input_tile = state[i//3][i%3]
        goal_tile = str(i+1)
        if input_tile != goal_tile :
            return False
    return True

# def clone_parent_state(parent_state : Tuple[Tuple[int]]) -> Tuple[Tuple[int]]:
def clone_parent_state(parent_state):
    """ Return a clone of the parent state""" 
    return parent_state

# def generate_child_node(parent : Node, action : Action) -> Node :
def generate_child_node(parent, action):
    """
    Generate child nodes for each of the Up, Down, Left, Right actions with appropriate depth, and cost
    """
    parent_empty_tile = parent.get_empty_tile()
    if (parent_empty_tile[0] == 0 and action == Action.up.name) or (parent_empty_tile[0] == 2 and action == Action.down.name) or (parent_empty_tile[1] == 0 and action == Action.left.name) or (parent_empty_tile[1] == 2 and action == Action.right.name):
        return None
    child_empty_tile_row = 0
    child_empty_tile_column = 0
    parent_state = parent.state
    child_state = clone_parent_state(parent_state)
    tile = ""
    if action is Action.up.name:
        tile = parent_state[parent_empty_tile[0] - 1][parent_empty_tile[1]]
        tempList = [list(cs) for cs in child_state]
        tempList[parent_empty_tile[0] - 1][parent_empty_tile[1]] = "*"
        child_state = tuple(tuple(ts) for ts in tempList)
        child_empty_tile_row = parent_empty_tile[0] - 1
        child_empty_tile_column = parent_empty_tile[1]
    elif action is Action.down.name:
        tile = parent_state[parent_empty_tile[0] + 1][parent_empty_tile[1]]
        tempList = [list(cs) for cs in child_state]
        tempList[parent_empty_tile[0] + 1][parent_empty_tile[1]] = "*"
        child_state = tuple(tuple(ts) for ts in tempList)
        child_empty_tile_row = parent_empty_tile[0] + 1
        child_empty_tile_column = parent_empty_tile[1]
    elif action is Action.left.name:
        tile = parent_state[parent_empty_tile[0]][parent_empty_tile[1] - 1]
        tempList = [list(cs) for cs in child_state]
        tempList[parent_empty_tile[0]][parent_empty_tile[1] - 1] = "*"
        child_state = tuple(tuple(ts) for ts in tempList)
        child_empty_tile_row = parent_empty_tile[0]
        child_empty_tile_column = parent_empty_tile[1] - 1
    else:
        tile = parent_state[parent_empty_tile[0]][parent_empty_tile[1] + 1]
        tempList = [list(cs) for cs in child_state]
        tempList[parent_empty_tile[0]][parent_empty_tile[1] + 1] = "*"
        child_state = tuple(tuple(ts) for ts in tempList)
        child_empty_tile_row = parent_empty_tile[0]
        child_empty_tile_column = parent_empty_tile[1] + 1
    tempList = [list(cs) for cs in child_state]
    tempList[parent_empty_tile[0]][parent_empty_tile[1]] = tile
    child_state = tuple(tuple(ts) for ts in tempList)
    child = Node(child_state, parent.get_total_cost() + 1, parent.get_depth() + 1, parent, action)
    child.set_empty_tile(child_empty_tile_row, child_empty_tile_column)
    return child

# def get_goal() -> Dict[str, List[int]]:
def get_goal():
    """
    Return a dictionary conatining the postion ([row, column]) of the tiles as present in goal Node
    {
        "1" : [0, 0], "2" : [0, 1], "3" : [0, 2], "4" : [1, 0], "5" : [1, 1], "6" : [1, 2], "7" : [2, 0], "8" : [2, 1], "*" : [2, 2]
    }
    """
    goal = {}
    for i in range(0, 8):
        tile = []
        tile.append(i//3)
        tile.append(i%3)
        goal.update({str(i + 1) : tile})
    return goal

# def is_state_present(state: Tuple[Tuple[int]], q : deque) -> bool:
def is_state_present(state, q):
    """To check if the state is already in the queue """
    for n in q:
        if state == n.state:
            return True
    return False

# def print_path_to(node: Node):
def print_path_to(node):
    """To print the path to a node"""
    if node is None:
        return
    print_path_to(node.parent)
    node_state = node.state
    print("  ⇓  ")
    for row in node_state:
        for column in row:
            print("{}".format(column), end = " ")
        print("", end = "\n")

# def print_output(goal_node : Node):
def print_output(node):
    """To print the output"""
    print("Path to goal: ")
    print_path_to(node)
    print("Total No. of Moves: {}".format(node.get_depth()))
    

# def breadth_first_search(input: Node) -> int:
def breadth_first_search(input):
    """
    To perform a breadth first search on the input node
    input: Node input
    returns 1 if a goal node is found, else returns -1
    """
    if goal_test(input.state):
        print_output(input)
        return 1
    q = deque()
    q.append(input)
    explored = set()
    while q:
        elem = q.popleft()
        if elem.get_depth() < 10:
            explored.add(elem.state)
            for action, member in Action.__members__.items():
                child = generate_child_node(elem, action)
                if child is not None and not explored.__contains__(child.state) and not is_state_present(child.state, q):
                    if goal_test(child.state):
                        print("States explored: {}".format(len(explored)))
                        print_output(child)
                        return 1
                    q.append(child)
    print("Failed to find goal state")
    return -1

# def depth_limited_search(input: Node, depth: int) -> Node :
def depth_limited_search(input, depth, states_explored):
    """
    To perform a depth first search on the input node upto a depth of specified
    input: Node input, int depth
    returns goal node if a goal node is found, else returns None
    """
    if goal_test(input.state):
        return input
    elif input.get_depth() == depth:
        return None
    else:
        states_explored[0] += 1
        for action, member in Action.__members__.items():
            child = generate_child_node(input, action)
            temp = None
            if child is not None:
                temp = depth_limited_search(child, depth, states_explored)
            if temp is not None:
                return temp
        return None

# def iterative_deepening_search(input: Node) -> int:
def iterative_deepening_search(input):
    """
    To perform a depth first search on the input node by increasing the depth considered
    input: Node input
    output: returns 1 if searcj is success, else returns -1
    """
    states_explored = [0]
    for i in range(0, 11):
        result = depth_limited_search(input, i, states_explored)
        if result is not None:
            print("No. of states explored/enqueued: {}".format(states_explored))
            print_output(result)
            return 1
        print("IDS failed to find goal at depth: {}".format(i))
    print("Failed to find goal state")
    return -1

# Heuristic 1
# def no_of_tiles_misplaced(game_state : Tuple[Tuple[int]]) -> int
def no_of_tiles_misplaced(state):
    """
    Return the number of misplaced tiles in the input state
    """
    tiles_misplaced = 0
    input_tile = ""
    for i in range(0, 8):
        input_tile = state[i//3][i%3]
        if input_tile != "*" and input_tile != str(i + 1) :
            tiles_misplaced+=1
    input_tile = state[2][2]
    if input_tile != "*":
        tiles_misplaced+=1
    return tiles_misplaced

# Heuristic 2
# def manhattan_distance(game_state : Tuple[Tuple[int]]) -> int
def manhattan_distance(game_state):
    """
    Returns the manhattan distance of the tiles from their intended goal position
    """
    manhattan_dist = 0
    goal = get_goal()
    for i in range(0, 9):
        input_tile = game_state[i//3][i%3]
        if input_tile != "*":
            goal_tile = goal[input_tile]
            manhattan_dist += abs(goal_tile[0] - i//3) + abs(goal_tile[1] - i%3)
    return manhattan_dist

def astar(input, algoName):
    """
    Perform A* search on the input
    returns 1 if success, else -1
    """
    if goal_test(input.state):
        print_output(input)
        return 1
    states_explored = 0
    pq = queue.PriorityQueue()
    pq.put(input)
    optimal_cost = sys.maxsize
    elem_total_cost = 0
    optimal_goal_node = None
    while True:
        elem = pq.get()
        # print(elem)
        # print(no_of_tiles_misplaced(elem.state))
        elem_total_cost = elem.get_total_cost()
        if elem_total_cost >= optimal_cost:
            break
        if elem.get_depth() < 10:
            states_explored += 1
            for action, member in Action.__members__.items():
                child = generate_child_node(elem, action)
                if child is not None:
                    heuristic_cost = no_of_tiles_misplaced(child.state) if algoName == "astar1" else manhattan_distance(child.state)
                    child_total_cost = child.get_depth() + heuristic_cost
                    child.set_total_cost(child_total_cost)
                    if goal_test(child.state):
                        optimal_cost = child.get_total_cost()
                        optimal_goal_node = child
                    else:
                        pq.put(child)
        if pq.empty():
            break
    if optimal_goal_node is not None:
        print("No. of states explored/enqueued: {}".format(states_explored))
        print_output(optimal_goal_node)
        return 1
    return -1


# def astar1(input: Node) -> int:
def astar1(input):
    """
    Perform A* search using the heuristic, Number of Misplaced Tiles
    """
    input.set_total_cost(no_of_tiles_misplaced(input.state))
    if astar(input, "astar1") == -1:
        print("Failed to find goal using A* (Heuristic 1) Search")

def astar2(input):
    """
    Perform A* search using the heuristic, Manhattan Distance
    """
    input.set_total_cost(manhattan_distance(input.state))
    if astar(input, "astar2") == -1:
        print("Failed to find goal using A* (Heuristic 2) Search")
  
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("algo", help = """Please provide an argument for the type of algorithm 
                                            \n bfs for Breadth First Search
                                            \n ids for ityerative Deepening
                                            \n astar1 for A* Algo using Heuristic 1
                                            \n asatr2 for A* Algo using Heuristic 2
    """)
    args = parser.parse_args()
    input_state = ()
    for i in range(0,3):
        row = ()
        for j in range(0,3):
            inp = input()
            if(inp == "*"):
                empty_tile_row = i
                empty_tile_column = j
            row+=(inp,)
        input_state+=(row,)
    start = Node(input_state, 0, 0, None)
    start.set_empty_tile(empty_tile_row, empty_tile_column)
    print
    if(args.algo == "bfs"):
        breadth_first_search(start)
    elif(args.algo == "ids"):
        iterative_deepening_search(start)
    elif(args.algo == "astar1"):
        astar1(start)
    elif(args.algo == "astar2"):
        astar2(start)
    else:
        print("Please check the arguments")



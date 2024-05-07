# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    stack = util.Stack()
    current_state = problem.getStartState()
    current_path = []
    visited_state = [current_state]
    curr = (current_state, current_path) 
    
    while True:
        if not(problem.isGoalState(curr[0])):
            successors = problem.getSuccessors(curr[0])
            for successor in successors:
                state = successor[0]

                if (state in visited_state):
                    continue

                
                path = curr[1] + [successor[1]]
                stack.push((state, path))
            
            ## Geting the node to travel
            while(True):
                current_node = stack.pop()
                current_state = current_node[0]
                current_path = current_node[1]
                curr = (current_state, current_path) 
                if(current_state not in visited_state):
                    visited_state.append(current_state)
                    break
                elif stack.isEmpty():
                    break
            
        elif stack.isEmpty():
            break
        else:
            break
    return(curr[1])



def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    current_state = problem.getStartState()
    current_path = []
    visited_state = [current_state]
    curr = (current_state, current_path) 
    
    while True:
        if not(problem.isGoalState(curr[0])):
            successors = problem.getSuccessors(curr[0])
            for successor in successors:
                state = successor[0]
                if (state in visited_state):
                    continue

                
                path = curr[1] + [successor[1]]
                queue.push((state, path))
            
            ## Geting the node to travel
            while(True):
                current_node = queue.pop()
                current_state = current_node[0]
                current_path = current_node[1]
                curr = (current_state, current_path) 
                if(current_state not in visited_state):
                    visited_state.append(current_state)
                    break
                elif queue.isEmpty():
                    break
            
            
        elif queue.isEmpty():
            break
        else:
            break
        
    return(curr[1])


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    current_state = problem.getStartState()
    current_path = []
    current_cost = 0
    visited_state = [current_state]
    curr = (current_state, current_path, current_cost) 
    
    while True:
        if not(problem.isGoalState(curr[0])):
            successors = problem.getSuccessors(curr[0])
            # print(successors)
            for successor in successors:
                state = successor[0]

                if (state in visited_state):
                    continue

                
                path = curr[1] + [successor[1]]
                score = curr[2] + successor[2]
                # print(score)
                priority_queue.push((state, path, score), score)
            
            ## Expanding the node to travel
            while(True):
                current_node = priority_queue.pop()
                current_state = current_node[0]
                current_path = current_node[1]
                current_score = current_node[2]
                curr = (current_state, current_path, current_score) 
                if(current_state not in visited_state):
                    visited_state.append(current_state)
                    break
                elif priority_queue.isEmpty():
                    break
            
            
        elif priority_queue.isEmpty():
            break
        else:
            break
        
    return(curr[1])
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def priority_func(item:tuple, problem, heuristic = nullHeuristic):
    priority  = heuristic(item[0], problem)
    priority = item[2] + priority
    return priority

        
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    current_state = problem.getStartState()
    current_path = []
    current_cost = 0
    visited_state = [current_state]
    curr = (current_state, current_path, current_cost) 
    
    while True:
        if not(problem.isGoalState(curr[0])):
            successors = problem.getSuccessors(curr[0])
            # print(successors)
            for successor in successors:
                state = successor[0]

                if (state in visited_state):
                    continue

                
                path = curr[1] + [successor[1]]
                score = curr[2] + successor[2]
                # print(score)
                item = (state, path ,score)
                priority_queue.update(item, priority=priority_func(item, problem, heuristic))
            
            ## Expanding the node to travel
            while(True):
                current_node = priority_queue.pop()
                current_state = current_node[0]
                current_path = current_node[1]
                current_score = current_node[2]
                curr = (current_state, current_path, current_score) 
                if(current_state not in visited_state):
                    visited_state.append(current_state)
                    break
                elif priority_queue.isEmpty():
                    break
            
            
        elif priority_queue.isEmpty():
            break
        else:
            break
        
    return(curr[1])
    
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

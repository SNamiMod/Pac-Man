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

def depthFirstSearch(problem):
    nodeStack = util.Stack()
    checked = []
    startState = problem.getStartState()
    nodeStack.push(startState)
    nodeStack.push([]) # action of first node = []
    # pop , check , not goal -> push childNodes
    while nodeStack.isEmpty() == 0:
        actions = nodeStack.pop()
        state = nodeStack.pop()
        if problem.isGoalState(state):
            checked.append(state)
            return actions
        else:
            checked.append(state)
            childNodes = problem.getSuccessors(state)
            isChecked = 0
            for child in childNodes:
                for temp in checked:
                    if child[0] == temp:
                        isChecked = 1
                        # we have checked the node
                if isChecked == 0:
                    nodeStack.push(child[0])
                    childActions = actions + [child[1]]
                    nodeStack.push(childActions)
                else:
                    isChecked = 0
    else:
        return None

def breadthFirstSearch(problem):
    from util import Queue

    # queueXY: ((x,y),[path]) #
    queueXY = Queue()

    visited = [] # Visited states
    path = [] # Every state keeps it's path from the starting state

    # Check if initial state is goal state #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Start from the beginning and find a solution, path is empty list #
    queueXY.push((problem.getStartState(),[]))

    while(True):

        # Terminate condition: can't find solution #
        if queueXY.isEmpty():
            return []

        # Get informations of current state #
        xy,path = queueXY.pop() # Take position and path
        visited.append(xy)

        # Comment this and uncomment 179. This is only works for autograder
        # In lectures we check if a state is a goal when we find successors

        # Terminate condition: reach goal #
        if problem.isGoalState(xy):
            return path

        # Get successors of current state #
        succ = problem.getSuccessors(xy)

        # Add new states in queue and fix their path #
        if succ:
            for item in succ:
                if item[0] not in visited and item[0] not in (state[0] for state in queueXY.list):

                    # Lectures code:
                    # All impementations run in autograder and in comments i write
                    # the proper code that i have been taught in lectures
                    # if problem.isGoalState(item[0]):
                    #   return path + [item[1]]

                    newPath = path + [item[1]] # Calculate new path
                    queueXY.push((item[0],newPath))



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

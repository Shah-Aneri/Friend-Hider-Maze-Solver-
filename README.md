# Friend-Hider-Maze-Solver-

Hide Friends problem:- The aim of this program is to place the friends such that no two of them can see each other.
State Space:-Any N*M size board with arrangements of buildings(&), Luddy hall(@) and number of friends(F)

Initial State:- Board map with sidewalks and buildings without any friends placed on it.

Goal State:- Board with the placement of N number of friends such that their view is obscured by the buildings and they cannot see each other.

Successor Function:- Search for all possible arrangements of friends and place one more friend than previous state.

Cost Path:- Here, we are focused on finding the solution to place the friends on the board irrespective of the path cost as it requires to check all the necessary cells on the board and recur back if the arrangement hinders the constraints and so path is not considered much. But the algorithm that is used should be strong enough to give faster solutions.

If it’s not possible to place a friend on the board then it returns None.

Explaination:- I have used DFS algorithm to solve the problem. Here the search starts with the initial board and checks for the place in the row and column where friend can be placed and if there is already any friend in the previous row or the previous column then the successor function will skip that position and find for other suitable position. While solving the problem, as I proceeded with solving the possibilities that come to my mind of placing the friends and changing the map file with a large size map, I faced challenges to solve that using a proper logic. So for that I tried all different ways of solving it using backtracking and checking explicitly for first rows and columns and finally came up with a solution.

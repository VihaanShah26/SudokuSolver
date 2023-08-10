# Constraint Satisfaction 

## Goal - Design a software to solve a sudoku problem 
Rules for sudoku - [https://www.conceptispuzzles.com/index.aspx?uri=puzzle/sudoku/rules](url)

## Program 
The program receives a two dimensional array of size 9x9 which represents the 9x9 sudoku board. Empty spots on the board are represented by 0's and other spots are represented by their respective numbers from 1-9. 

The program replaces all 0's on the board with the correct number and also returns the number of permutations required to arrive at the solution. 

Two constraint satisfaction techniques are used to solve the Sudoku - Back Tracking & Forward Checking. The number of permutations required in each method can be used to determine the optimized approach to solving Sudoku. 

## Back Tracking Search 
Back Tracking is the basic uninformed algorithm for solving constraint satisfaction problems. Variable assignments are commutative so only assignments to a single variable are considered at each step. Constraints are checked as you go ahead i.e. only those value are considered for assignment that do not conflict with previous assignments. It is built upon the concept of Depth First Search. 

## Forward Checking Search 
Forward Checking is an algorithm for solving constraint satisfaction problems by implementing filtering. It keeps track of domains for unassigned variables and eliminate bad options that would violate a constraint when added to the existing assignment. 

## Conclusion 
For numerous iterations with different boards ranging from very few missing numbers to many missing numbers, Forward Checking provided the correct solution with significantly fewer iterations than Back Tracking. Thus, it is a more optimised approach to solving Sudoku. 

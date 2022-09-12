
#-----Module Description - Data Set Generation-----------------------#
#
#  This module contains a function needed for Assessment Task 1 in
#  QUT's teaching unit IFB104 "Building IT Systems".  You should put
#  a copy of this file in the same folder as your solution to the
#  assignment.  The necessary element will then be imported
#  into your program automatically.
#
#  NB: Do NOT make any changes to this module and do NOT submit a
#  copy of this file with your solution.  Changes made to this
#  module will have no effect when your assignment is graded because
#  the markers will use their own copy of the file.  If your program
#  relies on changes made to this file it will fail to work when
#  assessed.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used for generating the
# data set.  Do not change any of the code in this section.
#

# Import standard Python functions needed to support this module.
from random import randint, choice

#
#--------------------------------------------------------------------#



#-----Data Set Function for Assessing Your Solution------------------#
#
# The function in this section is called by the assignment template
# to generate the data sets used by your program.  Do not change
# any of the code in this section.

# The following function creates a random data set defining the
# overall image to draw.  Your program must work for ANY data set that
# can be produced by this function.  The results returned by calling
# this function will be used as the argument to your data visualisation
# function during marking.  For convenience during code development
# and marking this function also prints the data set generated to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
def raw_data():

    # Assume a certain grid width
    grid_width = 16
    # Define the competitors
    competitors = ['Competitor A', 'Competitor B']
    # Define the competitors' initial energy levels
    energies = [randint(grid_width // 2, grid_width + 3),
                randint(grid_width // 2, grid_width + 3)]
    # Define the various ways the competitors can move,
    # biasing them to move towards the finishing line
    directions = ['Forward'] * 10 + ['Lane up', 'Lane down']
    # Keep track of how many moves have been created in total
    move_no = 0
    # Keep track of how many forward moves each competitor
    # has made
    forward_moves = [0, 0]
    # Initialise the data set with the initial
    # states of the two competitors
    moves = [[0] + energies]

    # Create enough forward moves for both competitors to reach
    # the finishing line (provided they begin with enough
    # energy and don't squander energy changing lanes)
    while min(forward_moves) < grid_width:
        # Increment move number
        move_no = move_no + 1
        # Choose which competitor gets to move
        competitor = choice([0, 1])
        # Choose in which direction the competitor wants
        # to move (ignoring any limitation on their ability
        # to do so)
        direction = choice(directions)
        # Track the number of forward moves
        if direction == 'Forward':
            forward_moves[competitor] = forward_moves[competitor] + 1
        # Add the new move to the data set
        moves.append([move_no, competitors[competitor], direction])

    # Print the whole data set to the shell window, laid out
    # one move per line
    print("The competitors' moves to visualise are:\n")
    print(str(moves).replace('],', '],\n'))
    # Return the data set to the caller
    return moves

#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
# Some "fixed" data sets
#
# Developing code when the underlying data set changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the data generation function at the bottom of
# the assignment template file with a "seed" value which will force
# it to produce a known data set.  Of course, having completed your
# solution, your program must work for any list that can be returned
# by calling the data generation function with no argument.
#
# Some examples of useful seed numbers follow.
#
# In the following cases, both competitors conk out well before
# the finishing line (and neither attempts to move outside the
# grid):
#
#   13966 (A stops in cell I3, B stops in cell H1)
#   39398 (A wastes lots of energy changing lanes four times!)
#   96580 (A stops in cell H4, B stops in cell H1)
#   60557 (A stops in cell K5, B stops in cell J3)
#   33201 (A stops in cell H5, B stops in cell L1)
#   73748
#
# In the following cases, both competitors get close to the
# finishing line but both run out of energy (and neither attempts
# to move outside the grid):
#
#   48049 (Only "forward" moves are made before the simulation ends)
#   62853 (A stops in cell L4, B stops in cell K2)
#   98020 (A stops in cell K4, B stops in cell N3)
#   25920
#   54720
#
# In the following cases, Competitor A runs out of energy and then
# Competitor B wins (and neither attempts to leave the grid):
#
#    4462 (A stops in cell I4, B wins in cell P1)
#   17712 (B makes "forward" moves only)
#   73240 (A stops in cell H3, B wins in cell P3)
#   37874
#
# In the following cases, Competitor B runs out of energy and then
# Competitor A wins (and neither attempts to leave the grid):
#
#   58510 (Only "forward" moves are made before the simulation ends)
#    9149 (B stops in cell O4, A wins in cell P5)
#   58275 (B stops in cell G2, A wins in cell P4)
#   14046 (B conks out on the finishing line in cell P1!)
#   48643 (B stops in cell I2, A wins in cell P2)
#   93542
#
# In the following cases, Competitor A wins while Competitor B
# is still moving (and neither attempts to leave the grid):
#
#   25714 (A wins in cell P5 while B is in cell K3)
#   71482 (A wins in cell P4 while B is in cell H3)
#   73535
#   92097
#
# In the following cases, Competitor B wins while Competitor A
# is still moving (and neither attempts to leave the grid):
#
#    6055 (B wins in cell P1 while A is in cell I4)
#   83332 (B wins in cell P1 while A is in cell J6)
#   96928 (Very close race!)
#   31518
#
# In the following cases, Competitor A runs out of energy in
# the last cell before the finishing line:
#
#   15367 (A runs out of energy in cell P5)
#   59053 (A runs out of energy in cell P3)
#
# In the following cases, Competitor B runs out of energy in
# the last cell before the finishing line:
#
#   26276 (B goes forward all the way but stops in cell P2)
#   56881 (Both change lanes a lot, A stops in cell O5, B in cell P2)
#   98642
#   71736
#
# In the following cases, Competitor A wastes moves (and
# energy) by trying to change up a lane when already at the
# top of the grid:
#
#    5311 (A tries to move outside the grid 3 times and
#          stops in cell O6)
#   35503 (A tries to move outside the grid 4 times and
#          stops in cell D6)
#
# In the following cases, Competitor B wastes moves (and
# energy) by trying to change down a lane when already at the
# bottom of the grid:
#
#   83237 (B tries to move outside the grid 4 times and stops
#          in cell L2)
#   92594 (B tries to move outside the grid once and stops
#          in cell F2)
#
# In the following case, Competitor A crosses Competitor B's path
# and thus overwrites B's symbol:
#
#   90221 (A overwrites B in cells H3 to L3)
#
# In the following case, Competitor B crosses Competitor A's path
# and thus overwrites A's symbol:
#
#   65315 (B overwrites A in cells F3 and F4)
#
# Of course, you are free to choose other seed values to help you
# debug your code.
#
#--------------------------------------------------------------------#

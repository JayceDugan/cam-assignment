
#-----Module Description - Drawing Canvas Configuration--------------#
#
#  This module contains functions needed for Assessment Task 1 in
#  QUT's teaching unit IFB104 "Building IT Systems".  You should put
#  a copy of this file in the same folder as your solution to the
#  assignment.  The necessary elements will then be imported
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
# This section imports necessary functions used for creating the
# drawing canvas.  Do not change any of the code in this section.
#

# Import standard Python functions needed to support this module.
from turtle import *

#
#--------------------------------------------------------------------#



#-----Functions for Maintaining the Drawing Canvas-------------------#
#
# The functions in this section are called by the assignment template
# to manage the drawing canvas used by your program.  Do not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
#
def create_drawing_canvas(canvas_title = "Put your solution's title here",
                          draw_slow = True,
                          cell_size = 80,
                          background_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          write_instructions = True):

    # Validity check on cell size
    assert cell_size >= 60, 'Grid cells must be at least 60x60 pixels'
    
    # Define constant values to determine the size of the
    # drawing canvas, proprtional to the given cell size
    grid_width = 16 # cells
    grid_height = 6 # cells
    x_margin = cell_size * 0.9 # pixels, left/right margin
    y_margin = cell_size * 2.3 # pixels, top/bottom margin
    canvas_height = grid_height * cell_size + y_margin * 2
    canvas_width = grid_width * cell_size + x_margin * 2
    axes_font = ('Arial', cell_size // 5, 'normal') # for the grid's axes
    instructions_font = ('Arial', cell_size // 3, 'normal') # for the instructions

    # Set up the drawing canvas with enough space for the grid and
    # surrounding margins
    setup(canvas_width, canvas_height)
    bgcolor(background_colour)

    # Put a title on the canvas
    title(canvas_title)

    # Draw the grid as quickly as possible
    tracer(False)

    # Get the pen ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Write each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = axes_font)

        # Write each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = axes_font)

        # Mark the two special cells
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size,
             cell_size * 1.5)
        dot(cell_size // 6)
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size,
             -cell_size * 1.5)
        dot(cell_size // 6)

    # Optionally write instructions in the blank spaces
    if write_instructions:
        # Top
        goto(0, ((grid_height + 1.75) * cell_size) // 2)
        write("Draw Competitor A\u2019s\ntwo states here",
              align = 'center', font = instructions_font)    
        # Bottom
        goto(0, -((grid_height + 3.4) * cell_size) // 2)
        write("Draw Competitor B\u2019s\ntwo states here",
              align = 'center', font = instructions_font)    

    # Reset the pen and cursor ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()

    # Complete the rest of the drawing at the student's chosen speed
    tracer(draw_slow)
        


# A useful function adapted from one of the lecture demonstrations
# for drawing a gold star, starting from the top point
#
def gold_star(x_pos, y_pos, cell_size = 80):

    # Constant values
    left_angle = 72 # degrees, for left turns
    right_angle = 144  # degrees, for right turns
    line_size = cell_size // 3 # length of each of the ten lines

    # Set the pen characteristics
    width(2)
    pencolor('black')
    fillcolor('gold')

    # Get ready to draw
    penup()
    goto(x_pos, y_pos)
    setheading(-left_angle)
    pendown()
    begin_fill()

    # Draw five concave segments
    for segment_no in [1, 2, 3, 4, 5]:
      forward(line_size)
      left(left_angle)
      forward(line_size)
      right(right_angle)

    # Tidy up
    end_fill()
    penup()
        


# End the program and release the drawing canvas back to the
# host operating system
#
def release_drawing_canvas(signature, cell_size = 80,
                           text_colour = 'slate grey'):

    # Define constant values related to the size of the
    # drawing canvas
    grid_width = 16 # cells
    grid_height = 6 # cells
    signature_font = ('Comic Sans MS', cell_size // 5, 'bold')
    
    # Ensure any student drawing still in progress is displayed
    tracer(True)
    
    # Ensure the cursor is not left visible at the end
    hideturtle()
    
    # Sign the canvas with the student's name
    color(text_colour)
    goto((cell_size * grid_width) // 2,
         (cell_size * (grid_height + 0.1)) // 2)
    write('Visualisation by ' + signature + ' ',
          align = 'right', font = signature_font)    
    
    # Release the window to the host system
    done()
    
#
#--------------------------------------------------------------------#

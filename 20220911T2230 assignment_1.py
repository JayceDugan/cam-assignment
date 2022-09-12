#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2022.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 10335412
student_name   = "cameron duchatel"
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#

#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the assignment instructions in Blackboard for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
if isfile('data_visualisation_configuration.py'):
    print('\nConfiguration module found ...\n')
    from data_visualisation_configuration import *
else:
    print("\nCannot find file 'data_visualisation_configuration.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('data_visualisation_data_source.py'):
    print('Data generation module found ...\n')
    from data_visualisation_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return raw_data() # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#


# variables
cell_Size = 80 # global


def competitor_b_exhausted(x_cord, y_cord): # cat_exhausted


    # border
    fillcolor("DarkSlateBlue")
    begin_fill()
    border(x_cord, y_cord) # (300,-400)
    end_fill()

    # start with body finish with head

    # cat_body
    penup()
    goto(x_cord +15, y_cord+15)
    pendown()
    width(1)
    begin_fill()
    fillcolor("cornsilk3")
    seth(-45)
    circle(40,90)
    circle(8,90)
    circle(40,90)
    circle(8,90)
    end_fill()


    # cat_head
    penup()
    left(90)
    forward(20)
    pendown()
    begin_fill()
    fillcolor("cornsilk3")
    circle(15)
    end_fill()

    # cat_left_ear
    penup()
    left(135)
    forward(25)
    right(80)
    forward(15)
    pendown()
    begin_fill()
    fillcolor("cornsilk3")
    for i in range(3):
        forward(10)
        right(120)
    end_fill()

    # right_ear
    penup()
    right(90)
    forward(25)
    left(15)
    pendown()
    begin_fill()
    fillcolor("cornsilk3")
    for i in range(3):
        forward(10)
        right(120)
    end_fill()
    pendown()

    # cat_eyes
    penup()
    right(130)
    forward(5)
    pendown()
    forward(5)
    
    penup()
    right(90)
    forward(10)
    right(110)
    pendown()
    forward(5)

    # cat_mouth
    penup()
    right(145)
    forward(12)
    pendown()
    circle(4)
    
    # cat_tail
    penup()
    left(80)
    forward(55)
    left(90)
    pendown()
    width(3)
    right(0)
    forward(15)
    right(270)
    forward(15)
    right(90)
    forward(15)
    penup()

#-------------------------------

def competitor_b_energetic(x_cord, y_cord): # cat_energetic

    # border
    fillcolor("yellow")
    begin_fill()
    border(x_cord, y_cord) # (-360,-400)
    end_fill()
    
    # cat_body
    penup()
    goto(x_cord +15, y_cord +15)
    pendown()
    width(1)
    begin_fill()
    fillcolor("DeepPink")
    seth(-45)
    circle(40,90)
    circle(8,90)
    circle(40,90)
    circle(8,90)
    end_fill()


    # cat_head
    penup()
    left(90)
    forward(20)
    pendown()
    begin_fill()
    fillcolor("DeepPink")
    circle(15)
    end_fill()

    # cat_left_ear
    penup()
    left(135)
    forward(25)
    right(80)
    forward(15)
    pendown()
    begin_fill()
    fillcolor("DeepPink")
    for i in range(3):
        forward(10)
        right(120)
    end_fill()

    # right_ear
    penup()
    right(90)
    forward(25)
    left(15)
    pendown()
    begin_fill()
    fillcolor("DeepPink")
    for i in range(3):
        forward(10)
        right(120)
    end_fill()
    pendown()

    # cat_eyes
    penup()
    right(140)
    forward(4)
    pendown()
    circle(3.5)
    
    penup()
    right(65)
    forward(8)
    right(110)
    pendown()
    circle(3.5)

    # cat_mouth
    penup()
    left(180)
    forward(5)
    pendown()
    circle(5, 180)
    penup()
    
    # cat_tail
    penup()
    right(80)
    forward(50)
    left(90)
    pendown()
    width(3)
    right(0)
    forward(15)
    right(270)
    forward(15)
    right(90)
    forward(15)
    penup()

    goto(x_cord, y_cord)

 
#-------------------------------


def competitor_a_exhausted(x_cord, y_cord): # mouse_exhausted

    # border
    fillcolor("cadetBlue")
    begin_fill()
    border(x_cord, y_cord) # (300,300)
    end_fill()

    # goto origin for all body parts
    # adjustments =  position, size


    # mouse_head
    penup()
    goto(x_cord +25, y_cord +28) # goto(330,340)
    pendown()
    begin_fill()
    fillcolor("grey")
    circle(13.5) # 20>13.5
    end_fill()
    
    # left_ear
    penup()
    left(180)
    forward(12)
    right(90)
    forward(20)
    pendown()
    begin_fill()
    fillcolor("grey")
    circle(6)
    end_fill()
    
    # right_ear
    penup()
    right(90) # continues from last angle
    forward(26)
    pendown()
    begin_fill()
    fillcolor("grey")
    circle(6)
    end_fill()

    # left_eye
    penup()
    #right(0)
    forward(8)
    left(180)
    forward(28)
    pendown()
    dot(4)
    
    #right_eye
    penup()
    right(180)
    forward(10)
    pendown()
    dot(4)

    # MOUTH
    penup()
    right(90)
    forward(10)
    right(90)
    forward(2)
    pendown()
    forward(10)
    
    # mouse_body
    penup()
    left(90)
    forward(23)
    pendown()
    begin_fill()
    fillcolor("grey")
    seth(-45)
    for i in range(2):
        circle(35,90)
        circle(6,90)
    end_fill()

    # mouse_tail
    penup()
    right(0)
    forward(25)
    left(90)
    forward(40)
    pendown()
    forward(10)
    left(270)
    forward(5)

    penup()
    hideturtle()

#-------------------------------

def competitor_a_energetic(x_cord, y_cord): # mouse_energetic

    # border
    fillcolor("green")
    begin_fill()
    border(x_cord, y_cord) # (-360,300) 
    end_fill()

    # mouse_head
    penup()
    goto(x_cord +25, y_cord + 30) # (x_cord +25, y_cord + 30) # (-330,340)
    pendown()
    begin_fill()
    fillcolor("DarkOrange")
    circle(13.5) # 20>13.5
    end_fill()
    
    # left_ear
    penup()
    left(180)
    forward(12)
    right(90)
    forward(20)
    pendown()
    begin_fill()
    fillcolor("DarkOrange")
    circle(6)
    end_fill()
    
    # right_ear
    penup()
    right(90) # continues from last angle
    forward(26)
    pendown()
    begin_fill()
    fillcolor("DarkOrange")
    circle(6)
    end_fill()

    # left_eye
    penup()
    #right(0)
    forward(8)
    left(180)
    forward(28)
    pendown()
    dot(4)
    
    #right_eye
    penup()
    right(180)
    forward(10)
    pendown()
    dot(4)

    # MOUTH
    penup()
    right(90)
    forward(10)
    right(90)
    forward(10)
    pendown()
    setheading(-60)
    circle(5, 120)

    
    # mouse_body
    penup()
    right(180)
    forward(25)
    pendown()
    begin_fill()
    fillcolor("DarkOrange")
    seth(-45)
    for i in range(2):
        circle(35,90)
        circle(6,90)
    end_fill()

    # mouse_tail
    penup()
    right(0)
    forward(25)
    left(90)
    forward(40)
    pendown()
    forward(10)
    right(270)
    forward(10)
    right(90)
    forward(10)

    penup()
    goto(x_cord, y_cord)
    hideturtle()
    
        
#-------------------------------

# border for symbols (cat, mouse)
# global vars:
dist = 80
sides = 4
angle = 90

def border(x_cord, y_cord):
    seth(0)
    penup()
    goto(x_cord, y_cord)
    pendown()
    width(3)
    for _ in range(sides):
        forward(dist)
        left(angle)
    width(1)
    penup()


#-------------------------------

def write_text():

    # text_top_left
    penup()
    goto(-400,300)
    pendown()
    write("Energetic Mouse", move=True,align='right',font=('Arial',10,'bold'))
    penup()

    # text_top_right
    penup()
    goto(520,300)
    pendown()
    write("Exhausted Mouse", move=True,align='right',font=('Arial',10,'bold'))
    penup()

    # text_bottom_left
    penup()
    goto(-400,-350)
    pendown()
    write("Energetic Cat", move=True,align='right',font=('Arial',10,'bold'))

    # text_bottom_right
    penup()
    goto(500,-350)
    pendown()
    write("Exhausted Cat", move=True,align='right',font=('Arial',10,'bold'))

#-------------------------------

# All of your code goes in, or is called from, this function
# rename_me = steps, and_me_too = labelling


def visualise_data(steps, labelling):
    # leave arguments, only calling four functions

    title("The Cat and Mouse")
    write_text()
    competitor_a_energetic(-330,295)
    competitor_a_exhausted(310,295)
    competitor_b_energetic(-345,-380)
    competitor_b_exhausted(315,-380)
    #competitor_b_exhausted(0,0)


    #competitor_a_energetic(-640,80)
    #competitor_a_energetic(-640,-160)

#---------------------------------------------------------------#

    ### 1B WORKINGS
    # check step > competitor > energy > direction > execute step
    

    # VARIABLES
    competitor_a_energy = 0 # energy updated based on dataset (first list)
    competitor_b_energy = 0

    # stopping draw function when exhausted
    competitor_b_end = False
    competitor_a_end = False
    

        # CHARACTER STARTING POSITION
    competitor_a_pos = [8 * -cell_Size, cell_Size] # changed to list
    competitor_b_pos = [8 * -cell_Size, 2* -cell_Size]


    # draw where; [0] = x, [1] = y
    competitor_a_energetic(competitor_a_pos[0], competitor_a_pos[1])
    competitor_b_energetic(competitor_b_pos[0], competitor_b_pos[1])
    

    ### FIRST LIST [[0, 15, 10] ...]
    for step in steps:

        if step[0] == 0: # refs 0 (step-1)
            competitor_a_energy = step[1] # refs 15 (step-2)
            competitor_b_energy = step[2] # refs 10 (step-3)
            
        ### SECOND LIST [step, competitor, movement]
        else:
            # COMPETITOR A
            if step[1] == 'Competitor A':
                
                # IF ENERGETIC (A)
                if competitor_a_energy > 0: # energetic

                    if step[2] == 'Forward':
                        if competitor_a_pos[0] < 640: # boundary control # 640
                            competitor_a_energetic(competitor_a_pos[0] + cell_Size, competitor_a_pos[1]) #forward
                        else:
                            competitor_a_energetic(competitor_a_pos[0], competitor_a_pos[1])

                    # if y_cord is less than border move up, else don't move
                    elif step[2] == 'Lane up':
                        print("listening")
                        if competitor_a_pos[1] <240: # boundary control
                            competitor_a_energetic(competitor_a_pos[0], competitor_a_pos[1] + cell_Size) #up
                        else:
                            competitor_a_energetic(competitor_a_pos[0], competitor_a_pos[1])
                    
                    else:
                        if competitor_a_pos[1] <-240: # boundary control
                            competitor_a_energetic(competitor_a_pos[0], competitor_a_pos[1] - cell_Size) # down
                        else:
                            competitor_a_energetic(competitor_a_pos[0], competitor_a_pos[1])
                        
                        
                    #write(competitor_a_energy)

                    competitor_a_pos = pos() # takes current position
    
                # IF EXHAUSTED (A)
                else:
                    if competitor_a_end == False:
                        
                        if step[2] == 'Forward':
                            competitor_a_exhausted(competitor_a_pos[0] + cell_Size, competitor_a_pos[1])
                        elif step[2] == 'Lane up':
                            competitor_a_exhausted(competitor_a_pos[0] + cell_Size, competitor_a_pos[1] + cell_Size)
                        else:
                            competitor_a_exhausted(competitor_a_pos[0] + cell_Size, competitor_a_pos[1] - cell_Size) # Down

                        competitor_a_pos = pos()
                    competitor_a_end = True
                    
                competitor_a_energy = competitor_a_energy -1 # rm energy used

            # COMPETITOR B
            else:

                # IF ENERGETIC (B)
                if competitor_b_energy > 0: # energetic

                    if step[2] == 'Forward':
                        if competitor_b_pos[0] <640: # boundary control
                            competitor_b_energetic(competitor_b_pos[0] + cell_Size, competitor_b_pos[1]) # forward
                        else:
                            competitor_b_energetic(competitor_b_pos[0], competitor_b_pos[1])

                    elif step[2] == 'Lane up':
                        if competitor_b_pos[1] <240: # boundary control
                            competitor_b_energetic(competitor_b_pos[0], competitor_b_pos[1] + cell_Size) # up
                        else:
                            competitor_b_energetic(competitor_b_pos[0], competitor_b_pos[1])
                            
                    else:
                        if competitor_b_pos[1] < -240: # boundary control
                            competitor_b_energetic(competitor_b_pos[0] + cell_Size, competitor_b_pos[1] - cell_Size) # down
                        else:
                            competitor_b_energetic(competitor_b_pos[0] + cell_Size, competitor_b_pos[1])
                            
                    competitor_b_pos = pos()

                # IF EXHAUSTED (B)
                else:
                    if competitor_b_end == False:
                    
                        if step[2] == 'Forward':
                            competitor_b_exhausted(competitor_b_pos[0] + cell_Size, competitor_b_pos[1])
                        elif step[2] == 'Lane up':
                            competitor_b_exhausted(competitor_b_pos[0] + cell_Size, competitor_b_pos[1] + cell_Size)
                        else:
                            competitor_b_exhausted(competitor_b_pos[0] + cell_Size, competitor_b_pos[1] - cell_Size) # Down

                        competitor_b_pos = pos()
                    competitor_b_end = True

                competitor_b_energy = competitor_b_energy -1 # rm energy used


    #gold_star()

            
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(cell_size = cell_Size, write_instructions=False)

tracer(False)

### add tracer to each symbol to make the symbol run made fast but the board normal pace

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set(), False) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#


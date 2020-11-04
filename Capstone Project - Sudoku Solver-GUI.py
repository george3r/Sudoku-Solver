from simple_colors import *
from IPython.display import clear_output

def update():
    
  #assigns each nine box (row, column, and box) to variables in the dictionary. 

  global row1
  global row2
  global row3
  global row4
  global row5
  global row6
  global row7
  global row8
  global row9

  global col1
  global col2
  global col3
  global col4
  global col5
  global col6
  global col7
  global col8
  global col9
  
  global box1
  global box2
  global box3
  global box4
  global box5
  global box6
  global box7
  global box8
  global box9    
  
  row1 = [dict_ln['A1'],dict_ln['B1'],dict_ln['C1'],dict_ln['D1'],dict_ln['E1'],dict_ln['F1'],dict_ln['G1'],dict_ln['H1'],dict_ln['I1']]
  row2 = [dict_ln['A2'],dict_ln['B2'],dict_ln['C2'],dict_ln['D2'],dict_ln['E2'],dict_ln['F2'],dict_ln['G2'],dict_ln['H2'],dict_ln['I2']]
  row3 = [dict_ln['A3'],dict_ln['B3'],dict_ln['C3'],dict_ln['D3'],dict_ln['E3'],dict_ln['F3'],dict_ln['G3'],dict_ln['H3'],dict_ln['I3']]
  row4 = [dict_ln['A4'],dict_ln['B4'],dict_ln['C4'],dict_ln['D4'],dict_ln['E4'],dict_ln['F4'],dict_ln['G4'],dict_ln['H4'],dict_ln['I4']]
  row5 = [dict_ln['A5'],dict_ln['B5'],dict_ln['C5'],dict_ln['D5'],dict_ln['E5'],dict_ln['F5'],dict_ln['G5'],dict_ln['H5'],dict_ln['I5']]
  row6 = [dict_ln['A6'],dict_ln['B6'],dict_ln['C6'],dict_ln['D6'],dict_ln['E6'],dict_ln['F6'],dict_ln['G6'],dict_ln['H6'],dict_ln['I6']]
  row7 = [dict_ln['A7'],dict_ln['B7'],dict_ln['C7'],dict_ln['D7'],dict_ln['E7'],dict_ln['F7'],dict_ln['G7'],dict_ln['H7'],dict_ln['I7']]
  row8 = [dict_ln['A8'],dict_ln['B8'],dict_ln['C8'],dict_ln['D8'],dict_ln['E8'],dict_ln['F8'],dict_ln['G8'],dict_ln['H8'],dict_ln['I8']]
  row9 = [dict_ln['A9'],dict_ln['B9'],dict_ln['C9'],dict_ln['D9'],dict_ln['E9'],dict_ln['F9'],dict_ln['G9'],dict_ln['H9'],dict_ln['I9']] 

  col1 = [dict_ln['A1'],dict_ln['A2'],dict_ln['A3'],dict_ln['A4'],dict_ln['A5'],dict_ln['A6'],dict_ln['A7'],dict_ln['A8'],dict_ln['A9']]
  col2 = [dict_ln['B1'],dict_ln['B2'],dict_ln['B3'],dict_ln['B4'],dict_ln['B5'],dict_ln['B6'],dict_ln['B7'],dict_ln['B8'],dict_ln['B9']]
  col3 = [dict_ln['C1'],dict_ln['C2'],dict_ln['C3'],dict_ln['C4'],dict_ln['C5'],dict_ln['C6'],dict_ln['C7'],dict_ln['C8'],dict_ln['C9']]
  col4 = [dict_ln['D1'],dict_ln['D2'],dict_ln['D3'],dict_ln['D4'],dict_ln['D5'],dict_ln['D6'],dict_ln['D7'],dict_ln['D8'],dict_ln['D9']]
  col5 = [dict_ln['E1'],dict_ln['E2'],dict_ln['E3'],dict_ln['E4'],dict_ln['E5'],dict_ln['E6'],dict_ln['E7'],dict_ln['E8'],dict_ln['E9']]
  col6 = [dict_ln['F1'],dict_ln['F2'],dict_ln['F3'],dict_ln['F4'],dict_ln['F5'],dict_ln['F6'],dict_ln['F7'],dict_ln['F8'],dict_ln['F9']]
  col7 = [dict_ln['G1'],dict_ln['G2'],dict_ln['G3'],dict_ln['G4'],dict_ln['G5'],dict_ln['G6'],dict_ln['G7'],dict_ln['G8'],dict_ln['G9']]
  col8 = [dict_ln['H1'],dict_ln['H2'],dict_ln['H3'],dict_ln['H4'],dict_ln['H5'],dict_ln['H6'],dict_ln['H7'],dict_ln['H8'],dict_ln['H9']]
  col9 = [dict_ln['I1'],dict_ln['I2'],dict_ln['I3'],dict_ln['I4'],dict_ln['I5'],dict_ln['I6'],dict_ln['I7'],dict_ln['I8'],dict_ln['I9']]    

  box1 = [dict_ln['A1'],dict_ln['B1'],dict_ln['C1'],dict_ln['A2'],dict_ln['B2'],dict_ln['C2'],dict_ln['A3'],dict_ln['B3'],dict_ln['C3']]
  box2 = [dict_ln['D1'],dict_ln['E1'],dict_ln['F1'],dict_ln['D2'],dict_ln['E2'],dict_ln['F2'],dict_ln['D3'],dict_ln['E3'],dict_ln['F3']]
  box3 = [dict_ln['G1'],dict_ln['H1'],dict_ln['I1'],dict_ln['G2'],dict_ln['H2'],dict_ln['I2'],dict_ln['G3'],dict_ln['H3'],dict_ln['I3']]
  box4 = [dict_ln['A4'],dict_ln['B4'],dict_ln['C4'],dict_ln['A5'],dict_ln['B5'],dict_ln['C5'],dict_ln['A6'],dict_ln['B6'],dict_ln['C6']]
  box5 = [dict_ln['D4'],dict_ln['E4'],dict_ln['F4'],dict_ln['D5'],dict_ln['E5'],dict_ln['F5'],dict_ln['D6'],dict_ln['E6'],dict_ln['F6']]
  box6 = [dict_ln['G4'],dict_ln['H4'],dict_ln['I4'],dict_ln['G5'],dict_ln['H5'],dict_ln['I5'],dict_ln['G6'],dict_ln['H6'],dict_ln['I6']]
  box7 = [dict_ln['A7'],dict_ln['B7'],dict_ln['C7'],dict_ln['A8'],dict_ln['B8'],dict_ln['C8'],dict_ln['A9'],dict_ln['B9'],dict_ln['C9']]
  box8 = [dict_ln['D7'],dict_ln['E7'],dict_ln['F7'],dict_ln['D8'],dict_ln['E8'],dict_ln['F8'],dict_ln['D9'],dict_ln['E9'],dict_ln['F9']]
  box9 = [dict_ln['G7'],dict_ln['H7'],dict_ln['I7'],dict_ln['G8'],dict_ln['H8'],dict_ln['I8'],dict_ln['G9'],dict_ln['H9'],dict_ln['I9']]    
 


    

def game_board():
  # dispaly game board
  print('     A     B     C     D     E     F     G     H     I    ')
  print('   '+'_____ '*9)

  for i in range(9):
    print('  |'+'     |'*9)        
    print(f'{i+1} | {col1[i]} | {col2[i]} | {col3[i]} | {col4[i]} | {col5[i]} | {col6[i]} | {col7[i]} | {col8[i]} | {col9[i]} | {i+1}')    
    print('  '+'|_____|'+'_____|'*8)

  print(" ")
  print('     A     B     C     D     E     F     G     H     I    ')


def sole_canidate(nine_box):
  # removes known values (cells with only one value) from all other cells in the given nine box. 
  # for each list with a len() of 1
  for counter,i in enumerate(nine_box):
    if len(nine_box[counter]) == 1:
      final_num = nine_box[counter]

      #remove row[counter_row] value from all other lists in row if the cell has been solved
      for c,n in enumerate(nine_box):
        if len(nine_box[c]) > 1:
          try:
            nine_box[c].remove(final_num[0])
          except:
            pass


def unique_canidate(nine_box):
  # If a number only apears in only one cell of a nine box, it is the only possible solution. Remove all other numbers from that cell
  # count the number of times a each number apears in a nine box
  for counter,i in enumerate(range(9)):
    sum_count = 0
    for ii in range(9):
      sum_count += nine_box[ii].count(counter+1)
    # if there is only one of a certain number, then remove all numbers from that cell, and add that number back to the cell (assigning it as the answer)
    if sum_count == 1:
      for n in range(9):
        if nine_box[n].count(counter+1) == 1:
          for nn in range(len(nine_box[n])):
            nine_box[n].pop()
          nine_box[n].append(counter+1)

        
def naked_subset(nine_box):
  # If only two numbers are in a cell of a nine box, and another cell in the same nine box also has only those two numbers:
  # those two numbers must go into those two cells and can be removed from all other cells in the nine box. 
  for counter,i in enumerate(nine_box):
    # check to see if any of the cells have a len == 2
      if len(i) == 2:
        # if a cell has a len = 2: 
        # remove it temporarily from the nine box
        cur_eval = nine_box.pop(counter)
        # check to see if the removed value matches any other cells in the nine box
        # THE ORDER OF THE NUMBERS MUST BE THE SAME IN THE LISTS OR IT WILL NOT MATCH!!!
        for count,j in enumerate(nine_box):
          # if the original len == 2 cell matches any other cells in the nine box:
          if j == cur_eval:
            # remove any matches temporarily from the nine box
            match_eval = nine_box.pop(count)
            # remove values in the popped lists from the other lists in the nine box
            # for k in the nine box (minus the two removed cells):
            for k in nine_box:
              # for each number in the list of k:
              for l in k:
                # if the number in list k == one of the two numbers in the matching cells with a length of two:
                # remove that number
                if match_eval[0] == l:
                  k.remove(match_eval[0])
                if match_eval[1] == l:
                  k.remove(match_eval[1])
            # add the second mathed value back into the list in the correct order
            nine_box.insert(count,match_eval)
        # add the original len == 2 value back into the list in the correct order
        nine_box.insert(counter,cur_eval)        

        
def starting_position():
  # define a blank unsolved sudoku problem, then take in input from the GUI 
  global dict_ln 
  global list_l_n
  global list_ln_keys
  
  # define list of GUI cell names
  list_l_n = [A_1,B_1,C_1,D_1,E_1,F_1,G_1,H_1,I_1,
  A_2,B_2,C_2,D_2,E_2,F_2,G_2,H_2,I_2,
  A_3,B_3,C_3,D_3,E_3,F_3,G_3,H_3,I_3,
  A_4,B_4,C_4,D_4,E_4,F_4,G_4,H_4,I_4,
  A_5,B_5,C_5,D_5,E_5,F_5,G_5,H_5,I_5,
  A_6,B_6,C_6,D_6,E_6,F_6,G_6,H_6,I_6,
  A_7,B_7,C_7,D_7,E_7,F_7,G_7,H_7,I_7,
  A_8,B_8,C_8,D_8,E_8,F_8,G_8,H_8,I_8,
  A_9,B_9,C_9,D_9,E_9,F_9,G_9,H_9,I_9]
  # define the starting sudoku solution where all cells could be any value
  dict_ln = {'A1':[1,2,3,4,5,6,7,8,9],'B1':[1,2,3,4,5,6,7,8,9],'C1':[1,2,3,4,5,6,7,8,9],'D1':[1,2,3,4,5,6,7,8,9],'E1':[1,2,3,4,5,6,7,8,9],'F1':[1,2,3,4,5,6,7,8,9],'G1':[1,2,3,4,5,6,7,8,9],'H1':[1,2,3,4,5,6,7,8,9],'I1':[1,2,3,4,5,6,7,8,9],'A2':[1,2,3,4,5,6,7,8,9],'B2':[1,2,3,4,5,6,7,8,9],'C2':[1,2,3,4,5,6,7,8,9],'D2':[1,2,3,4,5,6,7,8,9],'E2':[1,2,3,4,5,6,7,8,9],'F2':[1,2,3,4,5,6,7,8,9],'G2':[1,2,3,4,5,6,7,8,9],'H2':[1,2,3,4,5,6,7,8,9],'I2':[1,2,3,4,5,6,7,8,9],'A3':[1,2,3,4,5,6,7,8,9],'B3':[1,2,3,4,5,6,7,8,9],'C3':[1,2,3,4,5,6,7,8,9],'D3':[1,2,3,4,5,6,7,8,9],'E3':[1,2,3,4,5,6,7,8,9],'F3':[1,2,3,4,5,6,7,8,9],'G3':[1,2,3,4,5,6,7,8,9],'H3':[1,2,3,4,5,6,7,8,9],'I3':[1,2,3,4,5,6,7,8,9],'A4':[1,2,3,4,5,6,7,8,9],'B4':[1,2,3,4,5,6,7,8,9],'C4':[1,2,3,4,5,6,7,8,9],'D4':[1,2,3,4,5,6,7,8,9],'E4':[1,2,3,4,5,6,7,8,9],'F4':[1,2,3,4,5,6,7,8,9],'G4':[1,2,3,4,5,6,7,8,9],'H4':[1,2,3,4,5,6,7,8,9],'I4':[1,2,3,4,5,6,7,8,9],'A5':[1,2,3,4,5,6,7,8,9],'B5':[1,2,3,4,5,6,7,8,9],'C5':[1,2,3,4,5,6,7,8,9],'D5':[1,2,3,4,5,6,7,8,9],'E5':[1,2,3,4,5,6,7,8,9],'F5':[1,2,3,4,5,6,7,8,9],'G5':[1,2,3,4,5,6,7,8,9],'H5':[1,2,3,4,5,6,7,8,9],'I5':[1,2,3,4,5,6,7,8,9],'A6':[1,2,3,4,5,6,7,8,9],'B6':[1,2,3,4,5,6,7,8,9],'C6':[1,2,3,4,5,6,7,8,9],'D6':[1,2,3,4,5,6,7,8,9],'E6':[1,2,3,4,5,6,7,8,9],'F6':[1,2,3,4,5,6,7,8,9],'G6':[1,2,3,4,5,6,7,8,9],'H6':[1,2,3,4,5,6,7,8,9],'I6':[1,2,3,4,5,6,7,8,9],'A7':[1,2,3,4,5,6,7,8,9],'B7':[1,2,3,4,5,6,7,8,9],'C7':[1,2,3,4,5,6,7,8,9],'D7':[1,2,3,4,5,6,7,8,9],'E7':[1,2,3,4,5,6,7,8,9],'F7':[1,2,3,4,5,6,7,8,9],'G7':[1,2,3,4,5,6,7,8,9],'H7':[1,2,3,4,5,6,7,8,9],'I7':[1,2,3,4,5,6,7,8,9],'A8':[1,2,3,4,5,6,7,8,9],'B8':[1,2,3,4,5,6,7,8,9],'C8':[1,2,3,4,5,6,7,8,9],'D8':[1,2,3,4,5,6,7,8,9],'E8':[1,2,3,4,5,6,7,8,9],'F8':[1,2,3,4,5,6,7,8,9],'G8':[1,2,3,4,5,6,7,8,9],'H8':[1,2,3,4,5,6,7,8,9],'I8':[1,2,3,4,5,6,7,8,9],'A9':[1,2,3,4,5,6,7,8,9],'B9':[1,2,3,4,5,6,7,8,9],'C9':[1,2,3,4,5,6,7,8,9],'D9':[1,2,3,4,5,6,7,8,9],'E9':[1,2,3,4,5,6,7,8,9],'F9':[1,2,3,4,5,6,7,8,9],'G9':[1,2,3,4,5,6,7,8,9],'H9':[1,2,3,4,5,6,7,8,9],'I9':[1,2,3,4,5,6,7,8,9]}
  # create a list of the keys to be able to itterate through in the future
  list_ln_keys = list(dict_ln.keys())
  # take input from the GUI to assign starting values to some sudoku cells
  for i in range(81):
    try:
      if int(list_l_n[i].get()) in [1,2,3,4,5,6,7,8,9]:
        dict_ln[list_ln_keys[i]] = [int(list_l_n[i].get())]
    except:
      pass
      
  update()    


def changes():
  # function designed to count how many possible solutions are left in the sudoku problem
  # this is run before and after solving to check and see if any changes were made, and if not, then the solver needs to stop itterating
  total_possibilities = 0
  for i in range(81):
    total_possibilities += len(dict_ln[list_ln_keys[i]])
  return total_possibilities


def solve():
    
  starting_position()

  cont_solving = True
  while cont_solving == True:

    # calculate possible solutions before solving for comparison to possible solutions after solving
    previous_poss = changes()
    print(previous_poss)
    
    # SOLVE SOLE_CANIDATE FOR ROW, COL, AND BOX
    for c,i in enumerate(range(9)):
      current_9_box = eval('row'+str(c+1))
      sole_canidate(current_9_box)
    for c,i in enumerate(range(9)):
      current_9_box = eval('col'+str(c+1))
      sole_canidate(current_9_box)
    for c,i in enumerate(range(9)):
      current_9_box = eval('box'+str(c+1))
      sole_canidate(current_9_box)
    
    # SOLVE THE UNIQUE_CANIDATE FOR ROW, COL, AND BOX (ruc = rows-unique-canidate)
    for c,i in enumerate(range(9)):
      current_9_box_ruc = eval('row'+str(c+1))
      unique_canidate(current_9_box_ruc)
    for c,i in enumerate(range(9)):
      current_9_box_cuc = eval('col'+str(c+1))
      unique_canidate(current_9_box_cuc)
    for c,i in enumerate(range(9)):
      current_9_box_buc = eval('box'+str(c+1))
      unique_canidate(current_9_box_buc) 

    # SOLVE NAKED_SUBSET FOR ROW, COL, AND BOX (rns = rows-naked-subset)
    for c,i in enumerate(range(9)):
      current_9_box_rns = eval('row'+str(c+1))
      naked_subset(current_9_box_rns)
    for c,i in enumerate(range(9)):
      current_9_box_cns = eval('col'+str(c+1))
      naked_subset(current_9_box_cns)
    for c,i in enumerate(range(9)):
      current_9_box_bns = eval('box'+str(c+1))
      naked_subset(current_9_box_bns)         
        
    # calculate possible solutions after solving for comparison to possible solutions before solving
    current_poss = changes()
    print(current_poss)
    # if the number of solutions is the same, then continued solving will yield nothing, and itteration should stop
    if current_poss == previous_poss:
      cont_solving = False
  
  game_board()
  
  update_answer()




# -----------------------------------------------------------------GUI CODE -----------------------------------------------------



import tkinter
from tkinter import *


# WINDOW DEFINED
window = Tk()
window.title("Sudoku Solver")


# FRAMES DEFINED
title_frame = Frame(window)
title_frame.grid(row = 0,column = 0, padx= 2, pady= 2)

main_frame = Frame(window, bg = 'grey',relief = 'flat', borderwidth = 4)
main_frame.grid(row=1,column=0,padx=(20,10), pady=10)

button_frame = Frame(window)
button_frame.grid(row = 2,column = 0,padx = 2, pady=2)

answer_frame = Frame(window, bg = 'grey',relief = 'flat', borderwidth = 4)
answer_frame.grid(row=1, column=1,padx=(10,20),pady=10)


# NAVIGATION DEFINED
# allows <Return> and <Down> events to move focus to the next entry
def next_widget(event):
  event.widget.tk_focusNext().focus()
  return "break"
window.bind_class("Entry", "<Return>", next_widget)
window.bind_class("Entry", "<Down>", next_widget)

# allows <Up> event to move focus to the previous entry
def prev_widget(event):
  event.widget.tk_focusPrev().focus()
  return "break"
window.bind_class("Entry", "<Up>", prev_widget)

# ANSWER RETURNED
# prints solved answer in the entry fields
def update_answer():  
  update()
  for i in range(81):
    answer = dict_ln[list_ln_keys[i]]
    list_l_n[i].delete(0, END)
    list_l_n[i].insert(0, answer)


# SOLVE BUTTON
sudoku_solver = Button(button_frame,text='Solve This Sudoku Puzzle!',cursor='hand2',command=lambda:solve())
sudoku_solver.grid(row=0,column=0,columnspan=7,pady=4)


# MAIN DISPLAY
# display the instructions/title
title = Label(title_frame, text = "Please enter the sudoku problem below: ",font = ('arial',14,'bold'))
title.grid(row=0,column=0,pady=4)

# display the entry fields
# first column (A)
A_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_1.grid(row = 0,column=0,padx=1,pady=1)
A_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_2.grid(row = 1,column=0,padx=1,pady=1)
A_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_3.grid(row = 2,column=0,padx=1,pady=1)
A_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_4.grid(row = 3,column=0,padx=1,pady=(3,1))
A_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_5.grid(row = 4,column=0,padx=1,pady=1)
A_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_6.grid(row = 5,column=0,padx=1,pady=1)
A_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_7.grid(row = 6,column=0,padx=1,pady=(3,1))
A_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_8.grid(row = 7,column=0,padx=1,pady=1)
A_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
A_9.grid(row = 8,column=0,padx=1,pady=1)
# second column (B)
B_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_1.grid(row = 0,column=1,padx=1,pady=1)
B_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_2.grid(row = 1,column=1,padx=1,pady=1)
B_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_3.grid(row = 2,column=1,padx=1,pady=1)
B_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_4.grid(row = 3,column=1,padx=1,pady=(3,1))
B_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_5.grid(row = 4,column=1,padx=1,pady=1)
B_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_6.grid(row = 5,column=1,padx=1,pady=1)
B_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_7.grid(row = 6,column=1,padx=1,pady=(3,1))
B_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_8.grid(row = 7,column=1,padx=1,pady=1)
B_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
B_9.grid(row = 8,column=1,padx=1,pady=1)
# third column (C)
C_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_1.grid(row = 0,column=2,padx=(1,3),pady=1)
C_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_2.grid(row = 1,column=2,padx=(1,3),pady=1)
C_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_3.grid(row = 2,column=2,padx=(1,3),pady=1)
C_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_4.grid(row = 3,column=2,padx=(1,3),pady=(3,1))
C_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_5.grid(row = 4,column=2,padx=(1,3),pady=1)
C_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_6.grid(row = 5,column=2,padx=(1,3),pady=1)
C_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_7.grid(row = 6,column=2,padx=(1,3),pady=(3,1))
C_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_8.grid(row = 7,column=2,padx=(1,3),pady=1)
C_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
C_9.grid(row = 8,column=2,padx=(1,3),pady=1)
# forth column (D)
D_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_1.grid(row = 0,column=3,padx=1,pady=1)
D_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_2.grid(row = 1,column=3,padx=1,pady=1)
D_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_3.grid(row = 2,column=3,padx=1,pady=1)
D_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_4.grid(row = 3,column=3,padx=1,pady=(3,1))
D_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_5.grid(row = 4,column=3,padx=1,pady=1)
D_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_6.grid(row = 5,column=3,padx=1,pady=1)
D_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_7.grid(row = 6,column=3,padx=1,pady=(3,1))
D_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_8.grid(row = 7,column=3,padx=1,pady=1)
D_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
D_9.grid(row = 8,column=3,padx=1,pady=1)
# fifth column (E)
E_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_1.grid(row = 0,column=4,padx=1,pady=1)
E_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_2.grid(row = 1,column=4,padx=1,pady=1)
E_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_3.grid(row = 2,column=4,padx=1,pady=1)
E_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_4.grid(row = 3,column=4,padx=1,pady=(3,1))
E_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_5.grid(row = 4,column=4,padx=1,pady=1)
E_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_6.grid(row = 5,column=4,padx=1,pady=1)
E_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_7.grid(row = 6,column=4,padx=1,pady=(3,1))
E_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_8.grid(row = 7,column=4,padx=1,pady=1)
E_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
E_9.grid(row = 8,column=4,padx=1,pady=1)
# sixth column (F)
F_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_1.grid(row = 0,column=5,padx=(1,3),pady=1)
F_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_2.grid(row = 1,column=5,padx=(1,3),pady=1)
F_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_3.grid(row = 2,column=5,padx=(1,3),pady=1)
F_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_4.grid(row = 3,column=5,padx=(1,3),pady=(3,1))
F_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_5.grid(row = 4,column=5,padx=(1,3),pady=1)
F_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_6.grid(row = 5,column=5,padx=(1,3),pady=1)
F_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_7.grid(row = 6,column=5,padx=(1,3),pady=(3,1))
F_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_8.grid(row = 7,column=5,padx=(1,3),pady=1)
F_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
F_9.grid(row = 8,column=5,padx=(1,3),pady=1)
# seventh column (G)
G_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_1.grid(row = 0,column=6,padx=1,pady=1)
G_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_2.grid(row = 1,column=6,padx=1,pady=1)
G_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_3.grid(row = 2,column=6,padx=1,pady=1)
G_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_4.grid(row = 3,column=6,padx=1,pady=(3,1))
G_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_5.grid(row = 4,column=6,padx=1,pady=1)
G_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_6.grid(row = 5,column=6,padx=1,pady=1)
G_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_7.grid(row = 6,column=6,padx=1,pady=(3,1))
G_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_8.grid(row = 7,column=6,padx=1,pady=1)
G_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
G_9.grid(row = 8,column=6,padx=1,pady=1)
# eighth column (H)
H_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_1.grid(row = 0,column=7,padx=1,pady=1)
H_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_2.grid(row = 1,column=7,padx=1,pady=1)
H_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_3.grid(row = 2,column=7,padx=1,pady=1)
H_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_4.grid(row = 3,column=7,padx=1,pady=(3,1))
H_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_5.grid(row = 4,column=7,padx=1,pady=1)
H_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_6.grid(row = 5,column=7,padx=1,pady=1)
H_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_7.grid(row = 6,column=7,padx=1,pady=(3,1))
H_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_8.grid(row = 7,column=7,padx=1,pady=1)
H_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
H_9.grid(row = 8,column=7,padx=1,pady=1)
# ninth column (I)
I_1 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_1.grid(row = 0,column=8,padx=(1,1),pady=1)
I_2 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_2.grid(row = 1,column=8,padx=(1,1),pady=1)
I_3 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_3.grid(row = 2,column=8,padx=(1,1),pady=1)
I_4 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_4.grid(row = 3,column=8,padx=(1,1),pady=(3,1))
I_5 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_5.grid(row = 4,column=8,padx=(1,1),pady=1)
I_6 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_6.grid(row = 5,column=8,padx=(1,1),pady=1)
I_7 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_7.grid(row = 6,column=8,padx=(1,1),pady=(3,1))
I_8 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_8.grid(row = 7,column=8,padx=(1,1),pady=1)
I_9 = Entry(main_frame,width = 2,font = ('arial',30,'bold'),justify = 'center')
I_9.grid(row = 8,column=8,padx=(1,1),pady=1)


window.mainloop()

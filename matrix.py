import os
from row_echelon_form import *

matrix=[]   #<--Enter a square matrix, in the form of [1,2,3][4,5,6][7,8,9]
solution=REF(matrix)
os.system("cls")
print("Initial Matrix: ")
solution.array()
solution.sort_zero()
solution.row_echelon_form()
solution.reduced_row_echelon_form()
solution.sort_zero()

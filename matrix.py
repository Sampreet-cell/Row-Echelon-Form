import os
from row_echelon_form import *

matrix=[[4,8,3],[5,-5,2],[3,-9,-6]]   #<--Enter a square matrix
solution=REF(matrix)
os.system("cls")
print("Initial Matrix: ")
solution.array()
solution.sort_zero()
solution.row_echelon_form()
solution.reduced_row_echelon_form()
solution.sort_zero()

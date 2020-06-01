from numpy import *

matrice = []
dim =[]
rep = 'y'



def ask_matrices():
    rows = int(input('Enter how many rows you want matrix to have'))
    columns = int(input('Enter how many columns you want your matrix to have'))
    return rows, columns


def fill_matrices(rows,columns):
    for i in range(rows*columns):
        element = int(input('enter an element'))
        matrice.append(element)
    arr = array(matrice).reshape(dim[0][0], dim[0][1])
    m = matrix(arr)
    matrice.clear()
    return m

def calculate(mat1,mat2):
    ans = input('what would you like to do? \n (press 1) multiply 2 matrices \n (press 2) add matrices')
    if ans == '1' and mat1.shape[1] == mat2.shape[0]:
        print(mat1*mat2)
    elif ans == '2' and mat1.shape == mat2.shape:
        print(mat1+mat2)
    else:
        print('sorry input was not valid')


while rep.lower() == 'y':
    dim.append(ask_matrices())
    mat1 = fill_matrices(dim[0][0],dim[0][1])
    dim.clear()
    dim.append(ask_matrices())
    mat2 = fill_matrices(dim[0][0],dim[0][1])
    calculate(mat1,mat2)
    rep = input('Would you like to use the calculator again? Press Y or N')
    dim.clear()




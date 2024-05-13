import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30 #tamaño de la celda
        #una lista de listas
                    #lista de 10 ceros       y luego repite hasta completar 20 filas
        self.grid=[[0 for j in range (self.num_cols)] for i in range (self.num_rows)]
        self.colors=Colors.get_cell_colors()
        
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end =" ")
            print()
            
    #evitar que se salgan
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column<self.num_cols:
            return True
        return False
 #METODOS PARA CUANDO SE COMPLETAN FILAS       
    def is_empty(self,row,column):
        if self.grid[row][column]==0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0
    
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
            
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
#*****************************************************************************
    def draw (self, screen): #recorre el grid y asigna el valor a las celdas, todas empiezan en 0
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                #asignamos la columna 00 01 21 53 en cada iteracion
                cell_value=self.grid[row][column]
                                     #     x                    y                    w                     h
                cell_rect=pygame.Rect(column*self.cell_size+1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
            #agregamos esos 1 para separar los cuadrados y dejar ver lineas del color del fondo, en este caso el dark blue
                # recibe la variable pantalla que creamos en main
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
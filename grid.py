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
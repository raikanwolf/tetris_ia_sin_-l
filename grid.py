import pygame

class Grid:
    def __init__(self):
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30 #tamaño de la celda
        #una lista de listas
                    #lista de 10 ceros       y luego repite hasta completar 20 filas
        self.grid=[[0 for j in range (self.num_cols)] for i in range (self.num_rows)]
        self.colors=self.get_cell_collors()
        
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end =" ")
            print()
        
    def get_cell_collors(self):
        dark_grey=(26,31,40)
        green=(47,230,23)
        red=(232,18,18)
        orange=(226,116,17)
        yellow=(237,234,4)
        purple=(166,0,247)
        cyan=(21,204,209)
        blue=(13,64,216)
        
        return[dark_grey,green,red,orange,yellow,purple,cyan, blue]
    
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
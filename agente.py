from grid import Grid
from game import Game

class Agente:
    def __init__(self,game):
        self.ia_game=game
        self.current_block=self.ia_game.get_current_block()
        self.next_block=self.ia_game.get_next_block()
    
    
    
    def rotar_bloque(game):
        self.current_block.rotate()
        
    def bajar_bloque(game):
        game.move_down()
        
    def mover_bloque_izq(game):
        game.move_left()
        
    def mover_bloque_der(game):
        game.move_right()
        
        
    def logica():
        return 0
        #if grid==0 cuadros
            #if self.current_block== tetromino S
                #mover_bloque_izq 
                #mover abajo
            #eliif self.current_block== tetromino Z
                #mover_bloque_der 
                #mover abajo
            #elif
                #mover abajo
        #elif
            #mega_Estrategia_ganadora()
            

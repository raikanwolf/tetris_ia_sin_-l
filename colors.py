class Colors:
    dark_grey=(26,31,40)
    green=(47,230,23)
    red=(232,18,18)
    orange=(226,116,17)
    yellow=(237,234,4)
    purple=(166,0,247)
    cyan=(21,204,209)
    blue=(13,64,216)
    
    #es un pyhon decorator que permite definir un metodo que puedeser llamado
    #en una clase en lugar de una instancia
    
    @classmethod
    def get_cell_colors(cls):
        return[cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
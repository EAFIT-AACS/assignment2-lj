class PDA:
    def __init__(self):
        self.stack = []
    
    def process_string(self, input_string):
        self.stack = []  # Reiniciar pila para cada cadena
        
        for char in input_string:
            if char == 'a':
                self.stack.append(char)  # Apilar 'a'
            elif char == 'b':
                if self.stack and self.stack[-1] == 'a':
                    self.stack.pop()  # Desapilar 'a' si hay una disponible
                else:
                    return False  # 'b' sin 'a' que coincida -> Rechazar
        
        return len(self.stack) == 0  # Aceptar solo si la pila queda vacía


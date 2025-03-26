class PDA:
    def __init__(self):
        self.stack = []  # Pila del autómata
        self.transitions = [
            ('q0', 'a', 'push'),
            ('q0', 'b', 'pop'),
            ('q1', 'b', 'pop')
        ]
        self.history = []  # Para registrar la evolución del PDA
    
    def process_string(self, input_string):
        state = 'q0'
        self.stack = []
        self.history = []
        
        for symbol in input_string:
            if (state, symbol, 'push') in self.transitions:
                self.stack.append(symbol)
                self.history.append((input_string, list(self.stack), f'({state}, {symbol}) -> push'))
            elif (state, symbol, 'pop') in self.transitions:
                if self.stack and self.stack[-1] == 'a':
                    self.stack.pop()
                    self.history.append((input_string, list(self.stack), f'({state}, {symbol}) -> pop'))
                else:
                    return False  # Rechazo inmediato si no hay coincidencia
        
        return len(self.stack) == 0  # Acepta si la pila está vacía
    
    def get_history(self):
        return self.history


def build_tree(history):
    print("+----------------+----------------+----------------+")
    print("| Tree          | Stack          | Rules          |")
    print("+----------------+----------------+----------------+")
    
    for tree, stack, rule in history:
        print(f"| {tree:<14} | {''.join(stack):<14} | {rule:<14} |")
    
    print("+----------------+----------------+----------------+")
    print("| end           |                |                |")
    print("+----------------+----------------+----------------+")


# Ahora solo ejecutará la prueba si se ejecuta directamente, NO al importarlo
if __name__ == "__main__":
    pda = PDA()
    input_string = "aabb"
    if pda.process_string(input_string):
        history = pda.get_history()
        build_tree(history)
    else:
        print("La cadena no es aceptada por el PDA.")

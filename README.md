# Formal Languages - Assignment 2

**Course:** "Lenguajes Formales" SI2002-1 (7308)
**Professor:** Adolfo Andrés Castro Sánchez  

## Project Overview

This repository contains the implementation of Assignment 2 for the Formal Languages course.  
It is based on the context-free grammar `S → aSb | ε`, which defines the language of balanced a’s and b’s.

The project is organized into three modular scripts that work together to:
- Generate valid and invalid strings
- Recognize valid strings using a Push Down Automaton (PDA)
- Display derivation trees from the PDA's accepting computation

---

## Implementation Overview

### `ALGORITHM_1_LFCO_2025_LG_JL.py` - Integrated Controller

This is the main script and entry point. It:
- Generates 3 valid and 3 invalid strings
- Runs the PDA on each string to check if it's accepted or rejected
- Displays the results for both valid and invalid strings
- Shows **derivation trees** for accepted strings using PDA execution history

It depends on the PDA implementation and tree builder in other modules.

---

### `ALGORITHM_2_LFCO_2025_LG_JL.py` - PDA Logic (Algorithm 2)

This module defines a basic `PDA` class with a `process_string()` method:
- Implements the PDA behavior: pushes on `'a'`, pops on `'b'`
- Accepts strings if the stack is empty at the end
- Used in Algorithm 2 to recognize whether strings belong to the CFG

This is a simplified, stateless PDA focused on correct stack transitions.

---

### `ALGORITHM_3_LFCO_2025_LG_JL.py` - PDA with History + Tree Output (Algorithm 3)

This module contains an enhanced `PDA` class:
- Tracks **PDA transitions and stack history**
- Generates an execution trace for each accepted string
- Includes the `build_tree()` function to visually represent this history as a derivation tree in a table format

Used in Algorithm 3 to show how strings are derived step-by-step.

---

## Team Members

- **Luis Alfonso Agudelo Ramirez**  
- **Julián Lara**

---

## Tools & Environment

- **Programming Language:** Python 3.12
- **OS:** Windows 10
- **Online Editor / IDE:** VSCode, [OnlineGDB](https://www.onlinegdb.com/7GB7WkwMy)
---

## How to Run the Project

### Option 1 (Run from Terminal)

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```

2. Navigate to the folder containing the scripts:
   ```bash
   cd path/to/your/project
   ```

3. Run the main script:
   ```bash
   python Main.py
   ```

   If you're on macOS or Linux and `python` maps to Python 2, use:
   ```bash
   python3 Main.py
   ```

---

### Option 2 (Run from an IDE or OnlineGDB)

1. Open the project in your IDE or copy the code into [OnlineGDB](https://www.onlinegdb.com/7GB7WkwMy)
2. Open `Main.py`
3. Click the **Run** button

---

### Output

You will see:
- Which strings are accepted/rejected
- PDA execution trace for accepted strings
- A derivation tree table for each valid string

Example output snippet:

```
Cadena: 'aabb' -> Aceptada

Árboles de derivación para cadenas válidas:
| Tree          | Stack          | Rules          |
|---------------|----------------|----------------|
| aabb          | a              | (q0, a) -> push|
| aabb          | aa             | (q0, a) -> push|
| aabb          | a              | (q0, b) -> pop |
| aabb          |                | (q0, b) -> pop |
| end           |                |                |
```

---

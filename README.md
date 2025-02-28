
# FSA-Visualizer

FSA-Visualizer is a Python tool designed to define, evaluate, and visualize Finite State Automata (FSA) from JSON configuration files. It leverages the power of NetworkX for graph manipulation and Matplotlib for visual output, providing a clear and intuitive way to understand FSA behavior.

## Features

* **JSON-based FSA Definition:** Define your FSAs using simple and readable JSON files.
* **FSA Validation:** Ensures the integrity of your FSA definition, checking for valid states, alphabet symbols, and transitions.
* **String Evaluation:** Test input strings against your FSA to determine acceptance.
* **Visual Representation:** Generates graphical representations of your FSAs, highlighting accept states for easy identification.
* **Image Export:** Saves the generated FSA visualization as a PNG image file.

## Requirements

* Python 3.x
* Libraries:
    * `networkx`
    * `matplotlib`

Install required libraries using pip:

```bash
pip install networkx matplotlib
```

## Usage

1.  **Create an FSA JSON file:**
    * Define your FSA using the following JSON structure:

    ```json
    {
      "states": ["q0", "q1", "q2"],
      "alphabet": ["a", "b"],
      "transitions": [
        {"from": "q0", "to": "q1", "input": "a"},
        {"from": "q1", "to": "q2", "input": "b"},
        {"from": "q2", "to": "q0", "input": "a"},
        {"from": "q2", "to": "q1", "input": "b"}
      ],
      "initialState": "q0",
      "acceptStates": ["q2"]
    }
    ```

    * Save this file as `fsa_model.json` (or any desired name).

2.  **Run the Python script:**

    ```bash
    python your_script_name.py
    ```

    * Replace `your_script_name.py` with the actual name of your Python script.

3.  **View the Results:**
    * The script will print whether the test string ("abb" by default) is accepted by the FSA.
    * The FSA visualization will be displayed and saved as `fsa.png` in the script's directory.

## Example

```python
import json
import networkx as nx
import matplotlib.pyplot as plt

# ... (code from your script) ...

# Example usage
filename = "fsa_model.json" # Specify the JSON filename

fsa = load_fsa_from_file(filename)

if fsa:
    string_to_evaluate = "abb"
    result = evaluate_string(fsa, string_to_evaluate)
    print(f"Is the string '{string_to_evaluate}' accepted? : {result}")
    visualize_fsa(fsa)
```

## Contributing

Contributions are welcome! If you find a bug or have an idea for an improvement, please open an issue or submit a pull request.

```

import json
import networkx as nx
import matplotlib.pyplot as plt

def generate_fsa(json_data):
    """Generates a Finite State Automaton (FSA) from JSON data."""
    try:
        states = json_data["states"]
        alphabet = json_data["alphabet"]
        transitions = json_data["transitions"]
        initial_state = json_data["initialState"]
        accept_states = json_data["acceptStates"]

        if initial_state not in states:
            raise ValueError("Invalid initial state")
        for transition in transitions:
            if transition["from"] not in states or transition["to"] not in states or transition["input"] not in alphabet:
                raise ValueError("Invalid transition")

        return {
            "states": states,
            "alphabet": alphabet,
            "transitions": transitions,
            "initial_state": initial_state,
            "accept_states": accept_states,
        }
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
        print(f"Error in automaton definition: {e}")
        return None

def evaluate_string(fsa, string):
    """Evaluates a string against the FSA."""
    current_state = fsa["initial_state"]
    for symbol in string:
        transition_found = False
        for transition in fsa["transitions"]:
            if transition["from"] == current_state and transition["input"] == symbol:
                current_state = transition["to"]
                transition_found = True
                break
        if not transition_found:
            return False
    return current_state in fsa["accept_states"]

def visualize_fsa(fsa, filename="fsa.png"):
    """Visualizes the FSA using NetworkX and Matplotlib."""
    graph = nx.DiGraph()

    for state in fsa["states"]:
        graph.add_node(state)

    for transition in fsa["transitions"]:
        graph.add_edge(transition["from"], transition["to"], label=transition["input"])

    pos = nx.spring_layout(graph)  # Node positioning

    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrowsize=20)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'label'))

    # Highlight accept states
    accept_nodes = [node for node in graph.nodes if node in fsa['accept_states']]
    nx.draw_networkx_nodes(graph, pos, nodelist=accept_nodes, node_color='lightgreen', node_size=2000)

    plt.savefig(filename)  # Save the image
    plt.show()  # Show the visualization

def load_fsa_from_file(filename):
    """Loads an FSA from a JSON file."""
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)
        return generate_fsa(json_data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")
        return None

# Example usage
filename = "fsa_model.json"  # Specify the JSON filename

fsa = load_fsa_from_file(filename)

if fsa:
    string_to_evaluate = "abb"
    result = evaluate_string(fsa, string_to_evaluate)
    print(f"Is the string '{string_to_evaluate}' accepted? : {result}")
    visualize_fsa(fsa)
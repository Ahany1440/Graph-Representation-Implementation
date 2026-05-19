# Graph Representation Project

This Python project provides a robust implementation of fundamental graph representations, inspired by Chapter 10 of *Rosen, Discrete Mathematics and Its Applications*.

The project demonstrates how to generate a large, complex directed graph and perform conversions between different data structures used to represent graphs.

## Features

* **Graph Generation**: Creates a simple directed graph (V, E) with a configurable edge probability.
* **Data Structure Conversions**:
    * **Adjacency List → Adjacency Matrix**: Efficiently converts the graph from an adjacency list representation to an adjacency matrix.
    * **Adjacency Matrix → Edge List**: Converts the matrix representation back into a list of tuples representing edges.
* **Performance Tracking**: Measures and logs the time taken for conversion processes.
* **Structured Output**: Provides a clean, formatted summary of the resulting graph structures.

## Usage

The main execution logic is contained within the `if __name__ == "__main__":` block.

1.  **Configure Parameters**: You can adjust `MAX_VERTICES` to control the size of the generated graph and `edge_chance` in the `generate_huge_complex_graph` method.
2.  **Run the script**:
    ```bash
    python <script_name>.py
    ```

### Example Output Logic
The `print_clean_project_output` method provides a snapshot of the resulting data structures to ensure the conversions were successful:
* **Adjacency List**: Displays the first few nodes and their neighbors.
* **Adjacency Matrix**: Displays a sample sub-matrix.
* **Edge List**: Displays the total count of edges and the first few edges in the list.

## Technical Details

* **Adjacency List**: Implemented using a dictionary where keys are vertex indices and values are lists of neighbor indices.
* **Adjacency Matrix**: Implemented using a 2D list (matrix) where `matrix[i][j] == 1` indicates an edge from vertex `i` to vertex `j`.
* **Edge List**: A list of tuples `(source, destination)`.

## Requirements
* Python 3.x
* No external libraries required (uses built-in `time` and `random` modules).

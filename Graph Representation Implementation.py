import time
import random

# Graph Representation Implementation
# Based on Chapter 10 of Rosen, Discrete Mathematics 7th Edition

class GraphSystem:

    def __init__(self, num_vertices):
        """
        Initializes graph structures as defined in Section 10.3.
        """
        self.num_vertices = num_vertices
        # Fixed: Corrected dictionary comprehension for adjacency list
        self.adj_list = {i: [] for i in range(num_vertices)}
        # Fixed: Corrected list comprehension for adjacency matrix
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.edge_list = []

    def generate_huge_complex_graph(self, edge_chance=0.05):
        """
        Generates a Simple Directed Graph (V, E).
        """
        print(f" Generating a complex graph with {self.num_vertices} vertices...")
        random.seed(1234) # Ensures reproducible results
        total_edges_created = 0
        
        for source in range(self.num_vertices):
            for destination in range(self.num_vertices):
                if source != destination:
                    if random.random() < edge_chance:
                        self.adj_list[source].append(destination)
                        total_edges_created += 1
                        
        print(f"--> Success! Generated {total_edges_created} edges.\n")

    def convert_list_to_matrix(self):
        """
        Converts Adjacency List to Adjacency Matrix.
        """
        print(" Running conversion: Adjacency List -> Adjacency Matrix...")
        start_time = time.perf_counter()
        
        # Reset matrix
        self.adj_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        
        for current_node, neighbors_list in self.adj_list.items():
            for neighbor in neighbors_list:
                self.adj_matrix[current_node][neighbor] = 1
                
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"--> Success! Finished in {elapsed:.5f} seconds.\n")
        return elapsed

    def convert_matrix_to_edge_list(self):
        """
        Converts Matrix back to Edge List.
        """
        print(" Running conversion: Adjacency Matrix -> Edge List...")
        start_time = time.perf_counter()
        self.edge_list = []
        
        for row in range(self.num_vertices):
            for col in range(self.num_vertices):
                if self.adj_matrix[row][col] == 1:
                    self.edge_list.append((row, col))
                    
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"--> Success! Finished in {elapsed:.5f} seconds.\n")
        return elapsed

    def print_clean_project_output(self, view_size=8):
        # Result display logic
        print("="*75)
        print("GRAPH REPRESENTATION PROJECT RESULTS")
        print("="*75)
        print(f"1. ADJACENCY LIST (First {view_size} nodes):")
        for node in range(view_size):
            print(f"   Node {node:03d} -> {self.adj_list[node][:view_size]}...")
        print("-" * 65)
        print(f"2. ADJACENCY MATRIX ({view_size}x{view_size} sample):")
        for row in range(view_size):
            print(f"  [{row}]", " ".join(str(self.adj_matrix[row][col]) for col in range(view_size)))
        print("-" * 65)
        print(f"3. EDGE LIST (First {view_size} pairs):")
        print(f"   {self.edge_list[:view_size]}")
        print(f"   Total Edges: {len(self.edge_list)}")
        print("="*75)

if __name__ == "__main__":
    MAX_VERTICES = 500
    project_run = GraphSystem(MAX_VERTICES)
    project_run.generate_huge_complex_graph(0.05)
    project_run.convert_list_to_matrix()
    project_run.convert_matrix_to_edge_list()
    project_run.print_clean_project_output()
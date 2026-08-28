import sys

class DSU:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices
        self.components = num_vertices

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        
        # Path compression
        while x != root:
            next_node = self.parent[x]
            self.parent[x] = root
            x = next_node
        return root

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        
        if rootA == rootB:
            return False

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        
        self.components -= 1
        return True

def solve(data):
    """
    Core problem-solving function.
    Reads graph data, separates edges by type (pedestrian, bus, both),
    and uses DSU to determine if a minimal spanning network
    can connect all nodes under each transportation mode.
    
    Note: The "weight" for MST construction is not a numerical value 
    but the PRIORITY of edge types:
    - both_edges (type 2) = highest priority (weight 0 equivalent)
    - bus_edges (type 1) = medium priority (weight 1 equivalent)
    - ped_edges (type 0) = lowest priority (weight 2 equivalent)  
    """

    # Read input data 
    lines = data.strip().split()
    num_vertices, num_edges = map(int, lines[:2]) 
    edges = []
    for i in range(2, len(lines), 3):
        u = int(lines[i])
        v = int(lines[i + 1])
        t = int(lines[i + 2])  # t =edge type: 0 =ped; 1 =bus; 2 =both;
        edges.append((t, u, v))

    # Сonnected graph with num_edges nodes must have at least num_edges-1 edges
    if num_edges < num_vertices - 1:
        print(-1)
        return

    dsu_bus = DSU(num_vertices)
    dsu_ped = DSU(num_vertices)
    
    used_edges = 0
    
    
    for t, u, v in edges:
        if t == 2:
            # Attempt to add edge to both networks
            # Returns True if the edge actually connected previously disconnected component (its number reduces after adding)
            merged_ped = dsu_ped.union(u, v)  # Try to add to pedestrian network
            merged_bus = dsu_bus.union(u, v)  # Try to add to bus network
            
            # Use the edge if it helped at least one network
            if merged_ped or merged_bus:  
                used_edges += 1
               
    #for t, u, v in edges:
        elif t == 1 and dsu_bus.components > 1:
            if dsu_bus.union(u, v):  # Only add if it connects new components in bus network
                used_edges += 1
             
    #for t, u, v in edges:
        elif t == 0 and dsu_ped.components > 1:
            if dsu_ped.union(u, v):  # Only add if it connects new components in pedestrian network
                used_edges += 1
                #print(f"Used pedestrian edge: {u}-{v}")
         # ранняя остановка: если оба графа соединены, больше нет смысла продолжать
        if dsu_bus.components == 1 and dsu_ped.components == 1:
            break
              
    if dsu_ped.components > 1 or dsu_bus.components > 1:
        print(-1)  # Not all stages reachable in both networks
    else:
        print(num_edges - used_edges)
        

def main():
    # --- Option 1: for DomJudge or online testing ---
    """
    data = sys.stdin.read()
    solve(data)
    
"""
    # --- Option 2: for local file testing ONLY one file ---
    filename = "samples-Grading/1.in"
    with open(filename, 'r') as file:
        data = file.read()

    print(f"Reading file: {filename}")
    print("File contains:")
    print(data)
    print("\nResult:")
    solve(data)
"""
    # --- Option 3: for local file testing ALL files---
    folder = "samples-Grading"

    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".in"):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r') as file:
                data = file.read()
            
            print(f"Reading file: {filename}")
            #print("File contains:")
            #print(data)
            print("\nResult:")
            solve(data)
            print("-" * 40)  # Разделитель между файлами
   
    """


if __name__ == "__main__":
    main()

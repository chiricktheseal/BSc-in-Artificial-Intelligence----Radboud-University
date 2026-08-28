import sys
import os

class DSU:
    """
    Disjoint Set Union (Union-Find) data structure.
    Efficiently tracks and merges disjoint sets of elements.

    Operations:
    - find(x): Return the name of the set that contains 𝒙 (i.e., the root)
    - union(a, b): Merge the sets that contain a and b into a single set
    """

    def __init__(self, num_vertices):
        # Each node is initially its own parent (self loop)
        self.parent = {i: i for i in range(num_vertices)}
        # Rank is used for balancing tree height
        self.rank = {i: 0 for i in range(num_vertices)}
        # Number of connected components in the structure
        self.components = num_vertices

    def find(self, x):
        """
        Iteratively finds the root of the set containing element x with path compression - faster and no recursion limits
        """
        if self.parent[x] == x:
            return x
        
        root = x
        # Find the root
        while root != self.parent[root]:
            root = self.parent[root]
        
        # Path compression
        current = x
        while current != root:
            next_node = self.parent[current]
            self.parent[current] = root
            current = next_node
        return root

    def union(self, a, b):
        """
        Merges the sets containing elements a and b.
        Returns True if a merge actually occurred,
        or False if both elements were already in the same set.
        """
        rootA, rootB = self.find(a), self.find(b)
        
        if rootA == rootB:
            return False  # Already connected

        # Always attach the smaller tree (lower rank) under the larger tree (higher rank)
        # This keeps the tree balanced and minimizes height
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA     # Make the smaller tree point to the larger tree's root

        # If both trees were the same height, the new combined tree grows by 1 level
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
    
    # Сonnected graph with num_edges nodes must have at least num_edges-1 edges
    if num_edges < num_vertices - 1:
        print(-1)
        return
    

    # Categorize edges by connection type with priority order:
    ##both_edges = [(u, v) for t, u, v in edges if t == 2]
    ##bus_edges = [(u, v) for t, u, v in edges if t == 1]
    ##ped_edges = [(u, v) for t, u, v in edges if t == 0]
    
    #print(f"Total vertices: {num_vertices}, total edges: {num_edges}")
    #print(f"Edges type 'both': {len(both_edges)}")
    #print(f"Edges type 'bus': {len(bus_edges)}")  
    #print(f"Edges type 'pedestrian': {len(ped_edges)}")

    # Create separate DSU for the pedestrian and bus networks
    dsu_bus = DSU(num_vertices)
    dsu_ped = DSU(num_vertices)
    
    used_edges = 0
    
    edges = []
    for i in range(2, len(lines), 3):
        u = int(lines[i])
        v = int(lines[i + 1])
        t = int(lines[i + 2])  # t =edge type: 0 =ped; 1 =bus; 2 =both;
        edges.append((t, u, v))

    

    
    # Process 'both' type edges - useful for both networks (highest priority)
    #print("\n=== 'both' edges ===")
    ##for u, v in both_edges:
    for t, u, v in edges:
        if t == 2:
            # Attempt to add edge to both networks
            if dsu_ped.components == 1 and dsu_bus.components == 1:
                break
            # Returns True if the edge actually connected previously disconnected component (its number reduces after adding)
            merged_ped = dsu_ped.union(u, v)  # Try to add to pedestrian network
            merged_bus = dsu_bus.union(u, v)  # Try to add to bus network
            
            # Use the edge if it helped at least one network
            if merged_ped or merged_bus:  
                used_edges += 1
                #print(f"Used 'both' edge: {u}-{v}")
                #print(f"  Components of dsu_ped: {dsu_ped.components}")
                #print(f"  Components of dsu_bus: {dsu_bus.components}")
            #else:
                #print(f"Skipped 'both' edge: {u}-{v} (already connected in both networks)")
    
    # Process bus edges for bus network only  
    #print("\n=== 'bus' edges ===")
    ##for u, v in bus_edges:
    for t, u, v in edges:
        if t == 1:
            if dsu_bus.union(u, v):  # Only add if it connects new components in bus network
                used_edges += 1
                #print(f"Used bus edge: {u}-{v}")
                #print(f"  Components of dsu_bus:  {dsu_bus.components}")
            #else:
                #print(f"Skipped bus edge: {u}-{v} (already connected)")

    # Process pedestrian edges for pedestrian network only
    #print("\n=== 'pedestrian' edges ===")
    ##for u, v in ped_edges:
    for t, u, v in edges:
        if t == 0:
            if dsu_ped.union(u, v):  # Only add if it connects new components in pedestrian network
                used_edges += 1
                #print(f"Used pedestrian edge: {u}-{v}")
                #print(f"  Components of dsu_ped: {dsu_ped.components}")
            #else:
                #print(f"Skipped pedestrian edge: {u}-{v} (already connected)")


    # Verify both networks are fully connected
    #print(f"\n=== Connectivity Check ===")
    #print(f"Final dsu_ped components: {dsu_ped.components}")
    #print(f"Final dsu_bus components: {dsu_bus.components}")

    if dsu_ped.components > 1 or dsu_bus.components > 1:
        print(-1)  # Not all stages reachable in both networks
    else:
        #print(f"\n=== Result ===")
        #print(f"Edges used: {used_edges}")
        #print(f"Edges removed: {num_edges - used_edges}")
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
            print("-" * 40)  
   
    """


if __name__ == "__main__":
    main()

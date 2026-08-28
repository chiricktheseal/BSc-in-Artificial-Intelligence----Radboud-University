import queue

def reconstruct_path(start_vertex, destination_vertex, parents):
  """
  Reconstructs the path from the start to the goal.

  Args:
    start_vertex (object): The starting vertex.
    destination_vertex (object): The goal vertex.
    parents (dict): Dictionary containing the parent of each vertex.


  Returns:
    (str): A string representation of the reconstructed path.
  """
  path = []
  current_vertex = destination_vertex
  while current_vertex is not None:
    path.append(current_vertex)
    current_vertex = parents.get(current_vertex, None)
  
  # Convert each element in the path to a string
  path = list(map(str, path))
  
  
  return " -> ".join(reversed(path))
      
  
def breadth_first_search(graph, start_vertex, destination_vertex):
  """
  Breadth-First Search (BFS) algorithm.

  Args:
    graph (Graph): The graph on which BFS is applied.
    start_vertex (object): The starting vertex.
    destination_vertex (object): The goal vertex.

  Returns:
    (str or None): A string representation of the BFS path if it exists, otherwise None.
  """
  # Set to keep track of visited vertices
  visited_vertices  = set( ) 
  
  # FIFO queue for BFS
  bfs_queue = queue.Queue() 
  
  # Initialize the queue with the start vertex
  bfs_queue.put(start_vertex)
  visited_vertices .add(start_vertex)

  # Dictionary to store the path from start to current vertex
  parents = {start_vertex: None}
  
  print("Performing BFS")

  while not bfs_queue.empty():
    current_vertex = bfs_queue.get()
    print(f"  Visiting vertex {current_vertex}")

    # Check if the goal is reached
    if current_vertex == destination_vertex:
      print(f"  Arived at destination  {destination_vertex}")
      
      #Reconstruct the path
      path = reconstruct_path(start_vertex, destination_vertex, parents)
      print(f"Path: {path}")
      return ""

    # Explore neighbors
    neighbors = graph.get_neighbours(current_vertex)
    for neighbor,cost in neighbors:
      if neighbor not in visited_vertices :
        print(f"    Adding to queue vertex {neighbor}")
        bfs_queue.put(neighbor)
        visited_vertices .add(neighbor)
        # Store the parent of the neighbor
        parents[neighbor] = current_vertex

  print(f"Goal vertex {destination_vertex} not reachable from {start_vertex}")
  return None


def depth_first_search(graph, start_vertex, destination_vertex):
  """
  Depth-First Search (DFS) algorithm.

  Args:
    graph (Graph): The graph on which DFS is applied.
    start_vertex (object): The starting vertex.
    destination_vertex (object): The goal vertex.

  Returns:
    (str): A string representation of the DFS path.
  """
  # Set to keep track of visited vertices
  visited_vertices  = set( ) 
  
  # LIFO queue for DFS
  dfs_queue = queue.LifoQueue()
  
  # Initialize the queue with the start vertex
  dfs_queue.put(start_vertex)
  visited_vertices .add(start_vertex)

  # Dictionary to store the path from start to current vertex
  parents = {start_vertex: None}
  
  print("Performing DFS")

  while not dfs_queue.empty():
    current_vertex = dfs_queue.get()
    print(f"  Visiting vertex {current_vertex}")

    # Check if the goal is reached
    if current_vertex == destination_vertex:
      print(f"  Arived at destination  {destination_vertex}")
      
      #Reconstruct the path
      path = reconstruct_path(start_vertex, destination_vertex, parents)
      print(f"Path: {path}")
      return ""

    # Explore neighbors
    neighbors = graph.get_neighbours(current_vertex)
    for neighbor,cost in neighbors:
      if neighbor not in visited_vertices :
        print(f"    Adding to queue vertex {neighbor}")
        dfs_queue.put(neighbor)
        visited_vertices .add(neighbor)
        # Store the parent of the neighbor
        parents[neighbor] = current_vertex

  print(f"Goal vertex {destination_vertex} not reachable from {start_vertex}")
  return None


def uniform_cost_search(graph, start_vertex, destination_vertex):
  """
  Uniform Cost Search (UCS) algorithm.

  Args:
    graph (Graph): The graph on which UCS is applied.
    start_vertex (object): The starting vertex.
    destination_vertex (object): The goal vertex.

  Returns:
    (str): A string representation of the UCS path.
  """
  # Set to keep track of visited vertices
  visited_vertices  = set( ) 
  
  # PriorityQueue queue for UCS (UFC)
  ucs_queue = queue.PriorityQueue()
  
  # Initialize the queue with the start vertex and cost
  ucs_queue.put((0,start_vertex))
  visited_vertices.add(start_vertex)

  # Dictionary to store the cost of the cheapest path to each vertex
  vertex_costs = {start_vertex: 0}
    
  # Dictionary to store the path from start to current vertex
  parents = {start_vertex: None}
  
  print("Performing UFC")

  while not ucs_queue.empty():
    (current_cost, current_vertex) = ucs_queue.get()
    print(f"  Visiting vertex {current_vertex}")

    # Check if the goal is reached
    if current_vertex == destination_vertex:
      print(f"  Arived at destination  {destination_vertex}")
      
      #Reconstruct the path
      path = reconstruct_path(start_vertex, destination_vertex, parents)
      print(f"Path: {path}")
      return ""

    # Explore neighbors
    neighbors = graph.get_neighbours(current_vertex)
    
    for neighbor,edge_cost in neighbors :
      total_cost = current_cost + edge_cost
                  
      if neighbor not in visited_vertices or total_cost < vertex_costs[neighbor]:
        print(f"    Adding to queue vertex {neighbor} with cost {edge_cost}")
        ucs_queue.put((total_cost, neighbor))
        visited_vertices.add(neighbor)
        vertex_costs[neighbor] = total_cost        
        # Store the parent of the neighbor
        parents[neighbor] = current_vertex

  print(f"Goal vertex {destination_vertex} not reachable from {start_vertex}")
  return None

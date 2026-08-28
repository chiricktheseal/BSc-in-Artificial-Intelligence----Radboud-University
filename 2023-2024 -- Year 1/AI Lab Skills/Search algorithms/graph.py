#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment 4 Search

Module to represent a graph with nodes and edges between them. 
"""

class Graph(object):
    """
    A graph with nodes and edges between them.
    """

    def __init__(self):
        """
        Constructor of Graph.
        """
        self.vertices = {}

    def add_vertex(self, source):
        """
        Add a vertex to the graph.

        Args:
            source (object): a hashable object to identify the vertex with, e.g. int or str.
        """
        assert source not in self.vertices, f"Vertex ({source}) already exists!"
        self.vertices[source] = Vertex(source)

    def add_edge(self, source, destination, cost=None, directed=False):
        """
        Add an edge between two vertices.

        Args:
            source (object): a hashable identifier for the source (i.e. from).
            destination (object): a hashable identifier for the destination (i.e. to).
            cost (float): the cost of going from the source to the destination.
            directed (bool): whether the edge is directed or not. If undirected, a symmetrical 
                             edge for both directions will be added. Default: False. 
        """
        assert source in self.vertices, f"Source vertex ({source}) does not exist!"
        assert destination in self.vertices, f"Destination vertex ({destination}) does not exist!"
        self.vertices[source].add_edge(self.vertices[destination], cost)
        if not directed:
            self.vertices[destination].add_edge(self.vertices[source], cost)

    def get_neighbours(self, source):
        """
        Retrieve all vertices that are connected to a source via an edge.

        Args:
            source (object): a hashable identifier for the source.

        Returns:
            (list): a list of neighbors as tuples with (vertex, cost). 
        """
        assert source in self.vertices, f"Source vertex ({source}) does not exist!"
        return self.vertices[source].get_neighbours()

    def __str__(self):
        """
        String representation of a graph.

        Returns
            (str): the string representation of the graph.
        """
        return "\n".join(map(str, self.vertices.values()))


class Vertex(object):
    """
    A vertex, i.e.,  node. 
    """

    def __init__(self, name):
        """
        Constructor of Vertex.

        Args:
            name (str): the name of the vertex.
        """
        self.name = name
        self.edges = []

    def add_edge(self, vertex, cost=None):
        """
        Add an outgoing edge to this vertex.
        
        Args:
            vertex (Vertex): The vertex on the other end of the edge.
            cost (float): the cost to go from the current to the other vertex. Default: None.
        """
        self.edges.append(Edge(self, vertex, cost))

    def get_neighbours(self):
        neighbours = [(edge.destination.name, edge.cost) for edge in self.edges]
        return neighbours

    def __str__(self):
        """
        String representation of a vertex.

        Returns:
            (str): the string representation of a vertex.
        """
        return str(self.name) + ": [" + ", ".join(map(str, self.edges)) + "]"

    def __eq__(self, other):
        """
        Equals operator for a vertex.

        Args:
            other (object): the object to compare the vertex to.

        Returns:
            (bool): whether the current vertex is the same as the other. 
        """
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False


class Edge(object):
    """
    An edge, i.e., a connection.
    """

    def __init__(self, source, destination, cost=None):
        """
        Constructor of Edge.

        Args:
            source (object): a hashable identifier for the source (i.e. from).
            destination (object): a hashable identifier for the destination (i.e. to).
            cost (float): the cost of going from the source to the destination. Default: None.
        """
        self.source = source
        self.destination = destination
        self.cost = cost

    def __str__(self):
        """
        String representation of an edge.

        Returns:
            (str): the string representation of an edge.
        """
        text = str(self.source.name) + "-"
        if self.cost is not None:
            text += str(self.cost)
        text += "->" + str(self.destination.name)
        return text

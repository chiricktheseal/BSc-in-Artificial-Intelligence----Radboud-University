#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 13:48:43 2025

@author: mariathiele
"""

#import io
import sys
#import copy

class Vertex:
    """
    A class setting basic attributes for vertices.
    """
    def __init__(self, number):
        self.component = -1
        # self.name = name
        self.number = number
        # self.ped_con = False
        # self.bus_con = False
        
    def set_component(self, value):
        self.component = value
    
    """
    def set_both(self):
        self.ped_con = True
        self.bus_con = True
        
    def set_pedCon(self):
        self.ped_con = True
        
    def set_busCon(self):
        self.bus_con = True
    """


def solve(data):
    #read_data(data)
    totals, content = read_file(data)
    # print(f"Total stages: {totals[0]}")
    # print(f"Total edges: {totals[1]}")
    
    # exit program if there are too few edges to connect all vertices (happens when |E| < |V|-1) or incorrect number of vertices (<0)
    if totals[1] < (totals[0] - 1) or (totals[0] < 0):
        print("-1")
    # if there are 0 vertices, print total number of edges -> there cannot be any edges if there are no vertices
    elif totals[0] == 0:
        print(str(totals[1]))
    
    # run the algorithm
    else:
        vertex_list = []
        for i in range(totals[0]):
            v = Vertex(i)
            vertex_list.append(v)
        
        con_both = []
        con_ped = []
        con_bus = []
        for i in range(4, len(content), 3):           
            # pedestrian
            if content[i] == '0':
                con_ped.append([vertex_list[int(content[i-2])], vertex_list[int(content[i-1])]])
            # bus
            elif content[i] == '1':
                con_bus.append([vertex_list[int(content[i-2])], vertex_list[int(content[i-1])]])
            # both
            elif content[i] == '2':
                con_both.append([vertex_list[int(content[i-2])], vertex_list[int(content[i-1])]])
            
        result = create_MST(vertex_list, con_ped, con_bus, con_both) # returns the amount of edges used in the MST
        
        # return -1 if there is no MSt connecting all vertices
        if result == -1:
            print("-1")
        
        # compute the number of removed edges
        else:
            removed_edges = totals[1] - result
            print(str(removed_edges))


    
def read_file(data):
    content = data.replace("\n", " ").split()
    totals = (int(content[0]), int(content[1]))
    return totals, content
        

def create_MST(vertices, con_ped, con_bus, con_both):
    component_dict = {}
    
    # initialize MST
    component_dict[0] = [vertices[0]]
    vertices[0].set_component(0)
    component_dict[-1] = [] # no component
    for i in range(1, len(vertices)):
        component_dict[-1].append(vertices[i])
    
    edge_counter = 0
    
    # start with con_both 
    edge_counter += run_for_connection_type(component_dict, con_both)
    # print("Edges after both connections:", edge_counter)
    
    # store components of dictionary in separate list -> used to later retrieve this state of dictionary
    original_components = []
    for v in vertices:
        original_components.append(v.component)
        
    shorter_con_dict = {key: value[:] for key, value in component_dict.items()}
    longer_con_dict = {key: value[:] for key, value in component_dict.items()}
    
    if len(con_ped) <= len(con_bus):
        # print("ped first")
        shorter_con = con_ped
        longer_con = con_bus
    else:
        shorter_con = con_bus
        longer_con = con_ped
    
    edge_counter += run_for_connection_type(shorter_con_dict, shorter_con)

    for key in list(shorter_con_dict.keys()):
        if not shorter_con_dict[key]: # removes every empty entries
            del shorter_con_dict[key]
    if len(shorter_con_dict.keys()) == 0:
        return -1
    elif len(shorter_con_dict.keys()) > 1:
        # print("\n\nNo solution 1")
        return -1

    # restore orginal components
    for i in range(len(original_components)):
        vertices[i].component = original_components[i]
        
    
    edge_counter += run_for_connection_type(longer_con_dict, longer_con)

    for key in list(longer_con_dict.keys()):
        if not longer_con_dict[key]: # removes every empty entries
            del longer_con_dict[key]
    if len(longer_con_dict.keys()) == 0:
        return -1
    elif len(longer_con_dict.keys()) > 1:
        # print("\n\nNo solution 2")
        return -1
    
    # print("Edges after ped connections and both connections:", edge_counter)
    #filler = 0
    return edge_counter

def run_for_connection_type(dictionary, connection_list):
    used_edges = 0
    for connection in connection_list:
        # for vertex in connection:
            # print(vertex.name, vertex.number)
        v0 = connection[0]
        v1 = connection[1]
        
        if v0.component == v1.component:
            if v0.component != -1:
                # print("\nJUMP TO NEXT ITERATION\n")
                continue
            else:
                move_vertices_to_new_component(dictionary, v0, -1, v1, -1)
                # print("\nBoth in no component before, should be in the same now\n")

        else:
            # move_vertices_to_new_component(dictionary, v0, v0.component, v1, v1.component)
            
            if (v0.component != -1) and (len(dictionary[v0.component]) > len(dictionary[v1.component])):
                move_vertices_to_new_component(dictionary, v0, v0.component, v1, v1.component)
            else: 
                move_vertices_to_new_component(dictionary, v1, v1.component, v0, v0.component)
            # print("\ndifferent components, should now be in the same component as first vertex\n")
            
        """
        print("\nMoved Component check\n")
        for key, val in dictionary.items():
            print("Key:", key)
            for elem in val:
                print("Val:", elem.name, elem.number, elem.component)
        """
        used_edges += 1
        """
        if con_type == "both":
            v0.set_both()
            v1.set_both()
        
        elif con_type == "ped":
            v0.set_pedCon()
            v1.set_pedCon()
        
        elif con_type == "bus":
            v0.set_busCon()
            v1.set_busCon()
            
        print("\nVertex value check:")
        print("Vertex 1:", v0.ped_con, v0.bus_con)
        print("Vertex 2:", v1.ped_con, v1.bus_con)
        """
    return used_edges


def move_vertices_to_new_component(dictionary, vertex1, oldkeyV1, vertex2, oldkeyV2):
    
    # switches vertices if v1 is in no component but v2 is
    if (oldkeyV1 == -1) and (oldkeyV2 != -1):
        tmp_v = vertex1
        tmp_key = oldkeyV1
        vertex1 = vertex2
        oldkeyV1 = oldkeyV2
        vertex2 = tmp_v
        oldkeyV2 = tmp_key
    
    if oldkeyV1 == oldkeyV2: # True when both vertices in same component (here "no component")
        dictionary[vertex1.number] = [vertex1, vertex2]
        dictionary[oldkeyV1].remove(vertex1)
        dictionary[oldkeyV2].remove(vertex2)
        vertex1.set_component(vertex1.number)
        vertex2.set_component(vertex1.number)
    else:   
        if oldkeyV2 != -1:
            # print("Vertices in dic at key", oldkeyV2, ":", dictionary[oldkeyV2])
            move_vertex_list = dictionary[oldkeyV2]

            for v in move_vertex_list:
                # print("Vertex:", v.number)
                v.set_component(vertex1.component)
            dictionary[oldkeyV1].extend(move_vertex_list)
            del dictionary[oldkeyV2]
        else:
            # print("Heyho")
            # print(oldkeyV2)
            # print(vertex2)
            # print(dictionary[oldkeyV2])
            dictionary[oldkeyV1].append(vertex2)
            dictionary[oldkeyV2].remove(vertex2)
            vertex2.set_component(vertex1.component)

    
    

def main():
    data = sys.stdin.read()
    # print(data)
    # print(type(data))
    solve(data)

if __name__ == "__main__":
    main()


#"samples-Practice/1.in"


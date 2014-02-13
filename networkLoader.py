__author__ = 'Piotrek'

from vertex import Vertex
from edge import Edge
import xml.etree.ElementTree as ET

class NetworkLoader:

    def load(self, networkFileName):
        net = ET.parse(networkFileName).getroot()
        vertices = self.__getVertices(net)
        edges = self.__getEdges(net, vertices)
        self.__addEdgesToVertices(vertices, edges)
        return vertices

    def __getVertices(self, net):
        plainJunctions = filter(lambda junction: junction.get('type') != 'internal', net.findall('junction'))
        vertices = {}
        for junction in plainJunctions:
            sumo_id = junction.get('id')
            vertices[sumo_id] = Vertex(sumo_id)
        return vertices
    
    def __getEdges(self, net, vertices):
        plainEdges = filter(lambda edge: edge.get('function') != 'internal', net.findall('edge'))
        return map(lambda edge: Edge(edge.get('id'), vertices[edge.get('from')], vertices[edge.get('to')]), plainEdges)
    
    def __addEdgesToVertices(self, vertices, edges):
        for edge in edges:
            vertices[edge.vertex1.sumo_id].edges.append(edge)
            
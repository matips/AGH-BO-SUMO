from SumoPathFinding.sumoPathFinding.cityMap import CityMap, Vertex, Edge

__author__ = 'Piotrek'

import xml.etree.ElementTree as ET

def loadNetwork(xmlFileName):
    net = ET.parse(xmlFileName).getroot()
    vertices = _getVertices(net)
    edges = _getEdges(net, vertices)
    _addEdgesToVertices(vertices, edges)
    return CityMap(vertices)

def _getVertices(net):
    plainJunctions = filter(lambda junction: junction.get('type') != 'internal', net.findall('junction'))
    vertices = {}
    for junction in plainJunctions:
        sumo_id = junction.get('id')
        vertices[sumo_id] = Vertex(sumo_id)
    return vertices

def _getEdges(net, vertices):
    plainEdges = filter(lambda edge: edge.get('function') != 'internal', net.findall('edge'))
    return map(lambda edge: Edge(edge.get('id'), vertices[edge.get('from')], vertices[edge.get('to')]), plainEdges)

def _addEdgesToVertices(vertices, edges):
    for edge in edges:
        vertices[edge.vertex1.sumo_id].edges.append(edge)
            
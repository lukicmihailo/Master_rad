'''
Created on Feb 16, 2014

@author: misa
'''
class Element(object):
    '''
    classdocs
    '''
    def __init__(self,name,text,position,size,colorSolid,colorLine,superElement,diagram):
        '''
        Constructor
        '''
        self.diagram = diagram
        self.name = name
        self.text = text
        self.position = position
        self.size = size
        self.colorSolid = colorSolid
        self.superElement = superElement
        self.elements = []
        self.links = []
        
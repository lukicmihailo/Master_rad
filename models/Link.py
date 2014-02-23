'''
Created on Feb 16, 2014

@author: misa
'''
from models import Element
class Link(Element):
    '''
    classdocs
    '''
    def __init__(self,typeLink):
        '''
        Constructor
        '''
        super.__init__()
        self.typeLink= typeLink
        self.element1 = None
        self.element2 = None
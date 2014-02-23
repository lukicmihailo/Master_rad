'''
Created on Feb 16, 2014

@author: misa
'''
from models.Projekat import Projekat
class Diagram(object):
    '''
    classdocs
    '''
    def __init__(self, name,elements):
        '''
        Constructor
        '''
        self.name = name
        self.projekat = Projekat()
        self.elements = []
        
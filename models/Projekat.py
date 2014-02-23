'''
Created on Feb 16, 2014

@author: misa
'''

class Projekat(object):
    '''
    classdocs
    '''
    def __init__(self, name,diagramCounts):
        '''
        Constructor
        '''
        self.name = name
        self.diagramsCount = diagramCounts
        self.diagrams= []
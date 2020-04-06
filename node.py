##############################
# Node
##############################

class Node:

    def __init__(self, key=None, parent=None, payload=None):
        self.key = key
        if ( isinstance( parent, Node) ):
            self.parent = parent
        self.depth = 0 if ( parent == None ) else ( parent.depth + 1 )
        self.payload = payload
        self.children = []
    
    def __repr__(self):
        repr_str = ""
        for n in range( 0, self.depth ):
            repr_str += "-"
        repr_str += f'({ self.key }, { self.payload })\n'
        for child in self.children:
            repr_str += f'{ child }'
        return repr_str

    def set_payload(self, payload):
        self.payload = payload
        return self

    def get_payload(self):
        return self.payload
    
    def add_child(self, child):
        if ( isinstance( child, Node ) ):
            self.children.append( child )
        return self

    def get_children(self):
        return self.children
    
    def get_child(self, key):
        for child in self.children:
            if ( child.key == key ):
                return child
        
        new_node = Node( key, self )
        self.add_child( new_node )
        return new_node
    
    def get_payloads(self):
        payloads = []
        if ( self.payload ): payloads.append( self.payload )
        for child in self.children :
            payloads += child.get_payloads()
        return payloads

    def copy(self):
        return Node( self.key, self.parent, self.payload )
        
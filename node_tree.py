from node import Node

##############################
# Node Tree
##############################

class NodeTree:

    def __init__(self):
        self.top_node = Node()

    def __repr__(self):
        return f'{ self.top_node }'
    
    def print(self):
        print( self )

    def add_list(self, word_list):
        for word in word_list:
            self.add_word( word )

    def add_word(self, word):
        current_node = self.top_node
        index = 0
        while index < len( word ):
            current_node = current_node.get_child( word[index] )
            index += 1

        current_node.set_payload( word )
    
    def search(self, search_str):
        current_node = self.top_node
        index = 0
        while index < len( search_str ):
            for child in current_node.children:
                if ( child.key == search_str[index] ):
                    current_node = child
            index += 1
        return current_node.get_payloads()
            


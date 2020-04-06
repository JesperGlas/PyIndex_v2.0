import time

from node_tree import NodeTree

def main():
    running = True

    ############################################################
    # Loading the word list from the file
    ############################################################
    timestamp = time.time()
    print( f'Loading words..' )
    with open('words.txt', 'r') as f:
        word_list = [ line.strip() for line in f ]
    word_count = 0
    for word in word_list:
        word_count += 1
    print( f'{ word_count } words loaded in { ( time.time() - timestamp ) } s')
    ############################################################

    ############################################################
    # Creating and loading the node tree
    ############################################################
    timestamp = time.time()
    print( f'Creating NodeTree' )
    node_tree = NodeTree()
    print( f'Loading NodeTree..' )
    node_tree.add_list( word_list )
    print( f'NodeTree loaded in { ( time.time() - timestamp ) } s')
    ############################################################

    ############################################################
    # Main loop of the demo
    ############################################################
    while running:
        search_str = str( input("Enter a search word: ") )

        ############################################################
        # Searching through the list by iterating word by word.
        # Gives a match if the search string is found at
        # the start of the word.
        ############################################################
        start_time = time.time()
        word_hits = []
        for word in word_list:
            if word[0:len(search_str)] == search_str:
                word_hits.append( word )
        elapsed_time = time.time()
        regular_search_time = elapsed_time - start_time
        print( f'{ len( word_hits ) } words found in { regular_search_time } s using regular search..')
        regular_search_list = word_hits
        ############################################################

        ############################################################
        # Searching through the node tree
        ############################################################
        start_time = time.time()
        node_search_list = node_tree.search( search_str )
        elapsed_time = time.time()
        node_search_time = elapsed_time - start_time
        print( f'{ len( node_search_list ) } words found in { node_search_time } s using node search..')
        ############################################################

        ############################################################
        # Print the lists of words found
        ############################################################
        print( "Regular search matches:" )
        for word in regular_search_list:
            print( word )

        print( "NodeTree matches:" )
        for word in node_search_list:
            print( word )
        ############################################################

        ############################################################
        # Performance information
        ############################################################
        print( f'NodeTree search performed { ( regular_search_time - node_search_time ) / regular_search_time * 100 } % faster than iterating through the list one word at a time.')

        ############################################################
        # Terminate loop
        ############################################################
        running = False


if __name__ == '__main__':
    main()
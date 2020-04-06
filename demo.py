import time

from node_tree import NodeTree

def main():
    running = True

    timestamp = time.time()

    print( f'Loading words..' )
    with open('words.txt', 'r') as f:
        word_list = [ line.strip() for line in f ]

    word_count = 0
    for word in word_list:
        word_count += 1
    print( f'{ word_count } words loaded in { ( time.time() - timestamp ) } s')

    timestamp = time.time()
    print( f'Creating NodeTree' )
    node_tree = NodeTree()
    print( f'Loading NodeTree..' )
    node_tree.add_list( word_list )
    print( f'NodeTree loaded in { ( time.time() - timestamp ) } s')

    while running:
        search_str = str( input("Enter a search word: ") )

        #####
        start_time = time.time()
        word_hits = []
        for word in word_list:
            if word[0:len(search_str)] == search_str:
                word_hits.append( word )
        elapsed_time = time.time()
        regular_search_time = elapsed_time - start_time
        print( f'{ len( word_hits ) } words found in { regular_search_time } s using regular search..')
        regular_search_list = word_hits

        #####

        start_time = time.time()
        node_search_list = node_tree.search( search_str )
        elapsed_time = time.time()
        node_search_time = elapsed_time - start_time
        print( f'{ len( node_search_list ) } words found in { node_search_time } s using node search..')

        ####

        print( f'NodeTree search performed { ( regular_search_time - node_search_time ) / regular_search_time * 100 } % faster than iterating through the list')

        for word in node_search_list:
            print( word )
        
        running = False


if __name__ == '__main__':
    main()
import time
from graphs_heuristics import *
from graphs import *
from search import *


from Random_string_generator import *
def main():
    nr = input("nr of cities is ")
    nr = int(nr)
    list1=[]
    for iterator in range (0,nr):
      x = random_string_generator()
      list1.append(x)
    nr_start = input("nr of the start city is ")
    nr_start = int(nr_start)
    if nr_start > nr:
      print ("Oops!  That was no valid number as it was greater than the number of cities.  Try again...")
      exit(1)
    nr_dest = input("nr of the city destination is ")
    nr_dest = int(nr_dest)
    
    if(nr_dest>nr ):
         print ("Oops!  That was no valid number as it was greater than the number of cities.  Try again...")
         exit(1) 
    
    other_map = RandomGraph(list1)
    print("path from {} to {}\n".format(str(list1[nr_start]),str(list1[nr_dest])))
    graph_pb_eucl = GraphProblemEuclidian(list1[nr_start], list1[nr_dest], other_map)

    t1 = time.time()
    path = astar_search(graph_pb_eucl).solution()
    t2 = time.time()
    print("astar_search cu euristica euclidiana {}\n",(t2-t1))
    print(path)

    graph_pb_manhattan = GraphProblemManhattan(list1[nr_start], list1[nr_dest], other_map)
    t3 = time.time()
    path2 = astar_search(graph_pb_manhattan).solution()
    t4 = time.time()
    print("astar_search cu euristica manahttan {}\n",(t4-t3))
    print(path2)


    t5 = time.time()
    path3 = recursive_best_first_search(graph_pb_eucl).solution()
    t6 = time.time()
    print("RBFS cu euristica euclidiana {}\n",(t6-t5))
    print(path3)

    t7 = time.time()
    path4 = recursive_best_first_search(graph_pb_manhattan).solution()
    t8 = time.time()
    print("RBFS cu euristica manhattan {}\n",(t8-t7))
    print(path4)

    test = open('random_graph_locations.txt','w') 
    test.write(str(getattr(other_map, 'locations', None)) )
    
    compare_searchers(problems=[graph_pb_eucl,graph_pb_manhattan],
                      header=['Searcher', 'A* h1(n)',
                              'A* h2(n)'], searchers=[
            astar_search,
            recursive_best_first_search])



  




if __name__ == "__main__":
    main()

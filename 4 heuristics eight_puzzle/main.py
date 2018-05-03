import time
from eight_puzzle import *
from search import *
import math


def x():
      a=(1, 2, 3, 4, 0, 6, 7, 8, 5)
      b=(1, 2, 3, 4, 5, 6, 7, 8, 0)
      return math.sqrt(sum((e - s)**2 for s, e in zip(a, b)))
#randuri si coloane mismatch


def y(t1, t2):
   sz = math.ceil(math.sqrt(len(t2)))
   sr = sc = 0
   for i in range(0, sz):
      # print(list(zip(t1[i * sz:(i + 1) * sz], t2[i * sz:(i + 1) * sz])))
       sr = sr + sum(s != g for (s, g) in zip(t1[i * sz:(i + 1) * sz], t2[i * sz:(i + 1) * sz]))
   for i in range(0, sz):
      # print(list(zip(t1[i:len(t1):sz], t2[i:len(t2):sz])))
       sc = sc + sum(s != g for (s, g) in zip(t1[i:len(t1):sz], t2[i:len(t2):sz]))
   return sr + sc

      
def main():
    
    print(x())
    print(y((7,2,4,5,0,6,8,3,1),(0,1, 2, 3, 4, 5, 6, 7, 8)))
    
    problem_miss = EightPuzzleMiss((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0))
    problem_mht = EightPuzzleMht((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0))
    
    problem_euclidian = EightPuzzleEuclidianDistance((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0))
    
    
    problem_rows_and_cols = ColAndRow((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0))
    
    t1 = time.time()
    path = astar_search(problem_miss).solution()
    t2 = time.time()
    t3 = time.time()
    path2 = astar_search(problem_mht).solution()
    t4 = time.time()
    
    
    
    t5 = time.time()
    path3 = astar_search(problem_euclidian).solution()
    t6 = time.time() 
    
    t7 = time.time()
    path4 = astar_search(problem_rows_and_cols).solution()
    t8 = time.time() 
     
    
    
    print(path, '\n', t2 - t1)
    print(path2, '\n', t4 - t3)
    print(path3, '\n', t6 - t5)
    print(path4, '\n', t8 - t7)
    """ Compare searchers """
    compare_searchers(problems=[problem_miss, problem_mht, problem_euclidian,problem_rows_and_cols ],
                      header=['Searcher', 'A* h1(n)',
                              'A* h2(n)','A* h3(n)','A* h4(n)'], searchers=[
            astar_search,
            recursive_best_first_search])


if __name__ == "__main__":
    main()

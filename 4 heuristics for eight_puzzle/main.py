import time
from eight_puzzle import *
from search import *
import math

#Functii pentru a verifica daca euristicile functioneaza
def misplaced(t1,t2):
  return sum(t1 != t2 for (t1, t2) in zip(t1, t2))

def manhattan (t1,t2):
  return sum(abs(t1 - t2) for t1, t2 in zip(t1, t2))
  
  
def euclidian(t1,t2):
      return math.sqrt(sum((e - s)**2 for s, e in zip(t1, t2)))

def missplacedLinesAndColumns(t1, t2):
   sz = math.ceil(math.sqrt(len(t2)))
   sr = sc = 0
   for i in range(0, sz):
      # print(list(zip(t1[i * sz:(i + 1) * sz], t2[i * sz:(i + 1) * sz])))
       sr = sr + sum(s != g for (s, g) in zip(t1[i * sz:(i + 1) * sz], t2[i * sz:(i + 1) * sz]))
   for i in range(0, sz):
      # print(list(zip(t1[i:len(t1):sz], t2[i:len(t2):sz])))
       sc = sc + sum(s != g for (s, g) in zip(t1[i:len(t1):sz], t2[i:len(t2):sz]))
   return sr + sc

   
def linearConflict(t1,t2):
        size = math.ceil(math.sqrt(len(t2)))
        line_sum = 0
        for i in range(0, size):
            line_sum = line_sum + sum(
                t1 != t2 for (t1, t2) in zip(t1[i * size:(i + 1) * size], t2[i * size:(i + 1) * size]))

        return line_sum

def nillson(t1,t2):
        manhattan_distance =  manhattan(t1,t2)
        sequence_score = 0
        center_squares_matrix_size = math.ceil((len(t2)//2))
        sequence_score += euclidian(t1,t2)
        for i in range (0,len(t2)):
            if i % center_squares_matrix_size == 0:
                sequence_score += 1
            elif i+1 != (i+1) % center_squares_matrix_size:
                sequence_score += 2
        return manhattan_distance + 3*sequence_score
   
   
   
        
def main():
    print("Rezultatul euristicilor pe un caz mai simplu:\n")
    print("euclidian distance   ",euclidian((1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,0,15),(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,0)))
    print("missplaced rows and columns   ",missplacedLinesAndColumns((1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,0,15),(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,0)))
    print("manhattan distance   ",manhattan((1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,0,15),(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,0)))
    print("misplaced tiles   ", misplaced((1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,0,15),(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,0)))
    print("linear conflict   ",linearConflict((1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,0,15),(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,0)))
    print("nilson sequence  ",nillson( (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0),(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0)))
    
    
    
    
    print("\ntest\n")
    problem_miss = EightPuzzleMiss((1,2,3,0,5,6,8,4,9,10,7,12,13,14,11,15), (1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15, 0))
    problem_mht = EightPuzzleMht((1,2,3,0,5,6,8,4,9,10,7,12,13,14,11,15), (1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15, 0))
    problem_euclidian = EightPuzzleEuclidianDistance((1,2,3,0,5,6,8,4,9,10,7,12,13,14,11,15), (1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15, 0))
    problem_rows_and_cols = ColAndRow((1,2,3,0,5,6,8,4,9,10,7,12,13,14,11,15), (1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15, 0))
    problem_linear_conflict = EightPuzzleLinearConflict((1,2,3,0,5,6,8,4,9,10,7,12,13,14,11,15), (1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15, 0))
    problem_nilsson = NilssonSeq((1,2,3,0,5,6,8,4,9,10,7,12,13,14,11,15),(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 0))
    
    
    t1 = time.time()
    print("\nmissplaced tiles solution")
    path = astar_search(problem_miss).solution()
    t2 = time.time()
    print(path, '\n', t2 - t1)
    
    t3 = time.time()
    print("\nmanhattan distance solution")
    path2 = astar_search(problem_mht).solution()
    t4 = time.time()
    print(path2, '\n', t4 - t3)
    
    
    t5 = time.time()
    print("\neuclidian distance solution")
    path3 = astar_search(problem_euclidian).solution()
    t6 = time.time() 
    print(path3, '\n', t6 - t5) 
    
    
    t7 = time.time()
    print("\nmissplaced rows and collumns solution")
    path4 = astar_search(problem_rows_and_cols).solution()
    t8 = time.time() 
    print(path4, '\n', t8 - t7) 
    
    
    t9 = time.time()
    print("\nlinear conflict solution")
    path5 = astar_search(problem_linear_conflict).solution()
    t10 = time.time()
    print(path5, '\n', t10-t9)

    t11 = time.time()
    print("\nnilsson sequence solution")
    path6 = astar_search(problem_nilsson).solution()
    t12 = time.time()
    print(path6, '\n', t12-t11)
    print("\n")
    """ Compare searchers """
    compare_searchers(problems=[problem_miss, problem_mht, problem_euclidian,problem_rows_and_cols,problem_linear_conflict],
                      header=['Searcher', 'A* h1(n)',
                              'A* h2(n)','A* h3(n)','A* h4(n)','A*h5(n)'], searchers=[
            astar_search,
            recursive_best_first_search])


if __name__ == "__main__":
    main()

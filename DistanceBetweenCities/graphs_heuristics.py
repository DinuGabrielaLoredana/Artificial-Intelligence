from graphs import GraphProblem
from distances import *

class GraphProblemEuclidian(GraphProblem):
  "h function is straight-line distance from a node's state to goal.euclidian   distance"
  def h(self,node):
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:                
                return int(euclidian_distance(locs[node], locs[self.goal]))
            return int(euclidian_distance(locs[node.state], locs[self.goal]))
        else:
            return infinity



      
class GraphProblemManhattan(GraphProblem):
    def h(self, node):
      locs = getattr(self.graph, 'locations', None)
      if locs:
            if type(node) is str:
               
                return int(manhattan_distance((locs[node], locs[self.goal])))
             
            return int(manhattan_distance(locs[node.state], locs[self.goal]))
            
      else:
              
              return infinity
              

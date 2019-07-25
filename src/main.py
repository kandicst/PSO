from src.ann_criterion import optimality_criterion
from time import time
from src.Star.StarPSO import StarPSO
from src.Ring.RingPSO import RingPSO
from src.Regular.PSO import PSO

def rosenbrock(X):
    x = X[0]
    y = X[1]
    a = 1. - x
    b = y - x*x
    return a*a + b*b*100.

if __name__ == '__main__':

    p = PSO(rosenbrock, num_dimensions=2, num_particles=100, max_iter=100)
    position, value = p.optimize()
    print('Optimum position: '+ str(position) + '\nOptimum value: '+ str(value))
import numpy as np

class Particle(object):
    '''  Represents a single particle in a swarm

    Parameters
    ------------
    pso : PSO
        Swarm
    position : nd-array
        Position in the swarm

    Attributes
    ------------
    v : float
        velocity of a particle
    p : nd-array
        best local position
    pmin : float
        value at the best position
    '''

    def __init__(self, pso, position=None):
        if position is None:
            self.position = np.array(np.random.uniform(-5, 5, pso.num_dimensions))  # brzina cestice
        else:
            self.position = position
        self.v = 0
        self.p = self.position.copy()
        self.pmin = np.inf
        self.pso = pso
        self.evaluate()

    def move(self):
        ''' Update velocity and move particle in ndimensional space '''
        # two random coefficients between (0,1)
        rp = np.random.rand()
        rg = np.random.rand()

        # calculate new velocity
        self.v = self.pso.omega * self.v + self.pso.cp * rp * (self.p - self.position) + self.pso.cg * rg * (
                self.pso.g - self.position)

        # update particle position
        self.position += self.v

    def evaluate(self):
        ''' Calculate value at current position '''
        fp = self.pso.criterion(self.position)
        if fp < self.pmin:
            self.p[:] = self.position
            self.pmin = fp
        if self.pmin < self.pso.min_value:
            self.pso.g[:] = self.position
            self.pso.min_value = self.pmin
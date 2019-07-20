from src.Regular.Particle import *

class RingParticle(Particle):
    ''' Particle in a Ring PSO

    Parameters
    ------------
    pso : PSO
        Swarm
    left : RingParticle
        left neighbour particle
    right : RingParticle
        right neighbour particle

    Attributes
    ------------
    v : float
        velocity of a particle
    position : nd-array
        best local position
    pmin : float
        value at the best position

    '''
    def __init__(self, pso, left=None, right=None):
        super().__init__(pso)
        self.left = left
        self.right = right

    def move(self):
        ''' Move a particle in a swarm space'''
        # two random coefficients between (0,1)
        rp = np.random.rand()
        rg = np.random.rand()
        if self.left.pmin < self.right.pmin:
            g = self.left.p
        else:
            g = self.right.p

        # calculate new velocity
        self.v = self.pso.omega * self.v + self.pso.cp * rp * (self.p - self.position) + self.pso.cg * rg * (
                g - self.position)

        # update particle position
        self.position += self.v
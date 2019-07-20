from Regular.Particle import *

class StarParticle(Particle):
    ''' Particle in a Star PSO

    Parameters
    ------------
    pso : PSO
        Swarm

    Attributes
    ------------
    v : float
        velocity of a particle
    position : nd-array
        best local position
    pmin : float
        value at the best position
    '''

    def __init__(self, pso):
        super().__init__(pso)

    def move(self):
        ''' moves all particles but the central one'''
        # two random coefficients between (0,1)
        rp = np.random.rand()
        rg = np.random.rand()

        self.v = self.pso.omega * self.v + self.pso.cp * rp * (self.p - self.position) + self.pso.cg * rg * (
                self.pso.center.position - self.position)
        self.position += self.v

    def move_center(self):
        '''moves the central particle according to the global minimum particle'''
        # two random coefficients between (0,1)
        rp = np.random.rand()
        rg = np.random.rand()

        # calculate new velocity
        self.v = self.pso.omega * self.v + self.pso.cp * rp * (self.p - self.position) + self.pso.cg * rg * (
                self.pso.g - self.position)

        # update particle position
        self.position += self.v

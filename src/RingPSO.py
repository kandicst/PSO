from src.PSO import *


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
        rp = np.random.rand()
        rg = np.random.rand()
        if self.left.pmin < self.right.pmin:
            g = self.left.p
        else:
            g = self.right.p
        self.v = self.pso.omega * self.v + self.pso.cp * rp * (self.p - self.position) + self.pso.cg * rg * (
                g - self.position)  # ubrzanje
        self.position += self.v


class RingPSO(PSO):
    ''' PSO where each particle's position is affected by its two
        immediate neighbours in the population

    Parameters
    ------------
    criterion : function
        function which optimum we want computed
    num_dimensions : int
        number of dimensions of PSO search space
    num_particles : int
        number of particles in a swarm
    max_iter : int
        maximum number of iteration of the PSO algorithm
    omega_min, omega_max : float
        inertia factor
    cp1,cp2 : float
        cognitive factor
    cg1, cg2 : float
        social factor
    const : bool
        if factor change during execution or not

    Attributes
    ------------
    particles : list { RingParticle}
        all particles in a swarm

    '''

    def __init__(self, criterion, num_dimensions=3, num_particles=60, max_iter=100,
                 omega_max=0.9, omega_min=0.4, cp1=2.5, cp2=0.5,
                 cg1=0.5, cg2=2.5, display=False, const=False):

        super().__init__(criterion, num_dimensions, num_particles, max_iter,
                         omega_max, omega_min, cp1, cp2, cg1, cg2,const, display)

    def populace_init(self):
        ''' Generate all particles'''
        first = RingParticle(self)
        self.particles.append(first)
        for i in range(1, self.num_particles):
            p = RingParticle(self, left=self.particles[i - 1])
            self.particles[i - 1].right = p
            self.particles.append(p)
        first.left = self.particles[-1]
        self.particles[-1].right = first

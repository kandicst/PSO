from Regular.PSO import PSO
from Star.StarParticle import StarParticle

class StarPSO(PSO):
    ''' PSO where one central node influences and is influenced
        by all other members of the population

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
    particles : list { StarParticle}
        all particles in a swarm
    center : StarParticle
        central particle
    center_value
        value of the central particle

    '''

    def __init__(self, criterion, num_dimensions=3, num_particles=60, max_iter=100,
                 omega_max=0.9,omega_min=0.4,cp1=2.5, cp2=0.5,
                 cg1=0.5, cg2=2.5, const=False, display=False):

        super().__init__(criterion, num_dimensions, num_particles, max_iter, omega_max,
                         omega_min, cp1, cp2, cg1, cg2,const, display)
        self.center = StarParticle(self)
        self.center_value = criterion(self.center.position)

    def optimize(self):
        ''' Finds the optimum'''
        if self.display:
            print("Start", "f(g)> ", self.min_value, " particles=", len(self.particles), " iters= ", self.max_iter)

        for i in range(self.max_iter + 1):

            # moving the non-central particles
            for particle in self.particles:
                particle.move()
                particle.evaluate()

            # moving the central particle
            self.center.move_center()
            self.center.evaluate()

            self.omega = self.omega_min + (self.omega_max - self.omega_min) / self.max_iter * (self.max_iter - i)
            self.cp = self.cp2 + (self.cp1 - self.cp2) / self.max_iter * (self.max_iter - i)
            self.cg = self.cg2 + (self.cg1 - self.cg2) / self.max_iter * (self.max_iter - i)

            self.display_info(i)

        return self.g, self.min_value

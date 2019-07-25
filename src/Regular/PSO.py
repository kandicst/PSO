import numpy as np
from src.Regular.Particle import Particle

class PSO(object):
    '''

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
        bound for values of inertia factor
    cp1,cp2 : float
        bound for values of cognitive factor
    cg1, cg2 : float
        bound for values of social factor
    lower, upper_bound : float
        bounds for particle position values in swarm
    const : bool
        if factor change during execution or not


    Attributes
    ------------
    g : numpy-array
        best global position of a particle at any time during execution
    min_value : float
        value at position g
    particles : list
        list of all particles in a swarm
    '''

    def __init__(self, criterion, num_dimensions=3, num_particles=60, max_iter=100, omega_max=0.9,
                 omega_min=0.4, cp1=2.5, cp2=0.5, cg1=0.5, cg2=2.5, const=False, display=False,
                 lower_bound=-10, upper_bound=10):

        self.criterion = criterion
        self.num_dimensions = num_dimensions
        self.num_particles = num_particles
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.g = np.array(np.random.uniform(-5, 5, num_dimensions))
        self.min_value = criterion(self.g)

        self.particles = []
        self.max_iter = max_iter
        self.populace_init()

        if const is True:
            self.omega, self.omega_max, self.omega_min = 0.72, 0.72, 0.72
            self.cp, self.cp1, self.cp2 = 1.49, 1.49, 1.49
            self.cg, self.cg1, self.cg2 = 1.49, 1.49, 1.49
        else:
            self.omega = omega_max
            self.omega_max = omega_max
            self.omega_min = omega_min

            self.cp = cp1
            self.cp1 = cp1
            self.cp2 = cp2

            self.cg = cg1
            self.cg1 = cg1
            self.cg2 = cg2

        self.display = display


    def display_info(self, iter_no):
        if self.display:
            print("Iteration> ", iter_no, " f(g)> ", self.min_value, "w=", self.omega, "cp=", self.cp, "cg=", self.cg)


    def populace_init(self):
        ''' Generates particles '''
        for i in range(self.num_particles):
            self.particles.append(Particle(self, lower_bound=self.lower_bound, upper_bound=self.upper_bound))


    def optimize(self):
        ''' Finds the optimum of the PSO function

        Returns
        ------------
        g : numpy-array
            one-dimensional array that contains the position of the best particle
        min_value : float
            value at the best position
        '''
        if self.display:
            print("Start", "f(g)> ", self.min_value, " particles=", len(self.particles),
                  " iters= ", self.max_iter)

        for i in range(self.max_iter + 1):
            # move each particle
            for particle in self.particles:
                particle.move()
                particle.evaluate()
            self.omega = (self.omega_max - self.omega_min) * ((self.max_iter - i) / self.max_iter) + self.omega_min
            self.cp = (self.cp1 - self.cp2) * ((self.max_iter - i) / self.max_iter) + self.cp2
            self.cg = (self.cg1 - self.cg2) * ((self.max_iter - i) / self.max_iter) + self.cg2

            self.display_info(i)

        return self.g, self.min_value

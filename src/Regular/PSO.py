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
        inertia factor
    cp1,cp2 : float
        cognitive factor
    cg1, cg2 : float
        social factor
    const : bool
        if factor change during execution or not


    Attributes
    ------------
    g : nd-array
        best global position of a particle at any time during execution
    min_value : float
        value at position g
    particles : list
        list of all particles in a swarm
    '''

    def __init__(self, criterion, num_dimensions=3, num_particles=60, max_iter=100, omega_max=0.9,
                 omega_min=0.4, cp1=2.5, cp2=0.5, cg1=0.5, cg2=2.5, const=False, display=False,
                 init_positions=None):

        self.criterion = criterion
        self.num_dimensions = num_dimensions
        self.num_particles = num_particles
        if init_positions is None:
            self.init_positions = []
        else:
            self.init_positions = init_positions
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
        ''' Generate particles '''
        for array in self.init_positions:
            p = Particle(self, array)
            self.particles.append(p)
        for i in range(self.num_particles - len(self.init_positions)):
            self.particles.append(Particle(self))


    def optimize(self):
        ''' Find the optimum'''

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

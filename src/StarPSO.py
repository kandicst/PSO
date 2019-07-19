from src.PSO import *


class StarParticle(Particle):

    def __init__(self, pso):
        super().__init__(pso)

    def move(self):
        """moves the particle in relation to central particle and local best position"""

        rp = np.random.rand()  # kognitivna komponenta (0,1)
        rg = np.random.rand()  # socijalna komponenta (0,1)

        self.v = self.pso.omega * self.v + self.pso.cp * rp * (self.p - self.position) + self.pso.cg * rg * (
                self.pso.center.position - self.position)  # ubrzanje
        self.position += self.v

    def move_center(self):
        """moves the central particle according to the global min particle"""

        rp = np.random.rand()  # kognitivna komponenta (0,1)
        rg = np.random.rand()  # socijalna komponenta (0,1)

        self.v = self.pso.omega * self.v + self.pso.cp * rp * (self.p - self.position) + self.pso.cg * rg * (
                self.pso.g - self.position)  # ubrzanje
        self.position += self.v


class StarPSO(PSO):

    def __init__(self, criterion, num_dimensions=3, num_particles=60, max_iter=100, omega_max=0.9,
                 omega_min=0.4,
                 cp1=2.5, cp2=0.5,
                 cg1=0.5, cg2=2.5, const=False, display=False):
        super().__init__(criterion, num_dimensions, num_particles, max_iter, omega_max, omega_min, cp1, cp2, cg1, cg2,
                         const, display)
        self.center = StarParticle(self)
        self.center_value = criterion(self.center.position)

    def optimize(self):
        # iteracije algoritma
        if self.display:
            print("Start", "f(g)> ", self.min_value, " particles=", len(self.particles), " iters= ", self.max_iter)

        for i in range(self.max_iter + 1):
            t1 = time()
            # iteracije pomeranja svake cestice
            for particle in self.particles:
                particle.move()
                particle.evaluate()

            # pomeranje centra topologije zvezde
            self.center.move_center()
            self.center.evaluate()

            self.omega = self.omega_min + (self.omega_max - self.omega_min) / self.max_iter * (self.max_iter - i)
            self.cp = self.cp2 + (self.cp1 - self.cp2) / self.max_iter * (self.max_iter - i)
            self.cg = self.cg2 + (self.cg1 - self.cg2) / self.max_iter * (self.max_iter - i)

            self.display_info(i, t1)

        return self.g, self.min_value

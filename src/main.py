from src.ann_criterion import optimality_criterion
from src.RingPSO import *
from src.StarPSO import *


def main():
    while True:
        print("Odabir pso algoritma:")
        print("1. PSO")
        print("2. PSO Ring")
        print("3. PSO Star")
        print("x. Izlaz")
        inn = input(">>")
        if inn == "x":
            return
        else:
            t1 = time()
            if inn == "1":
                g, f = test_pso()
            elif inn == "2":
                g, f = test_ring()
            elif inn == "3":
                g, f = test_star()
            else:
                print("Neodgovarajuci znak!")
                continue
            dt = time() - t1
            print("dt : ", dt, "fmin : ", f)
            print("g = ", g)


def input_parameters():
    max_iter = eval(input("Unesite broj iteracija: "))
    num_particles = eval(input("Unesite broj cestica: "))
    i = input("Unesite 1 za konstantne koeficijente ili bilo sta drugo za promenljive koeficijente: ")
    if i == "1":
        const = True
    else:
        const = False
    return max_iter, num_particles, const


def test_pso():
    max_iter, num_particles, const = input_parameters()
    p = PSO(optimality_criterion, num_dimensions=60, num_particles=num_particles, max_iter=max_iter, display=True,
            const=const)
    return p.optimize()


def test_ring():
    max_iter, num_particles, const = input_parameters()
    p = RingPSO(optimality_criterion, num_dimensions=60, num_particles=num_particles, max_iter=max_iter, display=True,
                const=const)
    return p.optimize()


def test_star():
    max_iter, num_particles, const = input_parameters()
    p = StarPSO(optimality_criterion, num_dimensions=60, num_particles=num_particles, max_iter=max_iter, display=True,
                const=const)
    return p.optimize()


if __name__ == '__main__':
    main()

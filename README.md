
# Particle Swarm Optimization 

[![license](https://img.shields.io/github/license/ssttefann/PSO.svg)]()

Implementing different topologies of a population based algorithm that finds the optimum of a given function



## Requirements
- Python 3.x
- NumPy 

## How it works

__Particle Swarm Optimization__ (PSO) is an algorithm developed by Dr. Eberhart and Kennedy, who tried to simulate the behaviour of a flock of birds.

Algorithm starts with the creating a population on randomized points in the observed space and determining values for given function at each point.

Afterwards, these particles are moved in relation to the position of the best particle, and their local best position.

The idea is that by doing this, particles will efficiently search the input space searching for the global optimum, where they will hopefully all gather in the end.

```
![Alt Text](https://upload.wikimedia.org/wikipedia/commons/e/ec/ParticleSwarmArrowsAnimation.gif)
```

## How to use it
Let's say that we want to find the optimum of a Rosenbrock function
```python

<img src="https://www.researchgate.net/profile/Laurent_Baumes/publication/236625120/figure/fig4/AS:299275956310021@1448364356683/Plot-of-the-Rosenbrock-function-for-two-dimensions.png"/>
def rosenbrock(X):  
    y = X[1]  
    a = 1. - x  
    b = y - x*x  
    return a*a + b*b*100.
```
All we need to to is initialize desired PSO with this function ( we can obviously change other parameters but they have default values)

```python
p = PSO(rosenbrock, num_dimensions=2, num_particles=100, max_iter=100)  
position, value = p.optimize()  
print('Optimum position: '+str(position) + '\nOptimum value: '+ str(value))
```
Since PSO is a stochastic algorithm, the output will slightly vary between executions, but it should look something like this: 
```python
Optimum position: [0.99999998 0.99999996]
Optimum value: 4.6320456692446925e-16
```



## References
- [Particle Swarm Optimization](https://en.wikipedia.org/wiki/Particle_swarm_optimization) on Wikipedia
- [A Comparative Study for Neighbourhood Topologies](https://pdfs.semanticscholar.org/8c2b/95cec5adcb4c9d577d56f765b0d54175384c.pdf) 
- [An Algorithmic Approach of Particle Swarm Optimization](https://pdfs.semanticscholar.org/11b4/3fdcf2decc96a7521c2c62084502a5b6cac0.pdf)

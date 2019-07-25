# Particle Swarm Optimization 

[![license](https://img.shields.io/github/license/ssttefann/PSO.svg)]()

Implementing different topologies of a population based algorithm that finds the optimum of a given function



## Requirements
- Python 3.x
- NumPy 


## Example of use
Let's say that we want to find the optimum of a Rosenbrock function
```python
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

The output  for many function won't be the same after every execution since PSO is a stochastic algorithm, but it will look something like this:
```python
Optimum position: [0.99999998 0.99999996]
Optimum value: 4.6320456692446925e-16
```



## References
- [Particle Swarm Optimization](https://en.wikipedia.org/wiki/Particle_swarm_optimization) on Wikipedia
- [A Comparative Study for Neighbourhood Topologies](https://pdfs.semanticscholar.org/8c2b/95cec5adcb4c9d577d56f765b0d54175384c.pdf) 
- [An Algorithmic Approach of Particle Swarm Optimization](https://pdfs.semanticscholar.org/11b4/3fdcf2decc96a7521c2c62084502a5b6cac0.pdf)


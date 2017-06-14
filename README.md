# MDP-Pacman

Automatic pacman player using Markov decision process.

## Execution

write the following command:

python pacman.py -p EstimatePacmanMdpAgent -x 1000 -n 1005 -k 1 -l smallGrid2 -a "iterations=50,discount=0.8"

Where:

- EstimatePacmanMdpAgent is the agent.
- x: is the number of training episodes
- n: is te number of executions - number of training episodes
- k: is the number of ghost
- l: is the grid (you can find the grids in the layouts folder)
- a: Number of iterations for the value-iterarion process
- discount: the discount value for the value-iterarion process

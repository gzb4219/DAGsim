import helpers
import constants
from simulation import Simulation
from plot import Plot

try:
    #Parameters: no_of_transactions, lambda, no_of_agents, alpha, latency, distance
    simu = Simulation(10, 2, 1, 0, 1, 0)

    simu.setup()

    simu.run()

except Exception as e:
    print(e)




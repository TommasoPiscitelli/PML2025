import pyro
import pyro.distributions as dist

def conditioned_scale_file(obs, guess=8.5): 
    weight = pyro.sample("weight", dist.Normal(guess, 1.))
    measurement = pyro.sample("measurement", dist.Normal(weight, 1.), obs=obs)
    return measurement

def eight_school_file(J, sigma, y=None):
    #your code here
    return


def eight_schools_noncentered_file(J, sigma, y=None):
    #your code here
    return

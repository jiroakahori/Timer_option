import numpy as np

def BM(init=0., deltat=0.1, T =10):
    num_timesteps = np.int(np.ceil(T/deltat))
    trajectory = np.zeros(num_timesteps)
    sampletimes = np.zeros(num_timesteps)

    trajectory[0] = init
    for k in range(1,num_timesteps):
        dW = np.sqrt(deltat)*np.random.normal(0,1,1)
        trajectory[k] = trajectory[k-1] + dW
        sampletimes[k] = sampletimes[k-1] + deltat

    return trajectory, sampletimes

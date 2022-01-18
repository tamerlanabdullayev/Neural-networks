import numpy as np
from numpy.linalg import matrix_power

events = ['rainy', 'sunny', 'cloudy']

transition = np.array([[0.5, 0.25, 0.25], [0.5, 0, 0.5], [0.25, 0.25, 0.5]])

rain_ = np.array([1, 0, 0])
sun_ = np.array([0, 1, 0])
cloud_ = np.array([0, 0, 1])

sun_pred = sun_.dot(matrix_power(transition, 7))


#stationary distribution
#talk about rock reconstruction (porosity, permeability)
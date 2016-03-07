import numpy as np
import math

def mean_squared_error( outputs, targets, derivative=False ):
    e = outputs - targets
    if derivative:
        return e * (2 / len(e))
    else:
        return np.sum( np.power(e,2) ) / len(e)
#end cost function

def sum_squared_error( outputs, targets, derivative=False ):
    if derivative:
        return outputs - targets 
    else:
        return 0.5 * np.sum( np.power(outputs - targets,2) )
#end cost function

def hellinger_distance( outputs, targets, derivative=False ):
    """
    The output signals should be in the range [0, 1]
    """
    root_difference = np.sqrt( outputs ) - np.sqrt( targets )
    
    if derivative:
        return root_difference/( np.sqrt(2) * np.sqrt( outputs ))
    else:
        return np.sum( np.power(root_difference, 2 )) / math.sqrt( 2 )
#end cost function


def cross_entropy_cost( outputs, targets, derivative=False ):
    """
    The output signals should be in the range [0, 1]
    """
    if derivative:
        return (outputs - targets) / (outputs * (1 - outputs)) 
    else:
        return -np.sum(targets * np.log( outputs ) + (1 - targets) * np.log(1 - outputs))
#end cost function


def exponential_cost( outputs, targets, derivative=False, tau = 2.0 ):
    core = np.sum( np.power(outputs - targets,2) ) / tau
    cost = np.exp( core )
    
    if derivative:
        return 2 / tau * (outputs - targets) * tau * cost
    
    return np.sum(cost) - 1
#end cost function

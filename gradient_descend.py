import numpy as np

# def gradient_descend(x,y):
#     number_of_iterations = 10000
#     m_curr = b_curr = 0
#     learning_rate = 0.08
#     n = len(x)
    
#     for i in range(number_of_iterations):
#         y_predicted = m_curr*x + b_curr
#         cost = 1/n*sum([val ** 2 for val in (y-y_predicted)])
#         md = -(2/n)*sum(x*(y-y_predicted))
#         bd = -(2/n)*sum((y-y_predicted))
#         m_curr = m_curr - learning_rate * md
#         b_curr = b_curr - learning_rate * bd
#         print("m {}, b {}, cost {} iteration {}".format(m_curr, b_curr,cost,i))

# x = np.array([1,2,3,4,5])
# y = np.array([5,7,9,11,13])
# gradient_descend(x,y)

# Exercise
import math
def gradient_descent(x, y):
    number_of_iterations = 1000000
    m_curr = b_curr = 0
    learning_rate = 0.0002
    n = len(x)
    cost_prev = 0

    for i in range(number_of_iterations):
        y_predicted = m_curr*x + b_curr
        cost = 1/n*sum([val ** 2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum((y-y_predicted))
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        check = math.isclose(cost_prev,cost, rel_tol=1e-09, abs_tol=0.0)
        if check is True:
            print("m {}, b {}, cost {} iteration {}, isclose {}".format(m_curr, b_curr,cost,i,check))
            break
        cost_prev = cost

x = np.array([92,56,88,70,80,49,65,35,66,67])
y = np.array([98,68,81,80,83,52,66,30,68,73])
gradient_descent(x,y)
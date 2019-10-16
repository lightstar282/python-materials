from scipy.optimize import minimize_scalar


def objective_function(x):
    return 3 * x ** 4 - 2 * x + 1


res = minimize_scalar(objective_function)
print(res)


def objective_function(x):
    return x ** 4 - x ** 2


res = minimize_scalar(objective_function, method="brent")
print(res)

res = minimize_scalar(objective_function, method="bounded", bounds=[-2, -1])
print(res)

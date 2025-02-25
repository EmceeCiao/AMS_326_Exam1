import numpy as np 

def cubic_fit(t_values, y_values, point_value): 
    """ 
    Function to both create the cubit fit function and print out the results achieved when evaluating the function at a specific point_value 

    Input: 
    t_values: Array of t values passed in for the points (A point is of the form (t, y))
    y_values: Array of y values passed in for the points of the form (A point is of the form (t, y))
    point_value: t value we are evaluating our quadratic fit for 

    Output: 
    prints the quadratic fit equation and the value of computing the quadratic fit for the t value passed in 
    """ 

    t_values = np.array(t_values) 
    y_values = np.array(y_values) 

    n = len(t_values) 

    A = np.vstack([np.ones(n), t_values, t_values**2, t_values**3]).T

    # Need to create A^TA and A^Tb and then solve these 

    A_TA = np.dot(A.T, A) 

    A_Ty = np.dot(A.T, y_values)  

    #Solves for the coefficients
    coeffs = np.linalg.solve(A_TA, A_Ty)    

    a_0 = coeffs[0] 
    a_1 = coeffs[1] 
    a_2 = coeffs[2]  
    a_3 = coeffs[3] 

    # print(f"P_3(t) = {a_0} + {a_1}t + {a_2}t^2 + {a_3}t^3\n")   
    # ans = a_0 + (a_1*point_value) + (a_2 * point_value**2) + (a_3 * point_value**3)
    # print(f"P_3(t = {point_value}) = {ans}")  
    return coeffs 

# For loop ran to see what values should be inputted into the array
# for i in range(1, 13): 
#     print(16 + (31 * i))

t_values = np.array([16, 47, 78, 109, 140, 171, 202, 233, 264, 295, 326, 357]) 
y_values = np.array([33, 34, 40, 51, 60, 69, 75, 74, 67, 56, 47, 38])


coeffs = cubic_fit(t_values, y_values, 6) 
total_days = 31 * 12 

days = [] 
for i in range (1, total_days + 1):  
    temp_estimate = np.polyval(coeffs[::-1], i)
    if (abs(temp_estimate - 64.89)) < 0.25: 
        print(f"Temperature of Day {i}: {temp_estimate}, is less than 0.25 away from our target 64.89") 
        days.append(i) 
print("\n")
for i in days: 
    print(f"Day {i} reaches within 0.25 of 64.89") 

     

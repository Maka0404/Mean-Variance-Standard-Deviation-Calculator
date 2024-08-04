import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
 
    matriz = np.array(list).reshape(3, 3)


    mean_axis1 = np.mean(matriz, axis=0).tolist()  
    mean_axis2 = np.mean(matriz, axis=1).tolist() 
    mean_flattened = np.mean(matriz).tolist() 

    variance_axis1 = np.var(matriz, axis=0).tolist()  
    variance_axis2 = np.var(matriz, axis=1).tolist() 
    variance_flattened = np.var(matriz).tolist()

    std_dev_axis1 = np.std(matriz, axis=0).tolist()  
    std_dev_axis2 = np.std(matriz, axis=1).tolist() 
    std_dev_flattened = np.std(matriz).tolist()  

    max_axis1 = np.max(matriz, axis=0).tolist() 
    max_axis2 = np.max(matriz, axis=1).tolist()
    max_flattened = np.max(matriz).tolist()

    min_axis1 = np.min(matriz, axis=0).tolist() 
    min_axis2 = np.min(matriz, axis=1).tolist() 
    min_flattened = np.min(matriz).tolist() 

    sum_axis1 = np.sum(matriz, axis=0).tolist() 
    sum_axis2 = np.sum(matriz, axis=1).tolist() 
    sum_flattened = np.sum(matriz).tolist() 

 
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [std_dev_axis1, std_dev_axis2, std_dev_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations
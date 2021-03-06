import math
import numpy as np

# евклидово расстояние между двумя точками
def euclidean_distance(A, B):
  if (isinstance(A, np.ndarray) == 1 & isinstance(B, np.ndarray) == 1):
    return math.sqrt(sum((A-B)**2))

# возвращает список индексов ближайших центров по каждой точке
def class_of_each_point(X, centers):
  m = len(X)
  k = len(centers)
   
  # матрица расстояний от каждой точки до каждого центра
  distances = [[euclidean_distance(centers[j], X[i]) for j in range(k)] for i in range(m)]
        
  # поиск ближайшего центра для каждой точки
  return np.argmin(distances, axis=1)

def kmeans(k, X):
  m, n = X.shape
  curr_iteration = prev_iteration = np.zeros(m) 
  mn=np.min(X, axis=0) 
  mx=np.max(X, axis=0) 
  centers = np.random.uniform(mn, mx, (k, n))
  # приписываем каждую точку к заданному классу
  curr_iteration = class_of_each_point(X, centers)
  while np.any(curr_iteration != prev_iteration):
    prev_iteration = curr_iteration
    # вычисляем новые центры масс
    for i in range(k):
      sub_X = X[curr_iteration == i,:]
      if len(sub_X) > 0:
        centers[i,:] = np.mean(sub_X, axis=0)
    # приписываем каждую точку к заданному классу
    curr_iteration = class_of_each_point(X, centers)
  return centers

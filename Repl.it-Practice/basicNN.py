import numpy as np

#i = [[2],[1]]
#w = [[2],[1]]
inputs = np.array([[2],[1]])
weights = np.array([[2],[1]])

#oo = np.dot(ii, ww)

#print(ii, ww, oo)
def neural_network(inputs, weights):
  i2 = inputs.T
  w2 = weights
  dotprod = np.dot(i2, w2)
  oput = np.tanh(dotprod)
  return oput.reshape(1,1)

output = neural_network(inputs, weights)

print(output)


import numpy as np
#l=[[1,2,3,4,6],[1,3,7,9]]
a=np.array([1,2,3,5],ndmin=5)
b=np.array([[1,2,3],[2,3,4]])
c=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
d=np.array([[[[1,2],[2,3]],[[4,5],[6,7]]],[[[8,9],[10,11]],[[12,13],[14,15]]]])
print(a.ndim)
#print(c[0,1,1])
#print(d[0,1,1,1])
print(a)
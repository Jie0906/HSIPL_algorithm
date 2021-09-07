import matplotlib.pyplot as plt
import numpy as np

def SID(apple,d_point):
    ril = (apple.reshape(x*y,z)).transpose()
    m = ril / (np.sum(ril,axis=0))
    n = d_point / (np.sum(d_point,axis=0))
    
    D_rd = m * (np.log(m / n))
    D_rd = np.sum(D_rd,axis=0)
    D_dr = n * (np.log(n / m))
    D_dr = np.sum(D_dr,axis=0)
    
    SID_rd = D_rd + D_dr
    SID_result = SID_rd.reshape(x,y)
    
    
    return SID_result


''' main '''
apple = plt.imread('apple.jpg')
plt.imshow(apple)
apple = np.double(apple)
x,y,z = apple.shape#取得x,y,z的值

d_point = plt.ginput()
d_point = apple[int(d_point[0][1]),int(d_point[0][0]), :].reshape(z, 1)
plt.close()

result = SID(apple,d_point)
#print(result)

'''輸出結果'''
plt.figure()
plt.imshow(result)
plt.show()


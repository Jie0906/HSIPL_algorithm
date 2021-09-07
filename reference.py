import matplotlib.pyplot as plt
import matplotlib.image as maping
import numpy as np


apple = maping.imread(r'C:\Users\user\Downloads\apple.jpg')

#plt.imshow(apple)
rd=rtemp=dtemp =0 
plt.imshow(apple)
dd = plt.ginput()
apple = np.array(apple,dtype = "d")
plt.close()

dd = apple[int(dd[0][1]),int(dd[0][0]),:]


x,y,z = apple.shape

temp = []
for i in range(x):  
    for j in range(y) :
        for k in range(z) :
            rd+= apple[i,j,k] * dd[k] 
            rtemp+= pow((apple[i,j,k]), 2)
            r = pow(rtemp,0.5)
            dtemp+= pow(dd[k], 2)
            d = pow(dtemp,0.5)
            ans = (rd/(r*d))   
        temp.append(ans)
        rd=rtemp=dtemp =0 
        
img = np.arccos(temp)
fin = img.reshape(x,y)
plt.imshow(fin,'gray')


    
            
            
            
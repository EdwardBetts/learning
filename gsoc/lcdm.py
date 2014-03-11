from astropy.io import fits
from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl
import sys

def lcdm(filename):
    f = fits.open(filename)
    print f.info()

    scidata = f[0].data

    m = scidata.mean()
    s = scidata.std()
    mx = scidata.max()
    val = m+0.5*(s)

    imdata = scidata
    imdata[imdata < val] = 0

    varX = imdata.var(axis=0, dtype = 'int32')
    varY = imdata.var(axis=1, dtype = 'int32')
    kX = np.trim_zeros(varX)
    kY = np.trim_zeros(varY)

    xv1 = varX[varX.size - np.trim_zeros(varX, 'f').size]
    xv2 = varX[np.trim_zeros(varX, 'b').size -1]
    
    yv1 = varY[varY.size - np.trim_zeros(varY, 'f').size]
    yv2 = varY[np.trim_zeros(varY, 'b').size -1]
    
    (s1,s2) = imdata.shape
    
    for i in range(0,s1):
        for j in range(0,s2):
            if (imdata[i,j] == mx):
                (cy,cx)= (i,j)
        if (varX[i] == xv1):
            dx1 = i
        if (varX[i] == xv2):
            dx2 = i
        if (varY[i] == yv1):
            dy1 = i
        if (varY[i] == yv2):
            dy2 = i
    print (cx,cy)
    print (dx1,dx2,dy1,dy2)
    
    #mpl.colors.Normalize(log,clip=True) #not sure why needed
    
    #plot image
    plt.axis([60,180,100,220])
    plt.imshow(imdata,cmap='gray')
    
    #mark center in blue cross
    plt.plot(cx,cy,'bx')
    
    #mark the axes in dashed lines
    dxx= [dx1,dx2]
    dyy= [dy1,dy2] #coordinates for plotting first axis
    
    m = (((dx1-dx2)*1.0)/(dy2-dy1))
    c = (cy-(m*cx))
    x = np.linspace(50,250,200)
    y = m*x+ c #function for plotting along second axis
    
    plt.plot(dxx,dyy,'r--')
    plt.plot(x,y,'g--')
    
    #save output
    plt.savefig("D:/learning/gsoc/outFinal.png")
    
if __name__ == '__main__':
    if(len(sys.argv)!=2):
        print "Usage: python lcdm.py <filename>"
        print "eg. python D:/learning/gsoc/lcdm.py D:/learning/gsoc/m86.fits"
        print "Error : insufficient arguments"
        sys.exit()
    lcdm(sys.argv[1])
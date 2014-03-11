
## GSoC 2014 - Code Problem, for Prof. Brunner (lcdm)

# Start with astropy. 
# Import, and load data provided in a specific format.

# In[5]:

from astropy.io import fits
f = fits.open("M86.fits")
print f.info()


# Out[5]:

#     Filename: M86.fits
#     No.    Name         Type      Cards   Dimensions   Format
#     0    PRIMARY     PrimaryHDU      57   (313, 313)   int16   
#     None
#     

# Convert to ndarray

# In[6]:

scidata = f[0].data


# Compute the mean, standard deviation and maximum, and decide a threshold 'val' based on that.

# In[7]:

m = scidata.mean()
s = scidata.std()
mx = scidata.max()
val = m+0.5*(s)


# Apply thresholding for noise removal. 
# A copy is made to avoid the need for loading the data from file everytime and for ease of debugging.

# In[8]:

imdata = scidata
imdata[imdata < val] = 0


# Compute the axis-wise variance and use that to find out the illumination values along principal axes. Since spread is symmetrical about the origin of light, it is realitively easy if we trim all zero values from front and back and take the edge values.

# In[9]:

varX = imdata.var(axis=0, dtype = int32)
varY = imdata.var(axis=1, dtype = int32)
kX = np.trim_zeros(varX)
kY = np.trim_zeros(varY)

xv1 = varX[varX.size - np.trim_zeros(varX, 'f').size]
xv2 = varX[np.trim_zeros(varX, 'b').size -1]

yv1 = varY[varY.size - np.trim_zeros(varY, 'f').size]
yv2 = varY[np.trim_zeros(varY, 'b').size -1]

(s1,s2) = imdata.shape


# Write output in 'FITS' format. Not sure if needed.

# In[10]:

#fits.writeto("output.fits",imdata);


# Find location(indices) of maxima, and for the  illumination values retrieved above. Range/Dimension information is available from above.

# In[11]:

for i in range(0,s1):
    for j in range(0,s2):
        if (imdata[i,j] == mx):
            (y,x)= (i,j)
    if (varX[i] == xv1):
        dx1 = i
    if (varX[i] == xv2):
        dx2 = i
    if (varY[i] == yv1):
        dy1 = i
    if (varY[i] == yv2):
        dy2 = i
print (dx1,dx2,dy1,dy2)


# Out[11]:

#     (69, 176, 109, 204)
#     

# Plot the modified image in grayscale, and apply patches to the Centre, and along the axes.

# In[12]:

#matplotlib.colors.Normalize(log,clip=True) #not sure why needed

#plot image
plt.axis([0,300,0,300])
plt.imshow(imdata,cmap='gray')

#mark center in blue cross
plt.plot(x,y,'bx')

#mark the axes in dashed lines
dx = [dx2,dx1]
dy = [dy1,dy2]
dxx= [dx1,dx2]
dyy= [dy1,dy2] #redundant, but makes it easier to understand
plt.plot(dx,dy,'g--')
plt.plot(dxx,dyy,'r--')

#save output
plt.savefig("outFinal.png")


# Out[12]:

# image file:

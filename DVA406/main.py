from pylab import plot, figure, hexbin, show
import numpy as np
import scipy.cluster as sp
import csv as csv




print "hello world";

i = [1,2,3,4,5];
for k in i :
    print k

for i in range(5, 1, -1):
    print i
    
print (np.float(5))


data = np.vstack((np.random.rand(150,2) + np.array([.5,.5]),np.random.rand(150,2)))
centroids,_ = sp.vq.kmeans(data,5)
idx,_ = sp.vq.vq(data,centroids)

'''
plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or',
     data[idx==2,0],data[idx==2,1],'og',
     data[idx==3,0],data[idx==3,1],'oy',
     data[idx==4,0],data[idx==4,1],'oc')
#plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
'''

def generate_x_y(prob_map):
    s = prob_map.shape
    x, y = np.meshgrid(np.arange(s[0]), np.arange(s[1]))
    return x.ravel(), y.ravel()

def heatmap(prob_map):
    x, y = generate_x_y(prob_map)
    figure()
    hexbin(x, y, C=prob_map.ravel())

heatmap(np.random.rand(100,300))

#x = np.linspace(-7, 7, 20)
#y = np.sin(x) * 0.5
#size = len(x)
#tar = y.reshape(size,1)
#print "size ="
#print size
#print "tar ="
#print tar

show()
'''

def prep(p1,p2):
    test_file_object = csv.reader(open('C:/Users/debajyoti/Downloads/267847/plot.csv','rb'))
    header = test_file_object.next() #removes headers
    print "file opened successfully"
    data = []
    for row in test_file_object :
        data.append(row)
    
    #convert list to array
    data = np.array(data)
    

    for row in data:
        k = row[1]
        p1.append(k)
        h=row[2]
        p2.append(h)       
        
    


p1=[]
p2=[]
prep(p1,p2)

p1=np.array(p1)
p2=np.array(p2)

print p1[0:5]
print p2[1:6]


p = np.vstack(p1)
centroids,_ = sp.vq.kmeans(p,29)
idx,_ = sp.vq.vq(p,centroids)


plot(p[idx==0,0],p[idx==0,1],'ob',
     p[idx==1,0],p[idx==1,1],'or',
     p[idx==2,0],p[idx==2,1],'og',
     p[idx==3,0],p[idx==3,1],'oy',
     p[idx==4,0],p[idx==4,1],'oc')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
x = np.linspace(-7, 7, 20)
y = np.sin(x) * 0.5
size = len(x)
tar = y.reshape(size,1)

show()

'''

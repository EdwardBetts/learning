function[y]=FixedPoint(func,maxError)%calcs root of a scalar closest to zero using Fixed point method
%input a function func in terms of x, the function must be predefined using syms,and
%the maximum acceptable error
%Fixed point method is used to approximate the root closest to zero and
%then outputs y the root approximation of the function, and plots a graph

syms x;
currentError=1000;
oldX=2;
newX=0;

gDashX=diff(func)
roots=solve(func)
rootA=roots(1)
doesConverge=subs(func,x,rootA)
y=abs(doesConverge)
if y>1
    fprintf('\n does not converge');
else
    while currentError>maxError
        newX=subs(func,x,oldX);
        currentError=abs((newX-oldX)/oldX);
        oldX=newX;
        newX=newX+1;
    end
    fprintf('\n root is %g',oldX);
    k=-50;
    z=1;
    while k<=50
        y(z)=subs(func,x,k);
        k=k+1;
        z=z+1;
    end
    x=[-50:1:50];
    plot(x,y)
end
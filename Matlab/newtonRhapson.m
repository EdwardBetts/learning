function[y]=newtonRhapson(func,firstGuess,error)%calcs roots of an scalar using Newtons method
%input a function func(x in the function must be predefined using syms),
%also input the init first guess of the root
%also input the acceptable error ex 0.0001
%Newtons method is used to approximate the root and the
%output y the root approximation of the function
currentError=1;
newX=0;
oldX=firstGuess;
syms x;

differentiatedFunction=diff(func);

while currentError>error
    
    fDashOfX=subs(differentiatedFunction,x,oldX);
    fOfX=subs(func,x,oldX);
    
    newX=oldX-((fOfX)/(fDashOfX));
    currentError=abs((newX-oldX)/oldX);
    oldX=newX;
end
y=newX;
k=-50;
z=1;
while k<=50
    m(z)=subs(func,x,k);
    k=k+1;
    z=z+1;
end
x=[-50:1:50];
plot(x,m);
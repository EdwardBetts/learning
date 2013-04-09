function[y]=biSectionalMethod(func,maxIter)%calcs root of a scalar closest to zero using Bisectional method
%input a function func(x in the function must be predefined using syms),and
%the maximum amount of desired iterations
%Bisectional method is used to approximate the root closest to zero and
%then outputs y the root approximation of the function, and plots a graph

k=1;
bigger=3;
numberIter=0;

syms x;

%find if increasing k makes eqn bigger or smaller
fOfXOne=subs(func,x,k);
k=k+1; % k=2
fOfXTwo=subs(func,x,k);
if fOfXTwo>fOfXOne
    bigger=1;%increasing k makes function bigger
else
    bigger=0;%increasing k makes function smaller
end
fOfX=fOfXTwo;

%find positive value
if fOfX<0
    while fOfX<0 
        fOfX=subs(func,x,k);
        if bigger==1
            k=k+1;
        else
            k=k-1;
        end
    end
    positiveGuess=k;
else
    k=2;
    positiveGuess=k;
end
k=1;
fOfX=fOfXOne;
%find negative value
if fOfX>0
    while fOfX>0 
        fOfX=subs(func,x,k);
        if bigger==1
            k=k-1;
        else
            k=k+1;
        end
    end
    negativeGuess=k;
else
    negativeGuess=k;
end

%use method
while numberIter<maxIter
    %sub values in
    fOfPositiveGuess=subs(func,x,positiveGuess);
    fOfNegativeGuess=subs(func,x,negativeGuess);
    
    %find midpoint of values
    midPoint=(positiveGuess+negativeGuess)/2;
    
    fOfMidPoint=subs(func,x,midPoint);
    if fOfMidPoint>0
        positiveGuess=midPoint;
    else
        negativeGuess=midPoint;
    end
    
    numberIter=numberIter+1;
end
k=-50;
z=1;
while k<=50
    y(z)=subs(func,x,k);
    k=k+1;
    z=z+1;
end
x=[-50:1:50];
plot(x,y)
y=midPoint;
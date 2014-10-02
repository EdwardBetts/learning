#include <iostream>

using namespace std;

int countDigits(int n)
{
    if (n < 10)
        return 1;
    int c = 0;
    while(n > 0)
    {
        n /= 10;
        c++;
    }
    return c;
}

string getNum(int t)
{
    switch(t)
    {
        case 0: return "zero"; break;
        case 1: return "one"; break;
        case 2: return "two"; break;
        case 3: return "three"; break;
        case 4: return "four"; break;
        case 5: return "five"; break;
        case 6: return "six"; break;
        case 7: return "seven"; break;
        case 8: return "eight"; break;
        case 9: return "nine";
    }
    return "ERROR"; // write error handler
}

string getPower(int l)
{
    switch(l)
    {
        case 1: return "."; break;
        case 2: return "ten"; break;
        case 3: return "hundred"; break;
        case 4: return "thousand";
    }
    return "ERROR"; // write error handler
}


int main()
{
    int n, len, rLen =1;
    string num;
    cout << "Enter Integer" << endl;
    cin>> n;
    bool sign;
    if(n < 0)
        sign = 0;
    else
        sign = 1;
    len  = countDigits(n);
    while(rLen <= len)
    {
        int t = n%10;
        n /= 10;
        string p = getNum(t) +" "+ getPower(rLen);
        cout<< p<<endl;
        rLen++;
    }
    return 0;
}

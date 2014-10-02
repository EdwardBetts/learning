#include <iostream>
#include <fstream>

using namespace std;

#define NX 9
#define NY NX //square dimensions

int grid[NX][NY]; //structure to store sudoku

int sRead(char fName[100])
{
    ifstream sGrid;
    int a,b;
    string line;
    sGrid.open(fName);
    if(sGrid.is_open())
    {
        int i = 0;
        while( getline(sGrid,line) )
        {
            //cout<<line<<endl;
            int j;
            char temp;
            for(j=0; j<NY; j++)
            {
                temp = line.at(j);
                if(temp == '\0')
                    continue;
                int k = temp-'0';
                if(k<1||k>9)
                    k = 0; //write 0(zero) in empty space

                grid[i][j] = k;
                //cout<<k<<"\t";
            }
            i++;
        }
        if(i<NX)
        {
            cout<<"CORRUPT FILE!";
            return -1;
        }
        //cout<<"Read Successful!"<<endl;

    }
    else{
        cout<<"Error in opening file";
        //cout<<endl<<fName;
        return -1;
    }
    sGrid.close();
    return 1;
}

void sDisp()
{
    int i,j;
    for(i=0;i<NX;i++)
    {
        for(j=0;j<NY;j++)
        {
            cout<<grid[i][j]<<"\t";
        }
        cout<<endl;
    }

}

int main()
{
    char fName[100]; //100 char name length
    cout<<"Enter full path of file to read (D:/codeblocks/sudoku.txt or sudoku.txt) :";
    cin>>fName;
    int t = sRead(fName);
    if(t==1)
        sDisp();

    return 0;
}


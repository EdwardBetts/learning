#include <iostream>
#include <fstream>

using namespace std;

#define NX 9
#define NY NX   //square dimensions, maybe use constants if not specified otherwise

//TODO wrap the global vars in a struct
int grid[NX][NY];   //structure to store sudoku
int blanks;         //to classify difficulty
int positions[NX*NY];   // to store position of blanks

int sRead(char fName[100])
{
    blanks = 0;
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
                {
                    k = 0;  //write 0(zero) in empty space
                    positions[blanks] = NX*i + j;    //row-wise traversal of the grid
                    blanks++;
                }
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

int sClassify()
{
    //TODO Classify difficulty of sudoku
    int c;
    cout<<"\nBlanks :"<<blanks<<endl;
    if(blanks<0 || (blanks>(NX*NY)))
        return 0;
    if(blanks > 68) c = 4;
    else    if(blanks > 65) c = 3;
            else    if(blanks > 61)   c=2;
                    else    c = 1;          //Re-calibrate limits
    return c;
    //TODO use switch for strings
    /*switch(c)
    {
        case 1: cout<<c;    return 1; break;    //easy
        case 2: cout<<c;    return 2; break;    //medium
        case 3: cout<<c;    return 3; break;    //hard
        case 4: cout<<c;    return 4;           //samurai
    }*/
}

int nCheck(int pos, int n) //for 9X9 only
{
    //check if valid number, i.e., check row, column and grid
    int col = pos % NX; //modulus for column
    int row = pos / NX; //division for row
    int grid = 0;
    switch(row)
    {
        case 1:
        case 2:
        case 3: switch(col)
        {
            case 1:
            case 2:
            case 3: grid = 1; break;

            case 4:
            case 5:
            case 6: grid = 2; break;

            case 7:
            case 8:
            case 9: grid = 3; break;
        } ; break;

        case 4:
        case 5:
        case 6: switch(column)
        {
            case 1:
            case 2:
            case 3: grid = 4; break;

            case 4:
            case 5:
            case 6: grid = 5; break;

            case 7:
            case 8:
            case 9: grid = 6; break;
        } ; break;

        case 7:
        case 8:
        case 9: switch(column)
        {
            case 1:
            case 2:
            case 3: grid = 7; break;

            case 4:
            case 5:
            case 6: grid = 8; break;

            case 7:
            case 8:
            case 9: grid = 9; break;
        } ; break;

        case default: grid = -1; //ERROR
    };


}

int sSolve()
{
    //TODO Solve sudoku
    cout<<positions;
    int uNum = 0;
    while(uNum<blanks)
    {
        int k = positions[uNum];
        int nFill =  sGrid[k]; //positions[uNum];
        sGrid[k] = nFill+1;
        int res = nCheck(k,sGrid[k]);
        if(res == 1)
        {
            uNum++; //proceed to next blank position
        }
        else
        {
            if(sGrid[positions] == 9)
            {
                //fall back to last number
                uNum--;
            }
        }
    }

}

int main()
{
    char fName[100]; //100 char name length
    cout<<"Enter full path of file to read (D:/codeblocks/sudoku.txt or sudoku.txt) :";
    cin>>fName;
    int t = sRead(fName);
    if(t!=1)
        return 0;
    sDisp();
    int lvl = 0;
    lvl = sClassify(); // to be called before solving
    if(lvl < 1 || lvl > 4)
    {
        cout<<"Error in difficulty level";
        return 0;   //use error codes for easier debug
    }
    cout<<"\nDifficulty Level :"<<lvl;
    sSolve();

    return 0;
}


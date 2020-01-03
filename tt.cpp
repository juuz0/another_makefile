#include<fstream>
using namespace std;

int main(){

    fstream fil("text.txt",ios::out);
    fil<<"x= 1 2 3 4 5"<<endl<<"y= 1 2 3 4 5";
    fil.close();
    return 0;
}

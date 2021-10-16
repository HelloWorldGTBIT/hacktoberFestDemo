#include<iostream>
using namespace std;
int i=10;
int main(){
  char c = 0;
  int numCount = 0;
  int alphaCount = 0;
  int spaceCount = 0;
  //cin>>c;
  c = cin.get();
  while(c!='$'){
    if(c==' ' || c=='\t' || c=='\n'){
      ++spaceCount;
    }
    else if(c>='0' && c<='9'){
      ++numCount;
    }
    else if((c>='A' && c<='Z') || (c>='a' && c<='z')){
      ++alphaCount;
    }
    c = cin.get();
  }
  cout<<spaceCount<<endl;
  cout<<numCount<<endl;
  cout<<alphaCount<<endl;
}

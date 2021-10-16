#include<iostream>

int main(int argc,char **argv){
  int n;
  std::cin>>n;
  for(int i=0;i<n;++i){
    //for ith row
    for(int j=0;j<=i;j++){
        std::cout<<"*";
    }
    std::cout<<" ";
    for(int j=0;j<n-i;j++){
        std::cout<<"*";
    }
    std::cout<<" ";
    for(int j=0;j<n-i;j++){
        std::cout<<"*";
    }
    std::cout<<" ";
    for(int j=0;j<=i;j++){
        std::cout<<"*";
    }
    std::cout<<std::endl;
  }
}

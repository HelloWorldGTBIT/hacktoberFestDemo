#include<iostream>

template <typename T>
void factorial(T a) {
  T i=a;
  for(i-=1;i>0;--i) { 
    a*=i;
    if (a<0) break;
  }
  if (a<0) std::cout << "an overflow when using a " << sizeof(a) << " byte integer\n";
  else std::cout << a << "\n";
}
int main(int argc, char **argv) {
  using T = int;
  T a;
  std::cin>>a;
  std::cout << "The factorial of " << a << " is ";
  factorial(a);
  return 0;
}

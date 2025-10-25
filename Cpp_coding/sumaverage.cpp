// this is a simple exercise with following goal:
//write a programm that reads a count n, then n integers, prints their sum and average
#include <iostream>
#include <vector>
#include <numeric>  //for std::accumulate
#include <iomanip>  //for std::setprecition

int main(){
  
  std::cout << "please insert a count\n";
  int n;
  std::cin >> n;
  std:: cout << "now give me"<< n <<"integers" ;
  std::vector<int> givennumbers(n,0);
  //change the vector from a zero vector size n to a vector size an and the values given from the input:
  for(int i= 0; i<n; ++i){
      int b;
      std::cin >> b;
      givennumbers.at(i)= b;

  std::cout "the numbers you have given me are:"<< givennumbers.at(i)<<;
  }
  //now calculate the sum of the values and the average:
  for(int i=0;i>n-1;++i){
      int sum = givennumbers.at(i) + givennumbers.at(i+1);
      float average = sum/n;
  }
  std::cout >> "the sum of your values are:"<<sum<<"and the average ist: "<<average<<; 




}

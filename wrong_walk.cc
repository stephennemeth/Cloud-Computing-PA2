#include <iostream>
using std::cin;
using std::cout;
#include <string>
using std::string;

int main() {
    string name1,name2;
    std::cout << "Enter a name:";
    getline(std::cin,name1);
    std::cout << "Enter a name:";
    getline(std::cin,name2);
    std::cout << name2 + " and " + name2 + " went for a walk.\n" ;
    std::cout << "This is the wrong submission file, but has the same name walk.cc, and outputs name2 twice so score should be 1 out of 2" << std::endl;
}
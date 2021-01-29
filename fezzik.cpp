#include <fstream>
#include <string>
#include <iostream>

int main(int argc, char** argv)
{

  std::ifstream f("fezzik.txt");

  if (f.is_open())
      std::cout << f.rdbuf();

  return 0;
}

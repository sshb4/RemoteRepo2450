#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {

    std::srand(std::time(nullptr));

    std::cout << "10 Random numbers generated" << std::endl;

    for (int i = 0; i < 10; ++i) {
        int random_number = std::rand() % 100; 
        std::cout << random_number << std::endl;
    }
    return 0;
}

//g++ test.cpp -o test
//./test
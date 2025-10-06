#include <iostream>
#include <random>

int main() {

    std::mt19937 rng(std::random_device{}());

    std::cout << "10 Random numbers generated" << std::endl;

    for (int i = 0; i < 10; ++i) {
        int random_number = rng() % 100; 
        std::cout << random_number << std::endl;
    }

    return 0;
}

//g++ random.cpp -o random 
//./random
#include <iostream>
#include <vector>

using namespace std;

int count_neurons[] = {1, 3, 1}; // count of neurons in each layer

class Neuron{
    public:
        vector<float> weights; 
        float bias;
};


class Array{
    public:
        int rows;
        int cols;
        float *data;

};

class layer{
    public:
        vector<Neuron> neurons[];
};


// transposition method for array struct


int main(){
    float a = 0.1; // learning rate
    int training_steps = 50;
    int x[] = {1, 2, 3};
    int y[] = {4, 8, 12};

    // for (int training_step = 0; training_step < training_steps; i++){
    //     for (int layer = )
    // })

}








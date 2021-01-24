// utility functions

#include "utils.h"
#include <cstdlib>

double randDouble(double min, double max)
{
    // random double between min and max
    double range = (max - min); 
    double div = RAND_MAX / range;
    return min + (rand() / div);
}



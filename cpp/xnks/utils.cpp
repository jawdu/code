// utility functions

#include "utils.h"
#include <algorithm>
#include <cmath>
#include <cstdlib> 				
#include <string>
#include <vector>

static bool abs_compare(double a, double b)
{
    return (std::abs(a) < std::abs(b));
}

double randDouble(double min, double max)
{
    // random double between min and max
    double range = (max - min); 
    double div = RAND_MAX / range;
    return min + (rand() / div);
}

double maxF(int nF, std::vector<double> a)
{
    double aF = 0.0;
    for (int p = 0; p < nF; p++)
    {
        aF = aF + *max_element(a.begin(), a.end(), abs_compare);
    }
    aF = aF / nF;
    return aF;
}



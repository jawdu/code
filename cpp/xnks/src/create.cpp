// creating sound waves

#include "create.h"
#include "utils.h"
#include <vector>
#include <cmath>
#include <vector>

std::vector<double> makeF(int nF)       // will hopefully depreciate
{
    std::vector<double> f;

    for (int p = 0; p < 10; p++)
    {
        double f1 = randDouble(20.0, 600.0);
        for (int q = 0; q < 6; q++)
        {
            // 5 and 2, who knows
            f.push_back((5+q)*f1 / (2+q));
        }
    }
    return f;
}

std::vector<double> makeA(int nF)       // will hopefully depreciate
{
    std::vector<double> a;
    
    for (int p = 0; p < nF; p++)
    {
        a.push_back(randDouble(0.2, 0.8));
    }
    return a;
}

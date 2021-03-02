// utility functions

#include "utils.h"

static bool abs_compare(double a, double b)
{ return (std::abs(a) < std::abs(b)); }

double randDouble(double min, double max)
{           // random double between min and max
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_real_distribution<double> distrib(min, max);    
    double num = distrib(mt);    
    return num;
}

double maxF(int nF, std::vector<double> a)
{
    double aF = 0.0;
    for (int p = 0; p < nF; p++)
    { aF = aF + *max_element(a.begin(), a.end(), abs_compare); }
    aF = aF / nF;
    return aF;
}

void addnoise(int N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // add some noise/crackle/etc
}

void normaliser(int N, double F, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // otherwise use multiplier based on max value. F adds factor from outside.

    double lmax = *max_element(lChannel.begin(), lChannel.end(), abs_compare);
    double rmax = *max_element(rChannel.begin(), rChannel.end(), abs_compare);
    double lrmax = std::max(lmax, rmax);
    if (lrmax > 1.0) {        
        double factor = lrmax * F;           
        for (int p = 0; p<N; p++)
        {
             lChannel[p] = lChannel[p] / factor;   
             rChannel[p] = rChannel[p] / factor;   
        }
    }
    // else, if want to apply e.g. F blanketly
}



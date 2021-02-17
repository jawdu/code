// utility functions

#include "utils.h"
#include <algorithm>
#include <cmath>
#include <vector>

static bool abs_compare(double a, double b)
{ return (std::abs(a) < std::abs(b)); }

double randDouble(double min, double max)
{  // random double between min and max
    double range = (max - min); 
    double div = RAND_MAX / range;
    return min + (rand() / div);
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
{
    // add some noise/crackle/etc
}

void normaliser(int N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // add normalisation check. say if <10 points >1, just change each of them to 0.98
    // otherwise use multiplier based on max value
    // NOT TESTED with actual > 1.0 yet

    int lc = 0;
    int rc = 0;
    for (int p = 0; p < N; p++)
    {
        if (lChannel[p] > 1.0) { lc++; }
        if (rChannel[p] > 1.0) { rc++; }
    }
    if ((lc + rc) > 0) {
        double lmax = *max_element(lChannel.begin(), lChannel.end(), abs_compare);
        double rmax = *max_element(rChannel.begin(), rChannel.end(), abs_compare);
        double factor = std::max(lmax, rmax);

        for (int p = 0; p<N; p++)
        {
             lChannel[p] = lChannel[p] / factor;   
             rChannel[p] = rChannel[p] / factor;   
        }
    }
}

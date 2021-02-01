// sound control.

#include "scntrl.h"
#include "utils.h"

#include <cmath>
#include <vector>

void smain(int N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // this is the main point of entry for making sound.


    /* part 1: make arrays to control events. or just make a class.
        1: time (integer, so index for lChan, rChan start point of event)
        2: pan (?) maybe integer ok to save memory (in range e.g. -100-100)
        3+: some to characterise the event now. maybe one will be used to forward ref. chains
    */

    int nF = 60; // NOTE makeF fixed for use of 60
    std::vector<double> a = makeA(nF);
    std::vector<double> f = makeF(nF);
    double aF = maxF(nF, a) * nF;

    for (int n = 0; n < N; n++)                                         
    {
        double v = 0.0;
        for (int p = 0; p < nF; p++)
        {
            v = v + a[p]*cos(6.28*f[p]*n/44100.0);
        }
        // try aF not nF
        lChannel.push_back(v/(double)aF);
        rChannel.push_back(v/(double)aF);
    }
}

std::vector<double> makeF(int nF)
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

std::vector<double> makeA(int nF)
{
    std::vector<double> a;
    
    for (int p = 0; p < nF; p++)
    {
        a.push_back(randDouble(0.2, 0.8));
    }
    return a;
}



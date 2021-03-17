// functions to do with arranging the sound events

#include "arrange.h"
#include "create.h"
#include "utils.h"

std::vector<int> morletEvents(int& N, double lambda, int nev)
{           // make events for morlet. define N by last event + 10 seconds
    std::vector<int> mev;
    int time = 44000;
    mev.push_back(time);        // remember this! 0th event

    for (int p = 0; p < (nev-1); p++)          // keep this -1 because of 0th event
    {   
        time += 44000 * -1 * (int)log(randDouble(0.0001, 1.0) / lambda);   // after knuth
        mev.push_back(time);
    }

    N = mev[nev-1] + 500000;
    return mev;
}

std::vector<double> morletOmegas(int nom)
{           // make set of omegas: points on a 2.pi sin (so returns to start point roughly)
    std::vector<double> mos;
    for (int p = 0; p < nom; p++)
    {       // last randDouble term just to make slightly irregular
        mos.push_back(1000.0 + (500.0 * sin(p * 6.28 / nom) * randDouble(0.9, 1.1)));
    }      
    return mos;
}

std::vector<int> mdroneEvents(int& N, double lambda, int nev)
{
    std::vector<int> mev;
    int time = 44000;
    mev.push_back(time);
    for (int p = 0; p<(nev-1); p++)
    {
        time += 44000 * (-1 * (int)log(randDouble(0.0001, 1.0) / lambda) + 3); // 3s + poisson interval
        mev.push_back(time);
    }
    N = mev[nev-1] + 500000;
    return mev;
}

std::vector<double> mdroneOmegas(int nom)
{
    std::vector<double> mos;
    for (int p = 0; p < nom; p++)
    {
        mos.push_back(700.0 * randDouble(0.8, 1.2));
    }
    return mos;
}

std::vector<int> shannonEvents(int& N, double lambda, int pfact, int nsev)
{
    std::vector<int> sev;
    int time = 20000;
    sev.push_back(time);
    for (int p = 0; p < (nsev-1); p++)
    {
        time += (int)(-pfact * log(randDouble(0.0001, 1.0) / lambda));    
        sev.push_back(time);
    }
    N = sev[nsev-1] + 500000;
    return sev;
}


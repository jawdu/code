// functions to do with arranging the sound events

#include "arrange.h"
#include "create.h"
#include "utils.h"
#include "wavelets.h"
#include <cmath>
#include <vector>

#include <iostream>

std::vector<int> mevents(int& N)
{           // make events for morlet. define N by last event + 10 seconds
    std::vector<int> mev;
    int time = 44000;
    double lambda = 12.0;               //  average interval
    mev.push_back(time);

    for (int p = 0; p < 5; p++)
    {   
        time += 44000 * -1 * (int)log(randDouble(0.0001, 1.0) / lambda);   // after knuth
        mev.push_back(time);
    }
    
    int nmev = static_cast<int>(mev.size());
    N = mev[nmev-1] + 500000;
    return mev;
}

std::vector<double> momegas(int nmev)
{           // make set of omegas. for large nmev, fix mos.num at say 10.
    std::vector<double> mos;
    for (int p = 0; p < nmev; p++)
    {
        mos.push_back(randDouble(600.0, 1200.0));       // bit placeholdery
    }      
    return mos;
}

void lcmorlet(int N, std::vector<int> mev, std::vector<double> mos, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // arrange Lower Case Morlet wavelets. 
    int z = 10*44100;           // range of wavelets
    int nmev = static_cast<int>(mev.size());
    for (int m = 0; m < nmev; m++)
    {
        // decide which mos to use.
        int q = m;       // placeholder
        for (int n = 0; n < z; n++)                                         
        {
            double t = n / 44100.0;
           // add a pan term (i.e. s.t. lPan + rPan = 1.0. noisy morlet: add small random onto omega below
            lChannel[n+mev[m]] += morlet(t-5.0, mos[q]);    
            rChannel[n+mev[m]] += morlet(t-5.0, mos[q]);    
        }
    }
}

void mtest(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // test morlet wavelets
    for (int n = 0; n < N; n++)                                         
    {
        double t = n / 44100.0;
        double omega = 900.5;        // frequency term. [could add small random noise here for fun]
        lChannel.push_back(morlet(t-5.0, omega));    
        rChannel.push_back(morlet(t-5.0, omega));    
    }
}

void placeholder(int N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{            // the original wave maker. hang on to for testing for now
    int nF = 60; // NOTE makeF fixed for use of 60. but this will depreciate anyway.
    std::vector<double> a = makeA(nF);     
    std::vector<double> f = makeF(nF);      
    double aF = maxF(nF, a) * nF;

    for (int n = 0; n < N; n++)                                         
    {
        double v = 0.0;
        for (int p = 0; p < nF; p++) {  v = v + a[p]*cos(6.28*f[p]*n/44100.0); }
        lChannel.push_back(v/(double)aF);
        rChannel.push_back(v/(double)aF);
    }
}


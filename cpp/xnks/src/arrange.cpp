// functions to do with arranging the sound events

#include "arrange.h"
#include "create.h"
#include "utils.h"
#include "wavelets.h"
#include <cmath>
#include <vector>

std::vector<int> mevents(int& N)
{
    // make events for morlet. define N by last event + 10 seconds
    std::vector<int> mev;
    me.push_back(44000);

    // some more events here

    int nmev = static_cast<int>(mev.size());
    N = mev[nmev] + 440000;

    return mev;
}

std::vector<double> momegas(int nmev)
{
    // make set of omegas
    std::vector<double> mos;
    mos.push_back(900);
    return mos;
}


void mtest(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // test morlet wavelets
    // also means need to stop push_back, instead populate lrChannel elsewhere
    // do 'feldmanny' OR do a droney thing to test arranging structure. lower-case morlet?

    for (int n = 0; n < N; n++)                                         
    {
        double t = n / 44100.0;
        double omega = 900.5;        // frequency term. [could add small random noise here for fun]
        // add a pan term (i.e. s.t. lPan + rPan = 1.0. noisy morlet: add small random onto omega below
        lChannel.push_back(morlet(t-5.0, omega));    
        rChannel.push_back(morlet(t-5.0, omega));    
    }
}

void placeholder(int N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // the original wave maker. hang on to for testing for now
    int nF = 60; // NOTE makeF fixed for use of 60. but this will depreciate anyway.
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
        lChannel.push_back(v/(double)aF);
        rChannel.push_back(v/(double)aF);
    }
}



/*

    // use [statistical distribution] to obtain *time-gaps* between events rather than test at each time step

void sequence(){
    // make vector of start_time
    // make vector of pan (len = len(start_time) [assuming constant pans]
    // make vector of characteristic of events (len = integer * start_time) [more than 1 characteristic per event?]
    // ------- number terms in fourier expansion
    // ------- hmm, maybe here have a seed value for later stuff (frequency or amplitude...? if time (in)dep>
}

*/



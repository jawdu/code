// functions to do with arranging the sound events

#include "arrange.h"
#include "create.h"
#include "utils.h"
#include "wavelets.h"

std::vector<int> mevents(int& N, double lambda, int nev)
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

std::vector<double> momegas(int nom)
{           // make set of omegas. 
    std::vector<double> mos;
    for (int p = 0; p < nom; p++)
    {
        mos.push_back(randDouble(400.0, 1500.0));       // placeholdery.
    }      
    return mos;
}

void lcmorlet(int N, std::vector<int> mev, std::vector<double> mos, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // arrange Lower Case Morlet wavelets. 
    int z = 10*44100;           // range of wavelets (10 = seconds, -5 to 5)
    int nmev = static_cast<int>(mev.size());
    int nmog = static_cast<int>(mos.size());
    for (int m = 0; m < nmev; m++)
    {
        int q = m % nmog;
        double pan = randDouble(-0.3, 0.3);       
        for (int n = 0; n < z; n++)                                         
        {
            double t = n / 44100.0;

            lChannel[n+mev[m]] += (1.0 + pan) * morlet(t-5.0, mos[q]);    
            rChannel[n+mev[m]] += (1.0 - pan) * morlet(t-5.0, mos[q]);    
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



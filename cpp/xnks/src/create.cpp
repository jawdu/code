// creating sound waves

#include "create.h"
#include "utils.h"
#include "wavelets.h"

void morletOne(int N, std::vector<int> mev, std::vector<double> mos, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // add Morlet wavelets. but turning into hybrid. maybe rename waveletsOne
    int z = 10*44100;           // range of wavelets (10 = seconds, -5 to 5)
    int nmev = static_cast<int>(mev.size());
    int nmog = static_cast<int>(mos.size());
    for (int m = 0; m < nmev; m++)
    {
        int q = m % nmog;       // maybe a check that nmog < nmev needed
        double pan = randDouble(-0.3, 0.3);
        double s = randDouble(-1.0, 1.0);   
        for (int n = 0; n < z; n++)                                         
        {
            double t = n / 44100.0;
            if (s < 0) {            
                lChannel[n+mev[m]] += (1.0 + pan) * morlet(t-5.0, mos[q]);    
                rChannel[n+mev[m]] += (1.0 - pan) * gabor(t-5.0, mos[q]);    
            } else {
                rChannel[n+mev[m]] += (1.0 - pan) * morlet(t-5.0, mos[q]);    
                lChannel[n+mev[m]] += (1.0 + pan) * gabor(t-5.0, mos[q]);    
            }
        }
    }
}

void shannonOne(int N, std::vector<int> sev, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // e.g. shannon wavelet... have to rescale t for audbiel frequency, then try for large number of events.
    // also multiply each by (+-)0.3, function is asymmetrical +-.
    // double shannon(double t, double omega) omega: to get into audible freq zone.
    
    int z = 7*44100;
    int nsev = static_cast<int>(sev.size());
    for (int m = 0; m < nsev; m++)
    {
        double pan = randDouble(-0.5, 0.5);
        double s = 0.7;
        // double s = randDouble(-1.0, 1.0);       // just want +- 0.3
        double omega = randDouble(300, 1200);
        for (int n = 0; n < z; n++)
        {
            double t = omega * (n/44100.0 - 3.5);
            lChannel[n+sev[m]] += (1.0 + pan) * s * shannon(t);
            rChannel[n+sev[m]] += (1.0 - pan) * s * shannon(t);
        }
    }
}


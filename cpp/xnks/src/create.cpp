// creating sound waves

#include "create.h"
#include "utils.h"
#include "wavelets.h"

void morletOne(int N, std::vector<int> mev, std::vector<double> mos, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // add Morlet wavelets 

    int z = 10*44100;           // range of wavelets (10 = seconds, -5 to 5)
    int nmev = static_cast<int>(mev.size());
    int nmog = static_cast<int>(mos.size());
    for (int m = 0; m < nmev; m++)
    {
        int q = m % nmog;       // maybe a check that nmog < nmev needed
        double pan = randDouble(-0.3, 0.3);       
        for (int n = 0; n < z; n++)                                         
        {
            double t = n / 44100.0;

            lChannel[n+mev[m]] += (1.0 + pan) * morlet(t-5.0, mos[q]);    
            rChannel[n+mev[m]] += (1.0 - pan) * morlet(t-5.0, mos[q]);    
        }
    }
}


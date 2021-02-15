// sound control.

#include "arrange.h"
#include "create.h"
#include "scntrl.h"
#include "utils.h"
#include "wavelets.h"

#include <cmath>
#include <vector>

void smain(int N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // main point of entry for making sound. by the end, created and populated lChannel, rChannel
    
    /*     
            arrange.cpp to hold functions that arrange, characterise events, etc.
            create.cpp to hold functions to derive sound events, i guess?
            eventually may be arbitrary length - i.e. when the sound ends is determined stochasticly on the fly(ish)

            idea for start: use stochastic framework for *individual* sine waves (i.e 0-pi/2) with a, f random
            so make dense texture. just over shortish time (like a minute?). density with a distribution with 
            imposed-finite tail.  **  normalisation at end.

            ** WAVELETS??!! ** morlet wavelet.

    */

    // basically all that follows will hopefully go, to be replaced by function calls
    // keeping it a level deeper than main.cpp is tidier and allow for flexibility if i want to add options etc

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
    // finished; main will write .wav and finish.
}





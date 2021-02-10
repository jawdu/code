// sound control.

#include "arrange.h"
#include "create.h"
#include "scntrl.h"
#include "utils.h"

#include <cmath>
#include <vector>

void smain(int N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // main point of entry for making sound. by the end, created and populated lChannel, rChannel

    /* part 1: make arrays to control events.
        1: time (integer, so index for lChan, rChan start point of event)
        2: pan (?) maybe integer ok to save memory (in range e.g. -100-100)
        3+: some to characterise the event now. maybe one will be used to forward ref. chains

        arrange.cpp to hold functions that arrange, characterise events, etc.
        create.cpp to hold functions to derive sound events, i guess?
        eventually may be arbitrary length - i.e. when the sound ends is determined stochasticly on the fly(ish)

    */

    int nF = 60; // NOTE makeF fixed for use of 60. but this will depreciate anyway.
    std::vector<double> a = makeA(nF);       // will hopefully depreciate
    std::vector<double> f = makeF(nF);       // will hopefully depreciate
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





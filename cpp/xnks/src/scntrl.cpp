// sound control.

#include "arrange.h"
#include "create.h"
#include "scntrl.h"
#include "utils.h"
#include "wavelets.h"

#include <cmath>
#include <vector>

void smain(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{
    // main point of entry for making sound. by the end, created and populated lChannel, rChannel
    // eventually may be arbitrary length - i.e. when the sound ends is determined stochasticly on the fly(ish)
    // want to make sure arranging etc is general as possible. 

    int opt = 1;            // so primitive pre-compilation menu for different methods
    
    if (opt == 1)           // morlet lower-case
    {
        std::vector<int> mev = mevents(N);                   // N set in here.
        int nmev = static_cast<int>(mev.size());
        std::vector<double> mos = momega(nmev);     // obtain omegas
        mtest(N, lChannel, rChannel);
    } 

    

    // placeholder(N, lChannel, rChannel);
        
    addnoise(N, lChannel, rChannel);
    normaliser(N, lChannel, rChannel);
    // finished; main will write .wav and finish.
}





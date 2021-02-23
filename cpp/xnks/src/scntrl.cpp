// sound control.

#include "arrange.h"
#include "create.h"
#include "scntrl.h"
#include "utils.h"
#include "wavelets.h"

#include <cmath>
#include <vector>

void smain(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // main point of entry for making sound. by the end, created and populated lChannel, rChannel

    int opt = 1;                // so primitive pre-compilation menu for different methods
    double F = 1.0;         // default for value to pass to normaliser (this may deprecate)
    
    if (opt == 1)           // morlet lower-case
    {
        std::vector<int> mev = mevents(N);                   // N set in here.
        int nmev = static_cast<int>(mev.size());
        std::vector<double> mos = momegas(nmev);     
        lChannel.assign(N, 0.0); rChannel.assign(N, 0.0);    
        lcmorlet(N, mev, mos, lChannel, rChannel);
        normaliser(N, F, lChannel, rChannel);                      // maybe different for lowercase, see how it goes
    } 
    // mtest(N, lChannel, rChannel);            // deprecated i hope
    // placeholder(N, lChannel, rChannel);  // deprecated i hope
    // addnoise(N, lChannel, rChannel);        // empty so far

    // finished; main will write .wav and finish.
}





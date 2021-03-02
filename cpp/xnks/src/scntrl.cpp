// sound control.

#include "arrange.h"
#include "create.h"         // this is getting perilously empty.
#include "scntrl.h"
#include "utils.h"
#include "wavelets.h"

//#include <iostream>
//using namespace std;

void smain(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // main point of entry for making sound. by the end, created and populated lChannel, rChannel

    int opt = 1;                // so primitive pre-compilation menu for different methods
    double F = 1.0;         // default for value to pass to normaliser (this may deprecate).
    
    if (opt == 1)           // morlet 1. try naive/faux-serialist to give omega structure.
    {
        std::vector<int> mev = mevents(N, 5.0, 60);              // N set in here. lambda; nevents
        std::vector<double> mos = momegas(9);                    // here for now   
        lChannel.assign(N, 0.0); rChannel.assign(N, 0.0);    
        lcmorlet(N, mev, mos, lChannel, rChannel);
        normaliser(N, F, lChannel, rChannel);                      // maybe different for lowercase, see how it goes
    } 
    // mtest(N, lChannel, rChannel);            // deprecated i hope, or keep to test
    // addnoise(N, lChannel, rChannel);        // empty so far

    // finished; main will write .wav and finish.
}





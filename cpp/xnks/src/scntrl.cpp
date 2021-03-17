// sound control.

#include "arrange.h"
#include "create.h"         
#include "scntrl.h"
#include "utils.h"
#include "wavelets.h"

void smain(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel)
{           // main point of entry for making sound. by the end, created and populated lChannel, rChannel

    int opt = 2;                // so primitive pre-compilation menu for different methods
    double F = 1.1;         // default for value to pass to normaliser (this may deprecate).
    
    if (opt == 1)           // morlet 1. try naive/faux-serialist to give omega structure.
    {
        std::vector<int> mev = morletEvents(N, 15.0, 60);              // N set in here. lambda; nevents
        std::vector<double> mos = morletOmegas(9);                    // here for now. add check V nmev
        lChannel.assign(N, 0.0); rChannel.assign(N, 0.0);    
        morletOne(N, mev, mos, lChannel, rChannel);
        normaliser(N, F, lChannel, rChannel);                      // maybe different for lowercase, see how it goes
    } 

    if (opt == 2)           // morlet drone
    {
        std::vector<int> mdev = mdroneEvents(N, 2.0, 50);
        std::vector<double> mdos = mdroneOmegas(2);
        lChannel.assign(N, 0.0); rChannel.assign(N, 0.0);    
        morletOne(N, mdev, mdos, lChannel, rChannel);        
        //  morletDrone, can use morletOne but that uses morlet and gabor. guess that's ok.
        normaliser(N, F, lChannel, rChannel); 
    }

    if (opt == 3)           // try out shannon
    {
        std::vector<int> sev = shannonEvents(N, 100.0, 150, 200);  // N, lambda, extra poisson factor, nevents
        lChannel.assign(N, 0.0); rChannel.assign(N, 0.0);      
        shannonOne(N, sev, lChannel, rChannel);
        normaliser(N, F, lChannel, rChannel); 
    }

    // addnoise(N, lChannel, rChannel);        // empty so far

    // finished; main will write .wav and finish.
}





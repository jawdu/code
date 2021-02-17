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

    std::vector<int> mev = mevents(N);        // N set in here. m = morlet
    // int nmev = static_cast<int>(me.size());  or just do this locally each time.
    // std::vector<double> momega = momega(nmev, mevents);

    // placeholder(N, lChannel, rChannel);
    mtest(N, lChannel, rChannel);

    addnoise(N, lChannel, rChannel);
    normaliser(N, lChannel, rChannel);
    // finished; main will write .wav and finish.
}





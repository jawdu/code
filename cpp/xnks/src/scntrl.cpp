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
    // eventually may be arbitrary length - i.e. when the sound ends is determined stochasticly on the fly(ish)
 
    // placeholder(N, lChannel, rChannel);
    mtest(N, lChannel, rChannel);

    normaliser(N, lChannel, rChannel);
    // finished; main will write .wav and finish.
}







--- main.cpp
    top-level function. contains io stuff to write to .wav, no plans to add anything else.
    goes into scntrl.cpp to do the sound stuff.

-- scntrl.cpp
    sound control.  intention is to successively call functions to create sound.

-- arrange.cpp
    first step, contains routines to create structure/parameters of sound events.

-- create.cpp
    provisional: second step, contains routine to obtain sound events/waveforms

-- utils.cpp
    contains functions that are either used by different functions or are just boring and
    needn't clutter up the interesting bits




#!/usr/bin/env ruby

=begin
    make a little glitch music
    requires https://github.com/jstrait/wavefile
        --> https://github.com/jstrait/wavefile/blob/master/examples/generate_square_wave.rb

    step 1: generate some noise, test memory robustness, seems ok for ~10s
    step n: some libraries? e.g. vinyl crackle - some sort of random sampling after getting wavs
    also: mono. think about stereo?
    naive 'random' - randomise each input/parameter or whatever. but what about something more
    --> something more open when 1 seed can react 'chaotically' to create great unpredicatblity. brood on this.
    make little modules for types of glitch. try o form bottom up. like wavelets
=end

require_relative 'gclass'
require 'wavefile'
include WaveFile

print "\n .'._ _'-_'..`` GLITCHINO '/ ,-'`- -__'' `|\n"

# get some parameters from user

# new sound object

g = Glitch.new(5) # 5 = duration in seconds for now

# make wav.

g.test_noise
g.write_wav

print "\n ..,,done.,..,,\n\n"


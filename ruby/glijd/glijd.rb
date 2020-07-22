#!/usr/bin/env ruby

=begin
    make a little glitch music
    requires https://github.com/jstrait/wavefile
        --> https://github.com/jstrait/wavefile/blob/master/examples/generate_square_wave.rb

    step 1: generate some noise, test memory robustness, seems ok for ~10s
    step n: some libraries? e.g. vinyl crackle - some sort of random sampling after getting wavs
    modified bits of beats?
    also: mono. think about stereo?
    naive 'random' - randomise each input/parameter or whatever. but what about something more, re:structure
    --> something more open when 1 seed can react 'chaotically' to create great unpredicatblity. brood on this.
    maybe idea of library of .wavs  -espec for 'synths' - optino to display available files, etc
=end

require_relative 'glitch'
require_relative 'jag'
require_relative 'synth1'
require 'wavefile'
include WaveFile
include Math

print "\n .'._ _'-_'..`` GLIJD '/ ,-'`- -__'' `|\n"

g = Glitch.new(5) # 5 = duration in seconds for now
g.test_noise
g.write_wav

print "\n ..,,done.,..,,\n\n"


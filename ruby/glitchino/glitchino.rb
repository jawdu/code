#!/usr/bin/env ruby

=begin
    make a little glitch music
    requires https://github.com/jstrait/wavefile
        --> https://github.com/jstrait/wavefile/blob/master/examples/generate_square_wave.rb

    step 1: generate some noise, test memory robustness, will it need splitting?
    step n: some libraries?
=end

require_relative 'gclass'
require 'wavefile'
include WaveFile

print "\n .'._ _'-_'..`` GLITCHINO '/ ,[- -!'' `|\n"

# get some parameters from user

# new sound object

g = Glitch.new(5) # 5 = duration in seconds

# make wav.

g.test_noise
g.write_wav

print "\n ..,,done.,..,,\n\n"


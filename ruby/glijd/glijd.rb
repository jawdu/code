#!/usr/bin/env ruby

=begin
    make a little glitch music
    requires https://github.com/jstrait/wavefile
        --> https://github.com/jstrait/wavefile/blob/master/examples/generate_square_wave.rb

    step 1: generate some noise, test memory robustness, seems ok for ~10s
    step n: some libraries? e.g. vinyl crackle - some sort of random sampling after getting wavs
    modified bits of beats?
    also: mono. think about stereo? even naive of looping through @wave, randomly vary say 20% samples
    naive 'random' - randomise each input/parameter or whatever. but what about something more, re:structure
    --> something more open when 1 seed can react 'chaotically' to create great unpredicatblity. brood on this.
    maybe idea of library of .wavs  -espec for 'synths' - optino to display available files, etc
=end

require_relative 'glitch'
require_relative 'jag'
require_relative 'synth1'
require_relative 'synth2'
require_relative 'synmod'
require 'wavefile'
include WaveFile
include Math
include Synmod

print "\n .'._ _'-_'..`` GLIJD '/ ,-'`- -__'' `|\n"

time = 0.0

until time.between?(0.1,100.0)
    print "Input duration, from 0.1-100 seconds: "
    time = gets.chomp.to_f
end

g = Glitch.new(time) 

loop do
  puts ["\n", "0: Finish, write to wav and exit: ", "1: Add hum 1:", "2: Add hum 2:", "3: Add jag noise: ", ""].join $/
  case command = gets.chomp
  
  when "0"
    puts "Going to write wav..."
    g.write_wav
    break
  when "1"
    puts "Adding synth-hum 1"
    g.add_synth(time, 1)
  when "2"
    puts "Adding synth-hum 2"
    g.add_synth(time, 2)
  when "3"
    puts "Adding jag noise"
    g.add_jag
  else
    puts "not valid response, try again"
    #not valid, ask again
  end
end

print "Done, exiting.....\n"


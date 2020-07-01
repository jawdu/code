#!/usr/bin/env ruby

#https://github.com/rubocop-hq/ruby-style-guide

class Universe
  def initialize(num_higgs)
    @unstable = Array.[](num_higgs, 0, 0, 0, 0)
    @stable = Array.new(20, 0)
  end

  def show_data
    # test
    puts "unstable: #{@unstable}"
    puts "stable: #{@stable}"
  end
end

print "Number of initial higgs in simulation: "

num_higgs = gets.to_i

u = Universe.new(num_higgs)
u.show_data

# while unstable
#   u.timestep
# end


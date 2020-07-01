#!/usr/bin/env ruby

#https://github.com/rubocop-hq/ruby-style-guide

class Universe
  def initialize(num_unstable)
    @unstable = Array.[](num_unstable, 0, 0, 0, 0)
    # set up zero array
    @stable = Array.new(20, 0)
    @time = 0
  end

  def show_data
    # to monitor stuff
    puts "unstable: #{@unstable}"
    puts "stable: #{@stable}"
    puts "time: #{@time}"
  end

  def time_step
    # do a timestep
    # go backwards, avoid higgs->W/Z->other stuff in 1 timstep. still small chance (anti)top->W->other, meh


    # housekeeping to finish
    @time += 0.1
    num_unstable = @unstable.inject(0, :+)
    return num_unstable, @time
  end
end

print "Number of initial higgs in simulation: "

num_unstable = gets.to_i

u = Universe.new(num_unstable)
u.show_data

while (num_unstable > 0)
  num_unstable, time = u.time_step
end

u.show_data

printf("Simulation ended after %.1f yoctoseconds.", time)


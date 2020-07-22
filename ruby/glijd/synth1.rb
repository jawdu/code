#!/usr/bin/env ruby

=begin
    X(t+1) = a * X(t) * (1 - X(t)) 
    --> a between 3.53 and 4.00: oscillations. x(t) is originally a population ratio. so initial vals 0.n ish?

    henon strange attractor:
        x(n+1) = 1 + y(n) - a*x(n)*x(n)
        y(n+1) = b*x(n) 
    --> e.g. one is a = 1.4, b = 0.3 so that order of magnitude?

    harmonic form: y(t) = sum [ r_k.cos (2pi.k.f_0.t + phi_k) ] r can be r(t)
    inharmonic: y(t) = sum [ r_k(t).cos (2.pi.f_k.t + phi_k) ]

    https://www.cim.mcgill.ca/~clark/nordmodularbook/nm_algorithmic.html

    *** modulation? like as a glitch, turn into sorta step function, average each c.5 points

=end

class Synth1
  def initialize
    class << self
      attr_reader :syn
    end
    @syn = Array.new
  end

  def syn_1
    t = 0.0
    te = 2.0
    n = 5
    a = Array.new(n) { rand(3.1..3.99) }
    # previously a split, a1 = rand(3.6..3.99), a2 = rand(3.1..3.50)
    r = Array.new(n) { rand(0.2..0.7) }
    f = Array.new(n) { rand(100..400) }
    while t < te
        v = 0.0
        n.times do |k|
            v = v + r[k]*cos(6.28*f[k]*t)
            r[k] = a[k]*r[k]*(1-r[k])
        end
        @syn.push(v/n)
        t = t + (1.0/44100.0)        
    end
  end

  def syn_glitch
    # glitch up the completed synth?
  end

  def syn_fade
    # linear fade in & out
  end

end




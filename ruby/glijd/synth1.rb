#!/usr/bin/env ruby

=begin
    X(t+1) = a * X(t) * (1 - X(t)) 
    --> a between 3 and 3.53: oscillations. x(t) is originally a population ratio. so initial vals 0.n ish?

    henon strange attractor:
        x(n+1) = 1 + y(n) - a*x(n)*x(n)
        y(n+1) = b*x(n) 
    --> e.g. one is a = 1.4, b = 0.3 so that order of magnitude?

    harmonic form: y(t) = sum [ r_k.cos (2pi.k.f_0.t + phi_k) ] r can be r(t)
    inharmonic: y(t) = sum [ r_k(t).cos (2.pi.f_k.t + phi_k) ]

    https://www.cim.mcgill.ca/~clark/nordmodularbook/nm_algorithmic.html
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
    te = 1.0
    a1 = rand(3.0..3.5)
    a2 = rand(3.0..3.5)
    r1 = rand(0.3..0.7)
    r2 = rand(0.2..0.7)
    f1 = rand(200..700)
    f2 = rand(100..600)
    n = 0.5 # normalisation
    while t < te
        @syn.push(n * r1 * cos(6.28 * f1 * t) + n * r2 * cos(6.28 * f2 * t))
        r1 = a1 * r1 * (1 - r1)
        r2 = a2 * r2 * (1 - r2)
        t = t + (1.0/44100.0)        
    end
  end

  def syn_glitch
    # glitch up the completed synth?
  end

end




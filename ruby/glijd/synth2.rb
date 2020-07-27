#!/usr/bin/env ruby

=begin
    synth2: try use of henon form.

    henon strange attractor:
        x(n+1) = 1 + y(n) - a*x(n)*x(n)
        y(n+1) = b*x(n) 
    --> e.g. one is a = 1.4, b = 0.3 so that order of magnitude?
        looks like initial x, y of (-1,1) means max values of 1.3 (x) <1 (y) occasionally infinity :(
        --> 'rare' so make glitchy fix: if x > 2, y > 1 reset?
=end

class Synth2
  def initialize
    class << self
      attr_reader :syn
    end
    @syn = Array.new
  end

  def syn_2(time)
    t = 0.0
    n = 2 * rand(2..5) # even number so can couple
    a = Array.new(n) { rand(-1.0..1.0) }
    f = Array.new(n) { rand(50..600) }
    while t < time
        # henon
        (n/2).times do |k|
          x0 = a[2*k]
          a[2*k] = 1.0 - 1.4*x0**2 + a[1+2*k]
          a[1+2*k] = 0.3 * x0
          if (a[2*k] > 2)
            a[2*k] = rand(-1.0..1.0)
          end
          if (a[1+2*k] > 1)
            a[1+2*k] = rand(-1.0..1.0)
          end
        end
        v = 0.0
        n.times do |k|
            v = v + a[k]*cos(6.28*f[k]*t)
        end
        @syn.push(v/n)
        t = t + (1.0/44100.0)        
    end
  end

  def syn_glitch
    # partially flatten out chunks
    p = 0
    while p < (@syn.length-100) do # -100 to make things easier at end of array (when faded anyway)
        if rand(0.0..1.0) < 0.15
            q = rand(30..100) 
            n = 0.0      
            q.times do |k|
                n += @syn[k+p]/q
            end
            q.times do |k|
                @syn[k+p] = n
            end
            p += q
        end
        p += rand(10..100)
    end
  end

  def syn_fade
    # linear fade in & out
    a = rand((0.1*@syn.length)..(0.45*@syn.length)).to_i
    b = rand((0.55*@syn.length)..(0.9*@syn.length)).to_i
    a.times do |k|
        @syn[k] = k*@syn[k]/a
    end
    (b..(@syn.length-1)).each do |k|
        @syn[k] = (@syn.length-k)*@syn[k]/(@syn.length - b)
    end

  end

end


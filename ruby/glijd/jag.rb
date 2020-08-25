#!/usr/bin/env ruby

class Jag
    # make a sort of 'mountain' shape. linear between 5 points.
    # parameters to generate: t1...3, a1...3. a2 < a1, a3. zeros t0, t4
  def initialize
    class << self
      attr_reader :jg
    end
    @jg = Array.new
    # perform stereo in glitch
  end

  def jag_noise
    t1 = rand(0.01..0.02)
    t2 = t1 + rand(0.01..0.02)
    t3 = t2 + rand(0.01..0.02)
    t4 = t3 + rand(0.01..0.02)
    t1 = (44100*t1).to_i
    t2 = (44100*t2).to_i
    t3 = (44100*t3).to_i
    t4 = (44100*t4).to_i
    a1 = rand(0.4..0.95)
    a3 = rand(0.4..0.95)
    a2 = rand(0.1..[a1,a3].min)
    g1 = a1 / t1
    g2 = (a2 - a1) / (t2 - t1)
    g3 = (a3 - a2) / (t3 - t2)
    g4 = -a3 / (t4 - t3)

    s = [-1, 1].sample

    t1.times do |i|
      @jg.push(g1 * i * s)
    end
    (t2-t1).times do |i|
      @jg.push((g2 * i + a1)  * s)
    end
    (t3-t2).times do |i|
      @jg.push(g3 * i  * s)
    end
    (t4-t3).times do |i|
      @jg.push((g4 * i + a3)  * s)
    end
  end
end

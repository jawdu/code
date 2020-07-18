#!/usr/bin/env ruby

class Glitch
  def initialize(duration)
    @waveform = Array.new
    # len(@waveform) will be @sr
    @duration = duration
    @sr = duration * 44100
  end

  def test_noise
    # try stuff out
    @sr.times do
        @waveform.push(0.0)        
        #@waveform.push(rand(-0.2..0.2))
    end

    for i in 0..4 do
        jag_noise(i+rand(0.1..0.5))
    end
  end

  def tsr(t)
    # convert seconds to sample rate index integer. duplicated in jag, atm...
    t = (44100*t).to_i
  end

  def add_synth
    # generate a small synth glitch
    # have some input parameters.... or set up 3-5 with a constrained rand range, that sound ok
    # start with harmonic form, so y(t) = Sigma [ r_k.cos (2pi.k.f_0.t + phi_k) ] r can be r(t)
    # inharmonic: y(t) = Sigma [ r_k(t).cos (2.pi.f_k.t + phi_k) ]
  end

  def write_wav
    # write @waveform to wav
    fname = "glitchino." + Time.now.strftime("%H%M%S") + ".wav"
    Writer.new(fname, Format.new(:mono, :pcm_16, 44100)) do |writer|
        buffer_format = Format.new(:mono, :float, 44100)
        buffer = Buffer.new(@waveform, buffer_format)
        writer.write(buffer)
    end
    print "Written to " + fname
  end
end



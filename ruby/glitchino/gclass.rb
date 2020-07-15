#!/usr/bin/env ruby

class Glitch
  def initialize(duration)
    @waveform = Array.new
    # @sr will be len(@waveform)
    @sr = duration * 44100
  end

  def test_noise
    # setup basic glitchiness
    @sr.times do
        @waveform.push(rand(-0.2..0.2))
    end
  end

  def jag_noise(t0)
    # make a sort of 'mountain' shape.
    # parameters to generate: t1...3, a1...3. a2 < a1, a3. zeros t0, t4
    # think: what time units? seconds or sample rate?
    t1 = t0 + rand
    t2 = t1 + rand #etc

  end

  def add_synth
    # generate a small synth glitch
    # have some input parameters....
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



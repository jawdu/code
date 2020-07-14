#!/usr/bin/env ruby

class Glitch
  def initialize(duration)
    @waveform = Array.new
  end

  def test_noise
    # setup basic glitchiness
    # loop over duration * 44100
    @waveform = ([0.5] * 100000) + ([-0.5] * 100000)

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



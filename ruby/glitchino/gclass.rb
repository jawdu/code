#!/usr/bin/env ruby

class Glitch
  def initialize(duration)
    @waveform = Array.new
  end

  def test_noise
    # setup basic glitchiness

  end

  def write_wav
    # write to wav
    fname = "glitchino." + Time.now.strftime("%H%M%S") + ".wav"

    Writer.new(fname, Format.new(:mono, :pcm_16, 44100)) do |writer|
        samples = ([0.5] * 100) + ([-0.5] * 100)
  
        buffer_format = Format.new(:mono, :float, 44100)
        220.times do
            buffer = Buffer.new(samples, buffer_format)
            writer.write(buffer)
        end
    end

  end
end



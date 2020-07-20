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

    5.times do |i|
        offset = rand(0.1..0.3)
        j = Jag.new
        j.jag_noise
        (j.jg.length).times do |k|
          @waveform[(k + 44100*(i+offset)).to_i] = j.jg[k]
        end
    end
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



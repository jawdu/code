#!/usr/bin/env ruby

class Glitch
  def initialize(time)
    @waveform = Array.new
    # len(@waveform) will be @sr
    #@duration = time
    @sr = (time * 44100).to_i
  end

  def test_noise(time)
    # try stuff out
    @sr.times do
        @waveform.push(0.0)        
    end

    j = Synth1.new
    j.syn_1(time) 
    j.syn_glitch
    j.syn_fade
    (j.syn.length).times do |k|
      @waveform[k] = j.syn[k]
    end
  end

  def write_wav
    # write @waveform to wav
    fname = "Glijd." + Time.now.strftime("%H%M%S") + ".wav"
    Writer.new(fname, Format.new(:mono, :pcm_16, 44100)) do |writer|
        buffer_format = Format.new(:mono, :float, 44100)
        buffer = Buffer.new(@waveform, buffer_format)
        writer.write(buffer)
    end
    print "Written to " + fname
  end
end

=begin
    this is e.g. adding the jag noise.
    
    5.times do |i| --> this is deprecated. use the synth1 flatten method to distribute over the duration
        offset = rand(0.1..0.3)
        j = Jag.new
        j.jag_noise
        (j.jg.length).times do |k|
          @waveform[(k + 44100*(i+offset)).to_i] = j.jg[k]
        end
    end

=end

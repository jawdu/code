#!/usr/bin/env ruby

class Glitch
  #include Synmod
  def initialize(time)
    @waveform = Array.new
    # len(@waveform) will be @sr
    @sr = (time * 44100).to_i
  end

  def test_noise(time)
    # try stuff out
    @sr.times do
        @waveform.push(0.0)        
    end
    add_synth(time, 1)
    #add_jag
    # produts of synth1, synth2? maybe add this into add_synth
  end

  def add_synth(time, n)
    if n == 2
      j = Synth2.new
      j.syn_2(time)
    else
      j = Synth1.new
      j.syn_1(time)
    end 
    Synmod.syn_glitch(j.syn)    
    Synmod.syn_fade(j.syn)    
    (j.syn.length).times do |k|
      @waveform[k] = j.syn[k]
    end
  end

  def add_jag
    p = 0
    while p < (@waveform.length - 5000) do
      if rand(0.0..1.0) < 0.03
        j = Jag.new
        j.jag_noise
        (j.jg.length).times do |k|
          @waveform[k + p] += j.jg[k]
          p += 1
        end
        p += rand(750..1500)
      end
    end
  end

  def write_wav
    # write @waveform to wav
    fname = "Glijd." + Time.now.strftime("%d%H%M%S") + ".wav"
    Writer.new(fname, Format.new(:mono, :pcm_16, 44100)) do |writer|
        buffer_format = Format.new(:mono, :float, 44100)
        buffer = Buffer.new(@waveform, buffer_format)
        writer.write(buffer)
    end
    print "Written to " + fname
  end
end


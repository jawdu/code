#!/usr/bin/env ruby

class Glitch
  #include Synmod
  def initialize(time)
    @sr = (time * 44100).to_i           # also len(waveform)
    @waveform = Array.new(@sr) { Array.new(2,0)}
    @nprocs = 0.0
  end

  def add_synth(time, n)
    @nprocs += 1
    if n == 2
      j = Synth2.new
      j.syn_2(time)
    else
      j = Synth1.new
      j.syn_1(time)
    end 
    Synmod.syn_glitch(j.syn)    
    Synmod.syn_fade(j.syn)              # soon, options here, with other type of fade? or generalise fade
    (j.syn.length).times do |k|
      @waveform[k][0] = j.syn[k]
      @waveform[k][1] = j.syn[k]        # next add val or something to make actual stereo. start making t_syn < time
    end
  end

  def add_jag
    @nprocs += 1
    p = 0
    while p < (@waveform.length - 5000) do
      if rand(0.0..1.0) < 0.2
        j = Jag.new
        j.jag_noise
        u = rand(0..1)
        v = rand(0..100)
        w = rand(0.7..1.0)  
        (j.jg.length).times do |k|
          @waveform[k+p][u] += j.jg[k]
          @waveform[k+p+v][1-u] += w * j.jg[k]
        end
        p += j.jg.length
      end
      p += rand(250..1000)
    end
  end

  def write_wav
    # write @waveform to wav. 
    if @nprocs < 1 #i.e. nothing has happend
      puts "No operations performed, nothing to do"
    else  
#---think this not needed after all
#      puts 1/@nprocs  
#     (@waveform.length).times do |i|
#        @waveform[i] *= (1/@nprocs)
 #     end
      fname = "Glijd." + Time.now.strftime("%d%H%M%S") + ".wav"
      Writer.new(fname, Format.new(:stereo, :pcm_16, 44100)) do |writer|
        buffer_format = Format.new(:stereo, :float, 44100)
        buffer = Buffer.new(@waveform, buffer_format)
        writer.write(buffer)
      end
      puts "Written to " + fname
    end
  end

end


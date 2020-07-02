#!/usr/bin/env ruby

=begin
    essentially same as the python one. uses class; splits universe state into stable/unstable array;
    also symmetry top/anti top means can combine into one method
=end

class Universe
  def initialize(num_unstable)
    @unstable = Array.[](num_unstable, 0, 0, 0, 0)
    # set up zero array
    @stable = Array.new(20, 0)
    @time = 0
    @labels = %w(Higgs\ boson W\ boson Z\ boson top\ quark top\ antiquark gluon charm\ quark anticharm\ quark strange\ quark strange\ antiquark bottom\ quark bottom\ antiquark up\ quark up\ antiquark down\ quark down\ antiquark muon antimuon tau\ lepton antitau\ lepton electron positron neutrino antineutrino photon)
  end

  def show_data
    # to monitor stuff
    puts "unstable: #{@unstable}"
    puts "stable: #{@stable}"
    puts "time: #{@time}"
  end

  def time_step
    # do a timestep
    # go backwards, avoid higgs->W/Z->other stuff in 1 timstep. still small chance (anti)top->W->other, meh

    if @unstable[4] > 0
      for i in 0..@unstable[4]
        top_antitop(1) if rand < 0.1295
      end
    end

    if @unstable[3] > 0
      for i in 0..@unstable[3]
        top_antitop(0) if rand < 0.1295
      end
    end

    if @unstable[2] > 0
      for i in 0..@unstable[2]
        z_boson if rand < 0.5
      end
    end

    if @unstable[1] > 0
      for i in 0..@unstable[1]
        w_boson if rand < 0.5
      end
    end

    if @unstable[0] > 0
      for i in 0..@unstable[0]
        higgs if rand < 0.000433
      end
    end

    # print state of universe
    # add arrays together to make loop tidier?
    u = @unstable + @stable

    update = ""
#    for i in range(24, -1, -1)
    24.downto(0) do |i|
      if u[i] == 1
        if u.inject(0, :+) == u[i]
          update = u[i].to_s + " " + @labels[i] + "."
        elsif update == ""
          update = "and " + u[i].to_s + " " + @labels[i] + "."
        else
          update = u[i].to_s + " " + @labels[i] + ", " + update
        end
      elsif u.inject(0, :+) > 1
        if u.inject(0, :+) == u[i]
          update = u[i].to_s + " " + @labels[i] + "s."
        elsif update == ""
          update = "and " + u[i].to_s + " " + @labels[i] + "s."
        else
          update = u[i].to_s + " " + @labels[i] + "s, " + update
        end
      end
    end    
    puts "The universe contains #{update}"
    
    # housekeeping to finish
    @time += 0.1
    num_unstable = @unstable.inject(0, :+)
    return num_unstable, @time
  end

  def top_antitop(top)
    # top/anti top symmetric. so use single method. add +top, 1 = 1 for anti
    p = rand
    @stable[3+top] -= 1
    @stable[1] += 1
    if p<0.3333
      @stable[3+top] += 1
    elsif p<0.6666
      @stable[7+top] += 1 
    else
      @stable[9+top] += 1
    end
  end

  def z_boson
    @unstable[2] -= 1
    p = rand
    if p<0.206
      @stable[17] += 1
      @stable[18] +=1 
    elsif p<0.24
      @stable[14] += 1
      @stable[15] +=1
    elsif p<0.274
      @stable[12] += 1
      @stable[13] += 1
    elsif p<0.308
      @stable[10] += 1
      @stable[11] += 1
    elsif p<0.46
      @unstable[4] += 1
      @stable[9] += 1
    elsif p<0.612
      @stable[3] += 1
      @stable[4] += 1
    elsif p<0.764
      @stable[7] += 1
      @stable[8] += 1
    elsif p<0.882
      @unstable[3] += 1
      @unstable[4] += 1
    else
        @stable[1] +=1
        @stable[2] += 1
    end
  end

  def w_boson
    @unstable[1] -= 1
    @stable[16] += 1
    p = rand
    if p<0.3333
      @stable[12] += 1
    elsif p<0.6666
      @stable[14] += 1
    else
      @stable[15] += 1
    end
  end

  def higgs
    @unstable[0] -= 1
    p = rand
    if p<0.648
      @stable[7] += 1
      @stable[8] += 1
    elsif p<0.789
      @unstable[1] += 2
    elsif p<0.8772
      @stable[0] += 2
    elsif p<0.9476
      @stable[13] += 1
      @stable[14] += 1
    elsif p<0.9803
      @stable[1] += 1
      @stable[2] += 1
    elsif p<0.9962
      @unstable[2] += 2
    elsif p<0.99843
      @stable[19] += 2
    elsif p<0.99954
      @unstable[2] += 1
      @stable[19] += 1
    elsif p<0.999784
      @stable[11] += 1
      @stable[12] += 1
    else
      @stable[5] += 1
      @stable[6] += 1
    end
  end

end

print "Number of initial higgs in simulation: "

num_unstable = gets.to_i

u = Universe.new(num_unstable)
#u.show_data

while (num_unstable > 0)
  num_unstable, time = u.time_step
end

#u.show_data

printf("Simulation ended after %.1f yoctoseconds.", time)


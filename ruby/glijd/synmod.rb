#!/usr/bin/env ruby

module Synmod
  # utilities for synth1,2
  def syn_glitch(syn)
    # partially flatten out chunks
    p = 0
    while p < (syn.length-100) do # -100 to make things easier at end of array (when faded anyway)
        if rand(0.0..1.0) < 0.15
            q = rand(30..100) 
            n = 0.0      
            q.times do |k|
                n += syn[k+p]/q
            end
            q.times do |k|
                syn[k+p] = n
            end
            p += q
        end
        p += rand(10..100)
    end
  end
  
  def syn_fade(syn)
    # linear fade in & out
    a = rand((0.1*syn.length)..(0.45*syn.length)).to_i
    b = rand((0.55*syn.length)..(0.9*syn.length)).to_i
    a.times do |k|
        syn[k] = k*syn[k]/a
    end
    (b..(syn.length-1)).each do |k|
        syn[k] = (syn.length-k)*syn[k]/(syn.length - b)
    end
  end
end



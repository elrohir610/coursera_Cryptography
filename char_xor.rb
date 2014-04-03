a = "20202020"
b = "415a617a"

c = (a.to_i(16) ^ b.to_i(16)).to_s(16)

puts c[0,2].to_i(16).chr
puts c[2,2].to_i(16).chr
puts c[4,2].to_i(16).chr
puts c[6,2].to_i(16).chr

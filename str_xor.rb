def strxor(a, b)     # xor two strings of different lengths
    c = ""
    if a.length > b.length
        for i in 0...b.length
                c += (a[i].to_i(16) ^ b[i].to_i(16)).to_s(16)
        end
    else
        for i in 0...a.length
                c += (a[i].to_i(16) ^ b[i].to_i(16)).to_s(16)
        end
    end
    return c
end

str1 = "50617920426f622031303024"
str2 = "50617920426f622035303024"

str3 = strxor(str1,str2)
str4 = "20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d"

puts strxor(str3,str4)

str5 = "c0"
str6 = "01"

puts strxor(str5,str6)

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

str5 = "4a"
str6 = "01"
str7 = strxor(str5,str6)
puts strxor(str7,"b4")


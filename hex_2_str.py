def hex_2_string(str_i):
        str_o = ""
        i=0
        while i < len(str_i):
                str_o = str_o + chr(int(str_i[i:i+2],16))
                i+=2
        return str_o

m = '546865204d6167696320576f726473206172652053717565616d697368204f7373696672616765'

print hex_2_string(m)

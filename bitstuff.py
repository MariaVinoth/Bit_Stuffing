import binascii

fobj = open("File2.txt",'rb')
s = fobj.read()

#method to convert the text file to binary and then bitstuff the data

def conv_binary_bitstuff(s):
    #converting the input file to binary
    hex_str = str(binascii.hexlify(s))
    bin_data = bin(int(hex_str,16)).replace('b','')
    t = []
    index = 0
    count = 0
    incr = 1

    #logic to stuff the bit 

    for i in range(len(bin_data)):
        if(bin_data[i] != '1'):
            count = 0
        else:
             count = count + 1
        if(count == 5):
            t.insert(index,i)
            index = index+1
            count = 0 
    stol = list(bin_data)

    for i in t:
        stol.insert(i+incr,'0')
        incr = incr + 1

    final_data = "".join(str(x) for x in stol)

    #writing the data that has stuffed bits into a file

    write_bitstuff = open("Output_bitstuff.txt",'wb')
    write_bitstuff.write(final_data)
    return final_data


#method to unbitstuff and convert back to the original text file

def unbitstuff_conv_text(final_data):
    index2 = 0
    t2 = []
    incr2 = 1

    #logic to unbitstuff

    for i in range(len(final_data)):
    
        if(final_data[i] != '1'):
            count2 = 0
        else:
             count2 = count2 + 1
        if(count2 == 5):
            t2.insert(index2,i)
            index2 = index2 + 1
            count2 = 0



    stol2 = list(final_data)

    for i in t2:
        stol2.pop(i+incr2)
        incr2 = incr2 - 1


    final_data2 = "".join(str(x) for x in stol2)

    write_unbitstuff = open("Output_unbitstuff.txt",'wb')
    write_unbitstuff.write(final_data2)

#convert back to text

    int_conv = int(final_data2,2)
    back_to_text = binascii.unhexlify('%x' % int_conv)

    #binary data that has been converted to text is written to a file

    write_text = open("Output_text.txt",'wb')
    write_text.write(back_to_text)


#method calls
final_data1 = conv_binary_bitstuff(s)
unbitstuff_conv_text(final_data1)



























# 123 -> 'one hundred twenty three'
words = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
}
teens={
    10: "ten",
    11:"eleven",    
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
  }

tens = {
    
    2:"twenty",
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety"
  }

# 2,434,234,532




def three_places(num):
    str_num=str(num)
    hundred = words[int(str_num[0])]
    if int(str_num[1]) == 1:
        tens= teens[int(str_num[1]+str_num[2])]
        return hundred + " " +"hundred" +tens
    tens =  words[int(str_num[2])]

    final= hundred + " " +"hundred"
    return final






def spokenInteger(num):
  str_num=str(num)
  places=len(str_num)
  spoken_num= ""
  spoken_tens=""
  
  if places == 2:
    tens = int(str_num[0])*10
    print(tens)
    spoken_tens= words[tens]
    print(spoken_tens)
    
     
  if places == 1:
    spoken_num = words[num]
    print(spoken_num)

  final = spoken_tens.join(spoken_num)
  return final
  
  
  #if places ==3:
    # str_num


  
  #for place in str_num:
  
#print(spokenInteger(4))
print(spokenInteger(94))
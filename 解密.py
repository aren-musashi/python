a=int(input('输入偏移位数'))
ptxt=input('请输入需要加密的字符串')
for b in ptxt:
      if "a"<=b<="z":
            print(chr(ord("a")+(ord(b)-ord("a")-a)%26),end="")
      elif "A"<=b<="Z":
            print(chr(ord("A")+(ord(b)-ord("A")-a)%26),end="")
      else:
            print(b,end="")


import copy
import hashlib
# pt = 'A long black shadow slid across the pavement near their feet and the five Venusi'
pt = open('readme.txt').read()
print(pt)

# to check if number of blocks is power of 2
def powerof2(n):
  if n == 0:
    return False
  while n != 1:
    if n % 2 != 0:
      return False
    n = n//2
  return True

def hash(pt):
  # divide in blocks of 16 char
  pt_list = []
  while pt != '':
    temp = pt[:16]
    pt_list.append(temp)
    pt = pt[16:]

  # print(pt_list)

  # check if the last block is of 16 chars if not pad it will 0
  if len(pt_list[-1]) < 16:
    size = 16 - len(pt_list[-1])
    for i in range(size):
      pt_list[-1] += '0'
  
  # print(pt_list)

  # check if the number of blocks is of power of 2 if not then pad it with 0
  pad = '0000000000000000'
  # print(pad)

  if powerof2(len(pt_list)) == False:
    # calculate value k such that it is power of 2 and just greater than length of pt
    i = 0
    k = 0
    while k<len(pt_list):
      k = 2**i
      i += 1
    
    # print(k)

    for i in range(k - len(pt_list)):
      pt_list.append(pad)
    
    # print(pt_list)

    n = len(pt_list)
    count = 0

    while n!=1:
      count += 1
      n = n//2


    # first convert each block in respective hash value

    for i in range(len(pt_list)):
      print(f"H {pt_list[i]}->",end = " ")
      pt_list[i] = hashlib.md5(pt_list[i].encode()).hexdigest()
      # print(pt_list[i])
    # print(pt_list)

    for i in range(count):
      pt_list1 = []
      for j in range(0,len(pt_list),2):
        # print(j)
        concatenate = pt_list[j] + pt_list[j+1]
        # print(concatenate)
        conhash = hashlib.md5(concatenate.encode()).hexdigest()

        pt_list1.append(conhash)
      print(pt_list1)
      pt_list = copy.deepcopy(pt_list1)


hash(pt)
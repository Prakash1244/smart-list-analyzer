#-------function---------
def freqency_count(arr):
  if len(arr)==0:
    return {}
  m={}
  for i in arr:
    m[i]=m.get(i,0)+1
  return m

def duplicate_detect(arr):
  if len(arr)==0:
    return None
  m=set()
  for i in arr:
    if i in m:
      return i
    m.add(i)
  return None


def index_map(arr, target):

  for i in range(len(arr)):
    if arr[i]==target:
      return i
  return -1


def grouping_key(arr):
  m={}
  for i in arr:
    key=''.join(sorted(i))
    if key not in m:
      m[key]=[]
    m[key].append(i)
  return list(m.values())


def hash_lookup(arr, target):
  if len(arr)==0:
    return False
  m=set()
  for i in arr:
    needed=target-i
    if needed in m:
      return True
    m.add(i)
  return False

def opposite_end(arr,target):
  if len(arr)==0:
    return []
  m=[]
  l=0
  r=len(arr)-1
  while l<r:
    s=arr[l]+arr[r]
    if s>target:
      r-=1
    elif s<target:
      l+=1
    else:
      m.append((arr[l], arr[r]))
      r-=1
      l+=1
  return m


def same_direction(arr):
  if len(arr)==0:
    return []
  s=0
  for f in range(len(arr)):
    if arr[f]!=0:
      arr[s], arr[f]=arr[f], arr[s]
      s+=1
  return arr


def read_write(arr):
  if len(arr)==0:
    return []
  w=0
  for r in range(len(arr)):
    if arr[r]==2:
      arr[w],arr[r]=arr[r],arr[w]
      w+=1
  return arr


def twoarray(A, B):
  if len(A)==0 or len(B)==0:
    return []
  m=[]
  i=0
  j=0
  while i<len(A) and j<len(B):
    if A[i]>B[j]:
      j+=1
    elif A[i]<B[j]:
      i+=1
    else:
      m.append(A[i])
      i+=1
      j+=1
  return m

if __name__ == "__main__":
 while True:
  print("----------Smart List Analyzer--------------")

  print("1. Perform Array/Hashing Pattern")
  print("2. Perform Two Pointers Pattern")
  print("3. Exit")
  value=input("Enter option: ")
  if value=="1": 
      print("i. Frequency Counting")
      print("ii. Duplicate Detection")
      print("iii. Index/Value Mapping")
      print("iv. Grouping Key")
      print("v. Hash Lookup")
      print("vi. Exit\n")
      value=input("Choose an option: ")
      if value=="i":
        arr=list(map(int, input("Enter number separated by space: ").split()))
        frequency=freqency_count(arr)
        print(f"Frequency:")

        for key, val in frequency.items():
          print(f"{key} --> {val}")

      elif value=="ii":
        arr=list(map(int, input("Enter number separated by space: ").split()))

        duplicate=duplicate_detect(arr)

        if duplicate is not None:
          print(f"Duplicate: {duplicate}")
        else:
          print("No duplicate found")

      elif value=="iii":
        arr=list(map(int, input("Enter numbers separated by space: ").split()))
        target=int(input("Enter target value: "))

        index=index_map(arr, target)

        print(f"Index: {index}")
        
      elif value=="iv":
        arr=list(input("Enter numbers separated by space: ").split(','))

        group=grouping_key(arr)

        print(f"group: {group}")

      elif value=="v":
        arr=list(map(int, input("Enter numbers separated by space: ").split()))
        target=int(input("Enter target value: "))

        lookup = hash_lookup(arr, target)

        print(f'lookup: {lookup}')

      elif value=="vi":

        print("Returning to main menu...")

      else:
        print('Invalid input, Returning to main menu.')

  elif value=="2":

      print("i. Opposite ends pointer")
      print("ii. Same Direction pointer")
      print("iii. Read/Write pointer")
      print("iv. Two array pointer")
      print("v. Exit")

      value=input("Choose an Option: ")
      if value=="i":

        arr=list(map(int, input("Enter numbers separated by space: ").split()))
        target=int(input("Enter target number you to achive: "))

        opposite=opposite_end(arr, target)

        if opposite is not None:
          print(f"Opposite ends: {opposite}")
        else:
          print("No value found!!")

      elif value=="ii":

        arr=list(map(int, input("Enter numbers separated by space: ").split()))

        Fast=same_direction(arr)

        print(f"Rearrange: {Fast}")

      elif value=="iii":

        arr=list(map(int, input("Enter numbers separated by space: ").split()))

        read=read_write(arr)

        print(f"read: {read}")

      elif value=="iv":

        A=list(map(int, input("Enter numbers for A separated by space: ").split()))
        B=list(map(int, input("Enter numbers for B separated by space: ").split()))

        TwoArray=twoarray(A,B)

        if TwoArray is not None:
          print(f"Common Elements: {TwoArray}")
        else:
          print("No Common Found")

      elif value=="v":

        print("Returning to main menu...")

      else:
        print("Invalid input, returning to main menu.")

  elif value=="3":
    print('Thank You!! Please visit again!!')
    break

  else:
    print("Invalid option. Please try again.")


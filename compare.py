import sys
sys.stdout.reconfigure(encoding='utf-8')
from collections import Counter


def list1 ():
    with open('list.txt', 'r', encoding='utf-8') as file:
          lines = [line.strip() for line in file]
    count = Counter(lines)
    duplicates = [item for item, count in count.items() if count == 2]
    
    return duplicates

def list2 ():    
    with open('list2.txt', 'r', encoding='utf-8') as file:
          lines = [line.strip() for line in file]
    count = Counter(lines)
    duplicates = [item for item, count in count.items() if count == 2]
    
    return duplicates      

def main():
 myInfo = []
 d1 = list1()
 d2 = list2()
 
 for i in d2:
        if i not in d1:
            myInfo.append(i)
            

 
 try:
        with open("mutual.txt", 'w', encoding='utf-8') as file:
            for i in myInfo:
                file.write(i + '\n')  
 except Exception as e:
        print(f"Error: {e}")
    
    
 
 

        
if __name__ == "__main__":
    main()       
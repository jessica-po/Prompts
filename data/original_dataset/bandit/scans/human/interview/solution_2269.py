t=int(input())
no_of_chars = 256
  
# Function to find smallest window  
# containing all characters of 'pat'  
def findSubString(string, pat):  
    len1 = len(string)  
    len2 = len(pat)  
    if len1 < len2:  
      
        return 0
    hash_pat = [0] * no_of_chars 
    hash_str = [0] * no_of_chars  
    for i in range(0, len2):  
        hash_pat[ord(pat[i])] += 1
  
    start, start_index, min_len = 0, -1, float('inf')  
    count = 0 # count of characters  
    for j in range(0, len1):  
        hash_str[ord(string[j])] += 1
        if (hash_pat[ord(string[j])] != 0 and
            hash_str[ord(string[j])] <= 
            hash_pat[ord(string[j])]):  
            count += 1
        if count == len2:  
            while (hash_str[ord(string[start])] >  
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):  
              
                if (hash_str[ord(string[start])] >  
                    hash_pat[ord(string[start])]):  
                    hash_str[ord(string[start])] -= 1
                start += 1
            len_window = j - start + 1
            if min_len > len_window:  
              
                min_len = len_window  
                start_index = start  
    if start_index == -1: 
        return 0
      
    # Return substring starting from  
    # start_index and length min_len  
    return min_len
while t:
    t-=1
    a=input()
    x="123"
    print(findSubString(a,x))
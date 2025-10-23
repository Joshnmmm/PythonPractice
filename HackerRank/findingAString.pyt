def count_substring(string, sub_string):
    count =0
    length = len(sub_string)
    for i in range(0, len(string) - (length-1)):
        group = string[i:i+(length)]      
        if sub_string in group:
            count +=1
    return count
        
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
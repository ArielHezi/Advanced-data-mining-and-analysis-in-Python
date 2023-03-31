

def my_func(x1,x2,x3):
    
    try:
        if type(x1) != float or type(x2) != float or type(x3) != float:
             print("Error: parameters should be float")
             return None
             
        else:
            numerator = (x1+x2+x3)*(x2+x3)*x3
            denominator = x1+x2+x3
            value = numerator/denominator
            return  float(value)
    
    except:
        if denominator == 0:
            print("Not a number – denominator equals zero")
        return None

#print(my_func(1.5, 2.5, 'a'))




def revword(word: str) -> str:
    new_word = word[::-1].lower()
    
    return new_word


def countword() -> int:
    file = open("text.txt")
    lst = file.read().split()
    count = 1
    word = lst[0]
    for w in lst[1:]:
        reverse = revword(w)
        if reverse == word:
            count += 1
    
    return count
    

#print(countword())     















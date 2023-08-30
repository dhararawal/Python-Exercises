#Exercise 3a: Check string is palindrome

#Function 1: returns the reverse of the users inputted word
def check_palindrome():
    userword = input("Please enter a word:") #asks user to enter a word
    userword = userword.casefold() #makes user input able for caseless comparison
    if userword == userword[::-1]: #reverses users word
        print("True, the word", userword, "is a palindrome!") #returns true if palindrome
    else:
        print("False, the word", userword, "is not a palindrome!") #returns false if not palindrome
#check_palindrome()  #calls palindrome function



#Exercise 3b: Convert string to lower-case and returns 3rd most frequent letter

def countOccs(d):
    result = {}
    for c in d:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def top_three_frequent(d):
    count_occ = countOccs(d)
    tuples = []
    for k, v in count_occ.items():
        tuples.append((v, k))
    tuples.sort()
    if len(tuples) < 3:
        limit = len(tuples)
    else:
        limit = 3
    for i in range(-1, -(limit + 1), -1):
        v, k = tuples[i]
        print(k, ':', v)

#userdata = top_three_frequent(input("Enter a sentence: ").lower())
#print()






#Exercise 3c: Function that takes string and counts upper-case letters, lower-case letters and digits in a string

#Function 3: Counts upper-case, lower-case and digits in a string and returns as tuple
def string_analysis():
    user_string_analysis = input("Enter a sentence:") #asks user for input
    #defines variables
    upper_case = 0
    lower_case = 0
    digit_count = 0
    other = 0
    for i in user_string_analysis:
        if(i.islower()):
            lower_case+=1 #counts lower-case characters
        elif i.isupper():
            upper_case+=1 #counts upper-case characters
        elif i.isdigit():
            digit_count+=1 #counts digits
        else:
            other +=1 #counts white spaces and other characters e.g. ? and !
    mytuple = (upper_case, lower_case, digit_count) #creates a tuple consisting of upper-case, lower-case and digit count
    print(mytuple) #returns upper-case count, lower-case count and digit count as a tuple
#string_analysis() #calls string analysis function
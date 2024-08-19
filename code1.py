def countVowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    print(f"Vowel count is {count}")
    return count

# Test cases
countVowels("hello world")            
countVowels("The quick brown fox")    
countVowels("AEIOU")                  
countVowels("Python Programming")     

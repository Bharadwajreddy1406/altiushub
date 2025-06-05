

s = input("Enter a string: ")
def is_palindrome(s):
    fchars = ''.join(c.lower() for c in s if c.isalnum())
    print(fchars)
    
    for i in range(len(fchars) //2):
        if fchars[i]!= fchars[len(fchars) - i -1]:
            return False
    return True

result = is_palindrome(s)

if result:
    print("true")
else:
    print("false")



    # // 🧑‍💻 Intern (0–1 Years Experience) 
    # // A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    # // Given a string s, return true if it is a palindrome, or false otherwise.

    # // Example 1:
    # // Input: s = "A man, a plan, a canal: Panama"
    # // Output: true
    # // Explanation: "amanaplanacanalpanama" is a palindrome.

    # // Example 2:
    # // Input: s = "race a car"
    # // Output: false
    # // Explanation: "raceacar" is not a palindrome.

    # // Example 3:
    # // Input: s = " "
    # // Output: true
    # // Explanation: s is an empty string "" after removing non-alphanumeric characters.
    # // Since an empty string reads the same forward and backward, it is a palindrome.
    
    # // Constraints:
    # // •	1 <= s.length <= 2 * 105
    # // •	s consists only of printable ASCII characters.
    # // Focus Areas:	
    # // •	String manipulation
    # // •	Two-pointer technique
    # // •	Time complexity analysis



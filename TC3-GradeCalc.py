# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Variables
    gradevalue = {
        "A+" : 4.3 ,
        "A" : 4.0,
        "A-" : 3.7,
        "B+" : 3.3,
        "B" : 3.0,
        "B-" : 2.7,
        "C+" : 2.3,
        "C" : 2.0,
        "C-" : 1.7,
        "D+" : 1.3,
        "D" : 1.0,
        "D-" : 0.7,
        "F" : 0.0 }
    grade= input("Please enter your grade: ")
    if grade in gradevalue: (4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0)
        
    else:
        return "Invalid"
    
    
    print("This is your grade: %{0}".format (gradevalue))

    #my apologies a little behind still, I wasn't able to get the single print out, instead it prints everything


  

    










    # YOUR CODE ENDS HERE

main()

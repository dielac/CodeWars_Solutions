# Solution: number 1, Odd or Even.

def even_or_odd(number):      

  
    print("checking if the number is odd or even")

    result = "Odd"    # i put that its off first, dont know if that will matter or not 

    
    if number % 2 == 0: 
        
        result = "Even"     
        
        print("The number is even!") 
    

    # didnt handle the odd case?? it still passed so i dont think it mattered
    print("Returning the result...") 

    return result   



# Solution: number 2, Convert a number to a string

def number_to_string(num):         # this code turns a number into a string ? 

    
    print("Converting the number to a string")     
    

    result = ""      # next two codes store the string version i believe 

    # dont know if this code below is needed 
    result = str(num)      

    print(" it is converted now")  # checks if itconverted

    print("results loading back!!")    # confirms that it is done

    
    return result     


# Solution: number 3, Remove String Spaces

def no_space(string):         # i think this code removes spaces
    
    print("Removing spaces from the string...")     # checks if the function started


    result = ""    

    
    for char in string:      # loops through the character 
        
        if char != " ":      # makes sure it doesnt have a space 
            
            result = result + char    # attempting to add it to the result
            
        else:
            print("found the space!")     # noticing the spaces 


    print("done removing spaces!")    # checks if the loop finishes 
    
    print("returning the result...")    #returning the results 

    # printed the result before returning, but it still worked when i tested it
    print("The result is: " + result)   

    return result 

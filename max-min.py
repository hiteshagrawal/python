# reads numbers until the program is done and
# prints the maximum and the minimum

#while loop to append numbers to the list

working_list = list()

while True:
    # handle the edge cases
    inp = raw_input('Enter a number or "done"\n')
    if inp.lower() == "done":
        # check for empty list    
        if len(working_list) < 1:
            working_list.append("None")
        print "We are at the first break"
        break
    # check for empty line
    if len(inp) < 1:
        if len(working_list) < 1:
            working_list.append("None")
        print "We are at the second break"
        break
    # do the work
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    working_list.append(num)   

# prints results
print "The minimum is" , min(working_list)
print "The maximum is" , max(working_list) 
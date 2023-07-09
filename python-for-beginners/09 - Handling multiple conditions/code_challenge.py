# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
name = input("enter your name :").lower()
if name.startswith('a') or name.startswith('b'):
    print("You can go to room AB")
elif name.startswith('c'):
    print("You can go to room CD")
else:
    lname = input("enter your last name: ").lower()
    if lname.startswith('z'):
        print("You can go to room Z")
    else:
        print("You can go to other rooms")
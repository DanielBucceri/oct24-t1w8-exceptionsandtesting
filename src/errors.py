def convert_to_integer(value):
    try:
        result = int(value)
        return result
    except ValueError:   # can be restricted to only handle certain types of errors
       raise ValueError("Conversion failed. please enter valid INT")
    except Exception as e:   # can be restricted to only handle certain types of errors
        print("Error occured {e}")
    finally:
        print("Closing any open connectons..beepboop")
        #Connection.close(lol)




#user input
# spam = input("Enter a numb: ")
# convert_to_integer(spam)

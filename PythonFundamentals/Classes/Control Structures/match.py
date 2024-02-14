#Match statement
#For a large amount of conditions

http_status= 200

match http_status:
    case 200: 
        print("Success")

    case 400: 
        print ("Not Found")

    case 500|501:
        print("Server Error")
    case _:   #This is like the else condition 
        print("Unknow")
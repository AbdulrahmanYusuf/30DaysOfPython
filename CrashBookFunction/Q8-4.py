def make_shirt(size = "large", message = "i love Python"):
   

    if size == "large" or size == "medium"  :
        print(f"with {size} size, {message}")
    
    else:
        print(f"with {size} size, {message}")



make_shirt(size=40, message='i am enjoying Python')
make_shirt(size="large")
make_shirt(size="medium")

try:
    with open('ATA.log') as file:
        read_data = file.read()
        print(read_data)
except:
    print("error")
#collects and returns car and owner details
import datetime
def form():
    vrn = input('Registration Number: ')
    fname = input('Owner name: ')
    sname = input('Owner Surname: ')
    make = input('Make: ')
    model = input('Model: ')
    fuel = input('Fuel Type: ')
    #check if millage is passed as integer
    while True:
        try:
            milage = int(input('Milage: '))
            break
        except ValueError:
            print('Wrong value')
            continue

    #collect information about work done 
    work_done = []
    while True:
        work = input('Work done:')
        if work == 'q':
            break
        work_done.append(work)
    all_work = ', '.join(work_done)
    
    
    #prepare message which will be written to file
    full_name = fname.capitalize() +' '+ sname.capitalize()
    message = (f"\n\nReg number: {vrn.upper()}.\nOwner: {full_name}\n"
                f"Make and Mode: {make.capitalize()} {model.capitalize()}\n"
                f"Fuel Type: {fuel.capitalize()}\nCurrent millage: {milage}\n"
                f"Recent work done: {all_work}")
    
    #create file name
    date = str(datetime.date.today())
    filename = vrn.upper() + date +'.txt'
    
    #write information to file
    with open (f"C:\\Users\\skole\\Desktop\\temp\\{filename}", "w") as file:
        file.write(message)

form()
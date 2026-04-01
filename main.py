from list_CRUD import *

while True:
    print_info()
    opt = input()
    match opt:
        case '1':
            print_accomodations()
        case '2':
            create_accomodation()
        case '3':
            edit_accomodation()
        case '4':
            remove_accomodation()
        case '5':
            print('iseinu is programos')
            break
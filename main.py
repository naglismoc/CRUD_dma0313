from list_demo_data import load_accomodations
from list_CRUD import *

accomodations = load_accomodations()
id_counter = 3
while True:
    print_info()
    opt = input()
    match opt:
        case '1':
            print_accomodations(accomodations)
        case '2':
            id_counter = create_accomodation(accomodations,id_counter)
        case '3':
            edit_accomodation(accomodations)
        case '4':
            remove_accomodation(accomodations)
        case '5':
            print('iseinu is programos')
            break
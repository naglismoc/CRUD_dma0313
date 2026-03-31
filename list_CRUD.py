def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_accomodations(accomodations):
    for acc in accomodations:
        print(
            f'{acc['id']}. Atostogos {acc['country']} {acc['city']}. Kaina gyvenant {acc['accomodation']} parai {acc['price']} eurų.')

def create_accomodation(accomodations, id_counter):
    print('atostogu itraukimas:')
    print("iveskite sali")
    country = input()
    print("iveskite miesta")
    city = input()
    print('iveskite apgyveninimo tipa')
    accom = input()
    print('iveskite kaina')
    price = float(input())
    id_counter += 1
    acc = {
        'id': id_counter,
        'country': country,
        'city': city,
        'accomodation': accom,
        'price': price
    }
    accomodations.append(acc)
    return id_counter

def edit_accomodation(accomodations):
    print('atostogu redagavimas')
    print("iveskite id atostogu kurias norite redaguoti")
    edit_id = input()
    for acc in accomodations:
        if edit_id == str(acc['id']):
            print(f'{acc['id']}. Redaguojama: Atostogos {acc['country']} {acc['city']}. Kaina gy'
                  f'venant {acc['accomodation']} parai {acc['price']} eurų.')
            print("iveskite sali")
            acc['country'] = input()
            print("iveskite miesta")
            acc['city'] = input()
            print('iveskite apgyveninimo tipa')
            acc['accom'] = input()
            print('iveskite kaina')
            acc['price'] = float(input())
            break

def remove_accomodation(accomodations):
    print('atostogu salinimas')
    print("iveskite id atostogu kurias norite pasalinti")
    del_id = input()
    for acc in accomodations:
        if del_id == str(acc['id']):
            print(f'{acc['id']}. Šalinama: Atostogos {acc['country']} {acc['city']}. Kaina gy'
                  f'venant {acc['accomodation']} parai {acc['price']} eurų.')
            accomodations.remove(acc)
            break
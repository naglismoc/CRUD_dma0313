import csv

headers = ['id','country','city','price','accomodation']
def load_accomodations():
    with open('./accomodations.csv',mode='r',encoding='utf-8')as file:
        return list(csv.DictReader(file))

def save_accomodations(accomodations):
    with open('./accomodations.csv',mode='w', newline='', encoding='utf-8')as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(accomodations)

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_accomodations():
    accomodations = load_accomodations() # reikalinga TIK tada jei sistema ONLINE, ir dirbam keliese
    for acc in accomodations:
        print(
            f'{acc['id']}. Atostogos {acc['country']} {acc['city']}. Kaina gyvenant {acc['accomodation']} parai {acc['price']} eurų.')

def create_accomodation():
    accomodations = load_accomodations() # reikalinga TIK tada jei sistema ONLINE, ir dirbam keliese
    print('atostogu itraukimas:')
    print("iveskite sali")
    country = input()
    print("iveskite miesta")
    city = input()
    print('iveskite apgyveninimo tipa')
    accom = input()
    print('iveskite kaina')
    price = float(input())
    id_counter = int(accomodations[-1]['id']) + 1 if len(accomodations) > 0 else 1
    acc = {
        'id': id_counter,
        'country': country,
        'city': city,
        'accomodation': accom,
        'price': price
    }
    accomodations.append(acc)
    save_accomodations(accomodations)

def edit_accomodation():
    accomodations = load_accomodations() # reikalinga TIK tada jei sistema ONLINE, ir dirbam keliese
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
            acc['accomodation'] = input()
            print('iveskite kaina')
            acc['price'] = float(input())
            break
    save_accomodations(accomodations)

def remove_accomodation():
    accomodations = load_accomodations() # reikalinga TIK tada jei sistema ONLINE, ir dirbam keliese
    print('atostogu salinimas')
    print("iveskite id atostogu kurias norite pasalinti")
    del_id = input()
    for acc in accomodations:
        if del_id == str(acc['id']):
            print(f'{acc['id']}. Šalinama: Atostogos {acc['country']} {acc['city']}. Kaina gy'
                  f'venant {acc['accomodation']} parai {acc['price']} eurų.')
            accomodations.remove(acc)
            break
    save_accomodations(accomodations)
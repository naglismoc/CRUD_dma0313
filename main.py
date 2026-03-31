accomodations = [
            {
                'id': 1,
                "country":"Lithuania",
                "city":"Palanga",
                "price":20.0,
                "accomodation":"hotel"
            },
            {
                'id': 2,
                "country":"Turkija",
                "city":"Alanya",
                "price":60.0,
                "accomodation":"hostel"
            },
            {
                'id': 3,
                "country":"Cyprus",
                "city":"Larnaka",
                "price":70.0,
                "accomodation":"apartaments"
            }
        ]

id_counter = 3
while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    opt = input()
    match opt:
        case '1':
            for acc in accomodations:
                print(f'{acc['id']}. Atostogos {acc['country']} {acc['city']}. Kaina gyvenant {acc['accomodation']} parai {acc['price']} eurų.')
        case '2':
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
                'city':city,
                'accomodation':accom,
                'price':price
            }
            accomodations.append(acc)
        case '3':
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
        case '4':
            print('atostogu salinimas')
            print("iveskite id atostogu kurias norite pasalinti")
            del_id = input()
            for acc in accomodations:
                if del_id == str(acc['id']):
                    print(f'{acc['id']}. Šalinama: Atostogos {acc['country']} {acc['city']}. Kaina gy'
                          f'venant {acc['accomodation']} parai {acc['price']} eurų.')
                    accomodations.remove(acc)
                    break
        case '5':
            print('iseinu is programos')
            break
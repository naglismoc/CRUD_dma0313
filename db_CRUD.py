# pip install mysql-connector-python
# pip install pymysql (alternatyva jei anas  neveikia)
# jei atidarius workbencha nerodo duomenu baziu, o tik no connection established raudonai, darom taip:
# start ->command prompt. paleidziam kaip ADMINISTRATORIUS. atidaro terminala. jame rasome: net start (jusu servo
# pavadinimas, mysqld80 ar kazkas panasaus)
# pvz: net start new_one
import mysql.connector

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3312,
    'user':'root',
    'password':"root",
    'database':'holidays'
}
headers = ['id','country','city','price','accomodation']

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_accomodations():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from holidays')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    accomodations_list = []
    for row in rows:
        single_accomodation = {}
        for col_num in range(len(headers)):
            single_accomodation[headers[col_num]] = str(row[col_num]).replace('\r','')
        accomodations_list.append(single_accomodation)
    return accomodations_list

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
    print('atostogu itraukimas:')
    print("iveskite sali")
    country = input()
    print("iveskite miesta")
    city = input()
    print('iveskite apgyveninimo tipa')
    accom = input()
    print('iveskite kaina')
    price = float(input())
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO `holidays` (`country`,`city`,`price`,`accomodation`)VALUES(%s,%s,%s,%s);',(country,
                                                                                                  city,price,accom))
    conn.commit()
    cur.close()
    conn.close()

def edit_accomodation():
    print('atostogu redagavimas')
    print("iveskite id atostogu kurias norite redaguoti")
    edit_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from holidays where id = %s',(edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        print(f'{row[0]}. Atostogos {row[1]} {row[2]}. Kaina gyvenant {row[3]} '
              f'parai {row[4]} eurų.')
        print("iveskite sali")
        country = input()
        print("iveskite miesta")
        city = input()
        print('iveskite apgyveninimo tipa')
        accom = input()
        print('iveskite kaina')
        price = float(input())
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('UPDATE `holidays` SET `country` = %s,`city` = %s,`price` = %s,`accomodation` = %s WHERE `id` = '
                    '%s;', (country,city,price,accom,edit_id))
        conn.commit()
        cur.close()
        conn.close()

    else:
        print('tokio iraso nera')

def remove_accomodation():
    print('atostogu salinimas')
    print("iveskite id atostogu kurias norite pasalinti")
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from holidays where id = %s',(del_id,))
    row = cur.fetchone()

    if row:
        print(f'{row[0]}. Šalinama atostogos {row[1]} {row[2]}. Kaina gyvenant {row[3]} '
              f'parai {row[4]} eurų.')
        cur.execute('delete from holidays where id = %s',(del_id,))
        conn.commit()
    else:
        print('tokio iraso nera')
    cur.close()
    conn.close()
def customer_details(row):
    print(f'Customer Code: {row[0]:>14}\n'
        f'Reg Number: {row[2]:>18}\n'
        f'Name: {row[3]:>15}\n'
        f'Surname: {row[4]:>14}\n'
        f'Company: {row[5]:>16}\n'
        f'Address: {row[6]:>16}\n'
                    f'{row[7]:>16}\n'
                    f'{row[8]:>16\}n'
                    f'{row[9]:>16\n}'
        f'Phone number: {row[10]:>24}'
        f'Email Address: {row[11]:>24}')
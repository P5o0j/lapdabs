def car_details(row):
    print(f'Reg number: {row[0]:>14}\n'
        f'Make: {row[1]:>18}\n'
        f'Model: {row[2]:>15}\n'
        f'Fuel Type: {row[3]:>14}\n'
        f'Millage: {row[4]:>16}\n'
        f'Colour: {row[5]:>16}\n'
        f'MOT: {row[6]:>24}')

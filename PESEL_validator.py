pesel = str(input("Enter PESEL: "))

months = {'January': ['81', '01', '21', '41', '61'],
          'February': ['82', '02', '22', '42', '62'],
          'March': ['83', '03', '23', '43', '63'],
          'April': ['84', '04', '24', '44', '64'],
          'May': ['85', '05', '25', '45', '65'],
          'June': ['86', '06', '26', '46', '66'],
          'July': ['87', '07', '27', '47', '67'],
          'August': ['88', '08', '28', '48', '68'],
          'September': ['89', '09', '29', '49', '69'],
          'October': ['90', '10', '30', '50', '70'],
          'November': ['91', '11', '31', '51', '71'],
          'December': ['92', '12', '32', '52', '72']
          }

centuries = {'18': ['8, 9'],
             '19': ['0', '1'],
             '20': ['2', '3'],
             '21': ['4', '5'],
             '22': ['6', '7'],
}


def check_pesel() -> bool:

    if pesel.isdigit() == False:
        raise ValueError("Given input contains other than digit values!")
    
    if len(pesel) != 11:
        raise("Given input does not contain 11-digit number!")
    
    sum_ = (int(pesel[0]) * 1) + (int(pesel[1]) * 3) + (int(pesel[2]) * 7) + (int(pesel[3]) * 9) + (int(pesel[4]) * 1) + (int(pesel[5]) * 3) + (int(pesel[6]) * 7) + (int(pesel[7]) * 9) + (int(pesel[8]) * 1) + (int(pesel[9]) * 3)
    
    str_sum = str(sum_)
    
    if len(str_sum) > 1:
        result = int(str_sum[-1])
    else:
        result = sum_
    
    answer = 10 - result
    if answer == int(pesel[-1]):
        return True

    return False


def get_data_from_pesel() -> str:
    if check_pesel():
        month = [i for i in months if pesel[2:4] in months[i]][0]

        #loop not necessary but more secure
        for i in range(len(months[month])):
            if pesel[2] in months[month][i][0]:
                year_prefix = [i for i in centuries if pesel[2] in centuries[i]][0]

        # year_prefix = [i for i in centuries if pesel[2] in centuries[i]][0]

        year = year_prefix + pesel[0:2]

        if int(pesel[-2]) %2 == 0:
            gender = "female"
        else:
            gender = "male"

        return f'Date of birth: {pesel[4:6]} {month} {year} \ngender: {gender}'


print(get_data_from_pesel())

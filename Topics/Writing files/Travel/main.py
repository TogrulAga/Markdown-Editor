# add Turkey to countries.txt
file = open("countries.txt", 'a', encoding='utf-8')
file.writelines('Turkey\n')
file.close()

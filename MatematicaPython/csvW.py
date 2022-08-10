import csv

with open('user.csv','w') as user:
    escritor=csv.writer(user)
    escritor.writerow(['nome','sobrenome','email','genero'])
    escritor.writerow(['Kairo','Costa','kairomilhomem@gmail.com','M'])

import geradorcpf
from faker import Faker

fake = Faker('pt_BR')
print(fake.first_name(), fake.last_name())


cpf = geradorcpf.cpf()
print(cpf)
# print(geradorcpf.validarcpf(cpf))



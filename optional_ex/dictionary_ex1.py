phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#print Elizabeth phone number
print(phonebook_dict['Elizabeth'])

#add Kareem
phonebook_dict.update({'Kareem':'936-489-1234'})

#delete Alice
del phonebook_dict['Alice']

#change Bob phone number
phonebook_dict['Bob'] = '968-345-2345'

#print all contents of phonebook
print(phonebook_dict)

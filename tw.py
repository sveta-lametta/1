import re
phone = input()
phone_ = phone.replace(' (\-', '')
print(phone)
phone_pattern = r'(?[78][\s\-\(]?)(\d{3}[\s\-\)]?)(\d{3}[-\s]?)(\d{2}[-\s]?)(\d{2})'
valid_number = re.findall(phone_pattern, phone)

if valid_number:
  print(re.sub(phone_pattern, r'+7-\2-\3-\4-\5', phone))
else:
  print('Номер не валиден')


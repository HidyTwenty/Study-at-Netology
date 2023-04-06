import re
import csv
from collections import defaultdict
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_dict = defaultdict(list)

for contact in contacts_list[1:]:
    name_parts = re.split(r'[\s,]+', contact[0] + ',' + contact[1] + ',' + contact[2])
    if len(name_parts) > 3:
        name_parts = name_parts[:3]
    while len(name_parts) < 3:
        name_parts.append('')
    
    lastname, firstname, surname = name_parts

    phone = contact[5]
    if phone:
        phone = re.sub(r'\D', '', phone)
        phone = f"+7({phone[1:4]}){phone[4:7]}-{phone[7:9]}-{phone[9:11]}"
        if len(contact[5]) > 15:
            ext = re.search(r'доб\.\s*\d+', contact[5])
            if ext:
                phone += f" доб.{ext.group().split('доб.')[-1].strip()}"

    key = (lastname, firstname)
    value = [surname, contact[3], contact[4], phone, contact[6]]
    if not contacts_dict[key]:
        contacts_dict[key] = value
    else:
        for i, v in enumerate(value):
            if v and not contacts_dict[key][i]:
                contacts_dict[key][i] = v

result_list = [contacts_list[0]]
for key, value in contacts_dict.items():
    result_list.append(list(key) + value)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)

pprint(result_list)
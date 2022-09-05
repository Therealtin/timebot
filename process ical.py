import os
import json

weeks = ['A', 'B']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
periodslist = []
fills = {}

for week in weeks:
    for day in days:
        if day == 'Wednesday':
            for x in range(3):
                x += 1
                rtnval = week + day + str(x)
                periodslist.append(rtnval)
        else:
            for x in range(6):
                x += 1
                rtnval = week + day + str(x)
                periodslist.append(rtnval)

# replacement of A monday to the end as it isn't properly ordered
removallist = []
for period in periodslist:
    if period.startswith('AMonday'):
        removallist.append(period)
for period in removallist:
    periodslist.remove(period)
    periodslist.append(period)
print(periodslist)

for file in os.listdir(r"C:DIRECTORY"):
    filename = file.split('.')[0]
    if not os.path.isfile(
            r"DIRECTORY" + filename + ".json"):
        teachercodesfile = open(r"DIRECTORY", 'r+')
        teachercodes = json.loads(teachercodesfile.read())

        with open(r"DIRECTORY" + filename + '.ics', 'r') as calendar:
            calendar = calendar.read()
            calendar = calendar.split('END:VEVENT\nBEGIN:VEVENT')[:-1]
            x = 0
            for chunk in calendar:
                periodno = chunk[chunk.index('Period: ') + 8]
                if periodno == '0':
                    continue
                classno = chunk[chunk.index('SUMMARY:') + 8:chunk.index('SUMMARY:') + 15].strip()
                year = ''
                for y in classno:
                    if not y.isnumeric():
                        break
                    year += y
                if year[0] == year:
                    classno = classno[0:4] + '.' + classno[4:] + ' '
                    classno = classno.strip()
                    classno += ' '
                else:
                    classno = chunk[chunk.index('SUMMARY:') + 8:chunk.index('SUMMARY:') + 16].strip()
                    classno = classno[0:5] + '.' + classno[5:] + ' '
                    classno = classno.strip()
                    classno += ' '
                teacher = chunk[chunk.index('Teacher: ') + 9:chunk.index(r'\nPeriod')]
                year = int(year)
                if teacher not in teachercodes.keys():
                    teachercodes[teacher] = ''
                teacher = teachercodes[teacher]
                try:
                    if periodslist[x][-1] == periodno:
                        fills[periodslist[x]] = classno + teacher
                    else:
                        print(periodslist[x][-1], periodno)
                        print('slight problem')
                        x += 1
                        if periodslist[x][-1] == periodno:
                            fills[periodslist[x-1]] = 'free period'
                            fills[periodslist[x]] = classno + teacher
                except IndexError:
                    break
                x += 1

        print(filename)
        fills['firstname'] = input('firstname: ')
        fills['lastname'] = input('lastname: ')
        fills['id'] = input('discord user id: ')
        fills['year'] = year
        print(fills)
        newfile = open(r"DIRECTORY" + filename + ".json", 'x')
        json.dump(fills, newfile, indent=4)
        newfile.close()

        teachercodesfile.close()
        os.remove(r"DIRECTORY\\teachercodes.json")
        teachercodesfile = open(r"DIRECTORY\\teachercodes.json", 'x')
        json.dump(teachercodes, teachercodesfile, indent = 4)
        teachercodesfile.close()

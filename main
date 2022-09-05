# time bot.py
import os
import datetime
import asyncio
import discord
from time import sleep
from discord.ext import commands
from dotenv import load_dotenv
import calendar
import json

# env
load_dotenv()
TOKEN = os.getenv('SNOWY')
GUILD = os.getenv('TIME')

# bot prefix, etc. etc.
botprefix = '~'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=botprefix, intents=intents)
bot.remove_command('help')

# embed and current time
currenttime = datetime.datetime.now().strftime("%I:%M %p")
timetableembed = discord.Embed(
    title = f'**__Timetable - {calendar.day_name[datetime.date.today().weekday()]}__**',
    colour = discord.Colour.from_rgb(255, 255, 255),
    description = f"**Current Time: please wait...\nDate: {datetime.datetime.now().strftime('%d/%m/%Y')}**"
)

# Times
monday = {'05:00 AM': "Before School", '09:00 AM': 'Period 1', '09:40 AM': "Break", "09:45 AM": 'Period 2', "10:25 AM": "Recess",
           "10:45 AM": "Period 3", "11:25 AM": "Break", "11:30 AM": "Period 4", "12:10 PM": "Lunch",
           "12:50 PM": "Period 5", "01:30 PM": "Break", "01:35 PM": "Period 6", "02:15 PM": "After School"}
tuesday = {'05:00 AM': "Before School", '09:00 AM': 'Period 1', '09:40 AM': "Break", "09:45 AM": 'Period 2', "10:25 AM": "Recess",
           "10:45 AM": "Period 3", "11:25 AM": "Break", "11:30 AM": "Period 4", "12:10 PM": "Lunch",
           "12:50 PM": "Period 5", "01:30 PM": "Break", "01:35 PM": "Period 6", "02:15 PM": "After School"}
wednesday = {'05:00 AM': "Before School", '08:50 AM': 'Year Meeting', '09:00 AM': 'Period 1', '09:40 AM': "Break", "09:45 AM": 'Period 2', "10:25 AM": "Recess",
           "10:45 AM": "Period 3", "11:25 AM": "After School"}
thursday = {'05:00 AM': "Before School", '09:00 AM': 'Period 1', '09:40 AM': "Break", "09:45 AM": 'Period 2', "10:25 AM": "Recess",
           "10:45 AM": "Period 3", "11:25 AM": "Break", "11:30 AM": "Period 4", "12:10 PM": "Lunch",
           "12:50 PM": "Period 5", "01:30 PM": "Break", "01:35 PM": "Period 6", "02:15 PM": "After School"}
friday = {'05:00 AM': "Before School", '09:00 AM': 'Period 1', '09:40 AM': "Break", "09:45 AM": 'Period 2', "10:25 AM": "Recess",
           "10:45 AM": "Period 3", "11:25 AM": "Break", "11:30 AM": "Period 4", "12:10 PM": "Lunch",
           "12:50 PM": "Period 5", "01:30 PM": "Break", "01:35 PM": "Period 6", "02:15 PM": "After School"}

listoftimes = [monday, tuesday, wednesday, thursday, friday]

# knowledge
weekdays = {0: monday, 1: tuesday, 2: wednesday, 3: thursday, 4: friday}
periodids = {
    7: {
        'link': '1FAIpQLSf0wNsk9bJF9VxF-gZ7DAN6hvov3vr1EFHZrMyRk0WRQ_m8bA',
        "firstname": "518967158",
        "lastname": "110753369",
        "date": "343023419",
        "week": "896682597",
        "A": {
            "day": "2065827557",
            "Monday": {
                "period": "579252825",
                "1": "1492132211",
                "2": "276183671",
                "3": "2065002841",
                "4": "1207394977",
                "5": "677739964",
                "6": "356233713"
            },
            "Tuesday": {
                "period": "1753659730",
                "1": "1747443788",
                "2": "1191485534",
                "3": "442871464",
                "4": "1690614521",
                "5": "1297771223",
                "6": "1690635674"
            },
            "Wednesday": {
                "period": "1349263448",
                "1": "731517626",
                "2": "908867313",
                "3": "917085736"
            },
            "Thursday": {
                "period": "74733179",
                "1": "710525462",
                "2": "701704392",
                "3": "495635040",
                "4": "2054113039",
                "5": "676088789",
                "6": "619053855"
            },
            "Friday": {
                "period": "1725454409",
                "1": "2121273402",
                "2": "673317393",
                "3": "1322064346",
                "4": "307001899",
                "5": "1610168471",
                "6": "10559910"
            }
        },
        "B": {
            "day": "271738821",
            "Monday": {
                "period": "1551900997",
                "1": "240254549",
                "2": "1901887516",
                "3": "1842762448",
                "4": "369381181",
                "5": "1143620765",
                "6": "1876234890"
            },
            "Tuesday": {
                "period": "1363297772",
                "1": "1689193216",
                "2": "805772599",
                "3": "1169408241",
                "4": "1305592232",
                "5": "308033600",
                "6": "2135861899"
            },
            "Wednesday": {
                "period": "984080195",
                "1": "583476471",
                "2": "1588032036",
                "3": "1927255769"
            },
            "Thursday": {
                "period": "515606393",
                "1": "846552217",
                "2": "525238872",
                "3": "1316732497",
                "4": "1302706396",
                "5": "1375851339",
                "6": "1984960800"
            },
            "Friday": {
                "period": "1012986239",
                "1": "1249552199",
                "2": "2108038679",
                "3": "259661783",
                "4": "1929946335",
                "5": "948648490",
                "6": "585314848"
            }
        }
    },
    8: {
        'link': '1FAIpQLSdBn_QwHom86htHoZYGuG6YjXTvjL_-IJoCdoiYMVVbZMwU9g',
        "week": '1166771392',
        'date': '1193583720',
        'firstname': '42490989',
        'lastname': '653941905',
        "A": {
            "day": '449469481',
            "Monday": {
                "period": "669622984",
                "1": "1601785072",
                "2": "492614766",
                "3": "1389174264",
                "4": "1309283006",
                "5": "458631184",
                "6": "1052707520"
            },
            "Tuesday": {
                "period": "1898890906",
                "1": "645868928",
                "2": "591814589",
                "3": "1989555554",
                "4": "1779939051",
                "5": "749475928",
                "6": "2067319021"
            },
            "Wednesday": {
                "period": "371344035",
                "1": "615392324",
                "2": "1598202951",
                "3": "1998943124"
            },
            "Thursday": {
                "period": "1449705738",
                "1": "2109723926",
                "2": "152756583",
                "3": "2036232942",
                "4": "633789239",
                "5": "649117299",
                "6": "405853907"
            },
            "Friday": {
                "period": "524423421",
                "1": "622654647",
                "2": "1194219654",
                "3": "2006748060",
                "4": "91350098",
                "5": "17980361",
                "6": "1677288381"
            }
        },
        "B": {
            'day': '1844771487',
            "Monday": {
                "period": "1662723045",
                "1": "578683047",
                "2": "2103493675",
                "3": "1868050784",
                "4": "1275661507",
                "5": "1861900416",
                "6": "2035399927"
            },
            "Tuesday": {
                "period": "614317995",
                "1": "1397309710",
                "2": "831803163",
                "3": "1971468528",
                "4": "1450195995",
                "5": "1882416998",
                "6": "1571751628"
            },
            "Wednesday": {
                "period": "855393316",
                "1": "211915260",
                "2": "2134045129",
                "3": "1833835893"
            },
            "Thursday": {
                "period": "105918712",
                "1": "1805358208",
                "2": "1784111846",
                "3": "497683945",
                "4": "1485938331",
                "5": "1920620585",
                "6": "696300742"
            },
            "Friday": {
                "period": "115181569",
                "1": "951673188",
                "2": "1147840262",
                "3": "1342635955",
                "4": "1211898769",
                "5": "1627945464",
                "6": "1651302723"
            }

        }
    },
    9: {
        'link': '1FAIpQLSc1aXXrENpHmaJ30zlmR4xWnNv6mRw4jKJSiZeUErAG9e6bdw',
        "week": '1166771392',
        'date': '1193583720',
        'firstname': '1133929150',
        'lastname': '653941905',
        "A": {
            "day": '449469481',
            "Monday": {
                'period': '669622984',
                "1": "1601785072",
                "2": "492614766",
                "3": "1389174264",
                "4": "1309283006",
                "5": "458631184",
                "6": "1052707520"
            },
            "Tuesday": {
                'period': '1898890906',
                "1": "517123644",
                "2": "591814589",
                "3": "1989555554",
                "4": "1779939051",
                "5": "749475928",
                "6": "2067319021"
            },
            "Wednesday": {
                'period': '371344035',
                "1": "565592115",
                "2": "1598202951",
                "3": "1998943124"
            },
            "Thursday": {
                'period': '1449705738',
                "1": "1120583654",
                "2": "152756583",
                "3": "2036232942",
                "4": "633789239",
                "5": "649117299",
                "6": "405853907"
            },
            "Friday": {
                'period': '524423421',
                "1": "622654647",
                "2": "1194219654",
                "3": "2006748060",
                "4": "91350098",
                "5": "17980361",
                "6": "1677288381"
            }
        },
        "B": {
            'day': '1844771487',
            "Monday": {
                'period': '1662723045',
                "1": "578683047",
                "2": "2103493675",
                "3": "1868050784",
                "4": "1275661507",
                "5": "1861900416",
                "6": "2035399927"
            },
            "Tuesday": {
                'period': '614317995',
                "1": "396169425",
                "2": "831803163",
                "3": "1971468528",
                "4": "1450195995",
                "5": "1882416998",
                "6": "1571751628"
            },
            "Wednesday": {
                'period': '855393316',
                "1": "1673382255",
                "2": "2134045129",
                "3": "1833835893"
            },
            "Thursday": {
                'period': '105918712',
                "1": "853608133",
                "2": "1784111846",
                "3": "497683945",
                "4": "1485938331",
                "5": "1920620585",
                "6": "696300742"
            },
            "Friday": {
                'period': '115181569',
                "1": "951673188",
                "2": "1147840262",
                "3": "1342635955",
                "4": "1211898769",
                "5": "1627945464",
                "6": "1651302723"
            }
        }
    },
    10: {
        'link': '1FAIpQLSew3K82Uj9SRrtd0C1wHyC4Rn9neUmOCy1AzcCz7tRYJzFHGw',
        "firstname": "1587805380",
        "lastname": "653941905",
        "date": "1193583720",
        "week": "1166771392",
        "A": {
            "day": "449469481",
            "Monday": {
                "period": "669622984",
                "1": "1601785072",
                "2": "492614766",
                "3": "1389174264",
                "4": "1309283006",
                "5": "458631184",
                "6": "1052707520"
            },
            "Tuesday": {
                "period": "1898890906",
                "0": "645868928",
                "1": "1530194634",
                "2": "591814589",
                "3": "1989555554",
                "4": "1779939051",
                "5": "749475928",
                "6": "2067319021"
            },
            "Wednesday": {
                "period": "371344035",
                "0": "615392324",
                "1": "23102432",
                "2": "1598202951",
                "3": "1998943124"
            },
            "Thursday": {
                "period": "1449705738",
                "0": "2109723926",
                "1": "594493818",
                "2": "152756583",
                "3": "2036232942",
                "4": "633789239",
                "5": "649117299",
                "6": "405853907"
            },
            "Friday": {
                "period": "524423421",
                "1": "622654647",
                "2": "1194219654",
                "3": "2006748060",
                "4": "91350098",
                "5": "17980361",
                "6": "1677288381"
            }
        },
        "B": {
            "day": "1844771487",
            "Monday": {
                "period": "1662723045",
                "1": "578683047",
                "2": "2103493675",
                "3": "1868050784",
                "4": "1275661507",
                "5": "1861900416",
                "6": "2035399927"
            },
            "Tuesday":{
                "period": "614317995",
                "0": "1397309710",
                "1": "1055829179",
                "2": "831803163",
                "3": "1971468528",
                "4": "1450195995",
                "5": "1882416998",
                "6": "1571751628"
            },
            "Wednesday": {
                "period": "855393316",
                "0": "211915260",
                "1": "1744106310",
                "2": "2134045129",
                "3": "1833835893"
            },
            "Thursday": {
                "period": "105918712",
                "0": "1805358208",
                "1": "1689812512",
                "2": "1784111846",
                "3": "497683945",
                "4": "1485938331",
                "5": "1920620585",
                "6": "696300742"
            },
            "Friday": {
                "period": "115181569",
                "1": "951673188",
                "2": "1147840262",
                "3": "1342635955",
                "4": "1211898769",
                "5": "1627945464",
                "6": "1651302723"
            }
        }
    },
    11: {
        'link': '1FAIpQLScVR8KK7CPhdcbgg0CkpCNEofQEKy0h8uyw0JCFsPPh0EJFhg',
        "week": '896682597',
        'date': '343023419',
        'firstname': '190083598',
        'lastname': '110753369',
        "A": {
            "day": "2065827557",
            "Monday": {
                "period": "579252825",
                "0": "740307665",
                "1": "1492132211",
                "2": "276183671",
                "3": "2065002841",
                "4": "1207394977",
                "5": "677739964",
                "6": "356233713"
            },
            "Tuesday": {
                "period": "1753659730",
                "0": "1662419712",
                "1": "1747443788",
                "2": "1191485534",
                "3": "442871464",
                "4": "1690614521",
                "5": "1297771223",
                "6": "1690635674"
            },
            "Wednesday": {
                "period": "1349263448",
                "0": "1852926696",
                "1": "731517626",
                "2": "908867313",
                "3": "917085736"
            },
            "Thursday": {
                "period": "74733179",
                "0": "774019403",
                "1": "710525462",
                "2": "701704392",
                "3": "495635040",
                "4": "2054113039",
                "5": "676088789",
                "6": "619053855"
            },
            "Friday": {
                "period": "1725454409",
                "0": "2121273402",
                "1": "972632888",
                "2": "673317393",
                "3": "1322064346",
                "4": "307001899",
                "5": "1610168471",
                "6": "10559910"
            }
        },
        "B": {
            "day": "271738821",
            "Monday": {
                "period": "1551900997",
                "0": "768672961",
                "1": "240254549",
                "2": "1901887516",
                "3": "1842762448",
                "4": "369381181",
                "5": "1143620765",
                "6": "1876234890"
            },
            "Tuesday": {
                "period": "1363297772",
                "0": "441118627",
                "1": "1689193216",
                "2": "805772599",
                "3": "1169408241",
                "4": "1305592232",
                "5": "308033600",
                "6": "2135861899"
            },
            "Wednesday": {
                "period": "984080195",
                "0": "589120673",
                "1": "583476471",
                "2": "1588032036",
                "3": "1927255769"
            },
            "Thursday": {
                "period": "515606393",
                "0": "1502124067",
                "1": "846552217",
                "2": "525238872",
                "3": "1316732497",
                "4": "1302706396",
                "5": "1375851339",
                "6": "1984960800"
            },
            "Friday": {
                "period": "1012986239",
                "0": "461874511",
                "1": "1249552199",
                "2": "2108038679",
                "3": "259661783",
                "4": "1929946335",
                "5": "948648490",
                "6": "585314848"
            }
        }
    },
    12: {
        "link": "1FAIpQLSdqg7NnSAYiZjIafsTDwsaemF1ZRmBNi4yP5uYxEw5f0O0d6A",
        "firstname": '207121423',
        "lastname": '110753369',
        "date": '343023419',
        "week": '896682597',
        "A": {
            "day": '2065827557',
            "Monday": {
                "period": "579252825",
                "0": "740307665",
                "1": "1492132211",
                "2": "276183671",
                "3": "2065002841",
                "4": "1207394977",
                "5": "677739964",
                "6": "356233713"
            },
            "Tuesday": {
                "period": "1753659730",
                "0": "1662419712",
                "1": "1747443788",
                "2": "1191485534",
                "3": "442871464",
                "4": "1690614521",
                "5": "1297771223",
                "6": "1690635674"
            },
            "Wednesday": {
                "period": "1349263448",
                "0": "1852926696",
                "1": "731517626",
                "2": "908867313",
                "3": "917085736"
            },
            "Thursday": {
                "period": "74733179",
                "0": "774019403",
                "1": "710525462",
                "2": "701704392",
                "3": "495635040",
                "4": "2054113039",
                "5": "676088789",
                "6": "619053855"
            },
            "Friday": {
                "period": "1725454409",
                "0": "1436643494",
                "1": "2121273402",
                "2": "673317393",
                "3": "1322064346",
                "4": "307001899",
                "5": "1610168471",
                "6": "10559910"
            }
        },
        "B": {
            "day": '271738821',
            "Monday": {
                "period": "1551900997",
                "0": "768672961",
                "1": "240254549",
                "2": "1901887516",
                "3": "1842762448",
                "4": "369381181",
                "5": "1143620765",
                "6": "1876234890"
            },
            "Tuesday": {
                "period": "1363297772",
                "0": "441118627",
                "1": "1689193216",
                "2": "805772599",
                "3": "1169408241",
                "4": "1305592232",
                "5": "308033600",
                "6": "2135861899"
            },
            "Wednesday": {
                "period": "984080195",
                "0": "589120673",
                "1": "583476471",
                "2": "1588032036",
                "3": "1927255769"
            },
            "Thursday": {
                "period": "515606393",
                "0": "1502124067",
                "1": "846552217",
                "2": "525238872",
                "3": "1316732497",
                "4": "1302706396",
                "5": "1375851339",
                "6": "1984960800"
            },
            "Friday": {
                "period": "1012986239",
                "0": "509435898",
                "1": "1249552199",
                "2": "2108038679",
                "3": "259661783",
                "4": "1929946335",
                "5": "948648490",
                "6": "585314848"
            }
        }
    }
}

# funcs

async def dmembed(userid, embed):
    user = await bot.fetch_user(int(userid))
    try:
        await user.send(embed = embed)
    except:
        print(f'dm failed {user.name}')

def weekday():
    return weekdays[datetime.datetime.today().weekday()]

def timeformat(time):
    rtnval =  datetime.datetime.strptime(time, "%I:%M %p")
    rtnval = int(datetime.datetime.strftime(rtnval, "%H%M"))
    return rtnval

def updatetimetable(currenttime, currentweekday):
    global fields
    for time in currentweekday.keys():
        timetableembed.fields[fields[time]] = timetableembed.set_field_at(index=fields[time], name=currentweekday[time], value=time, inline = False)
    # i = 0
    for time in currentweekday.keys():
        # if i == 0:
        #     i = 1
        #     continue
        if timeformat(currenttime) < timeformat(time):
            today = datetime.datetime.today()
            if int(today.strftime("%W")) % 2 == 0:
                week = 'A'
            else:
                week = 'B'
            if currenttime[0] == '0':
                currenttime = currenttime[1:]
            timetableembed.set_field_at(index=fields[pasttime], name=f"{currentweekday[pasttime]} :star:", value=f""
                                                                                                                 f"*{pasttime}*", inline = False)
            timetableembed.description = f"**Current Time: {currenttime}\nDate: {datetime.datetime.now().strftime('%d/%m/%Y')}\nWeek: Week {week}**"
            timetableembed.set_footer(text = f"Time until next period: {remainingtime(time)}")
            break
        pasttime = time
    else:
        today = datetime.datetime.today()
        if int(today.strftime("%W")) % 2 == 0:
            week = 'A'
        else:
            week = 'B'
        if currenttime[0] == '0':
            currenttime = currenttime[1:]
        timetableembed.set_field_at(index=fields[time], name=f"{currentweekday[time]} :star:", value=f"*{time}*", inline=False)
        timetableembed.description = f"**Current Time: {currenttime}\nDate: {datetime.datetime.now().strftime('%d/%m/%Y')}\nWeek: Week {week}**"
        timetableembed.set_footer(text = '')

def minutesformat(minutes):
    if minutes == 1:
        return f"{minutes} minute"
    else:
        return f"{minutes} minutes"

def secondsformat(sec):
    if sec == 1:
        return f"{sec} second"
    else:
        return f"{sec} seconds"

def remainingtime(targettime):
    # times in %I:%M %p
    # %h%M
    targettime = datetime.datetime.strptime(targettime, "%I:%M %p")
    crnttime = str(datetime.datetime.now().strftime("%H%M%S"))
    targettime = str(targettime.strftime("%H%M"))
    crnttime = int(crnttime[0:2])*60 + int(crnttime[2:4])
    targettime = int(targettime[0:2]) * 60 + int(targettime[2:4])
    remaining = int(targettime) - int(crnttime) - 1
    seconds = 60 - int(datetime.datetime.now().strftime("%S"))
    if seconds == 60:
        seconds = 0
        remaining += 1
    rtnval = str(minutesformat(remaining) + ' ' + secondsformat(seconds))
    if remaining <= 0:
        rtnval = secondsformat(seconds)
    if seconds <= 0:
        rtnval = minutesformat(remaining)
    return rtnval

def grablink(period, year):
    today = datetime.datetime.today()
    if int(today.strftime("%W")) % 2 == 0:
        week = 'Week+A'
    else:
        week = 'Week+B'

    rtnval = "https://docs.google.com/forms/d/e/" + periodids[year]['link'] + '/viewform?usp=pp_url'
    rtnval += '&entry.' + periodids[year]['date'] + '=' + today.strftime("%Y-%m-%d")
    rtnval += "&entry." + periodids[year]['week'] + "=" + week
    rtnval += "&entry." + periodids[year][week[-1]]['day'] + "=" + today.strftime("%A")
    rtnval += '&entry.' + periodids[year][week[-1]][today.strftime("%A")]['period'] + "=" + period[-1]
    return rtnval

async def sendpersonallinks(period):
    for userfile in os.listdir(r"C:\Users\Therealtin\Desktop\Learning\Coding\Discord\Timetable\User Timetables"):
        if 'Period' in period:
            today = datetime.datetime.today()
            if int(today.strftime("%W")) % 2 == 0:
                week = 'A'
            else:
                week = 'B'
            periodcode = week + today.strftime("%A") + period[-1]

            with open(r'C:\Users\Therealtin\Desktop\Learning\Coding\Discord\Timetable\User Timetables\\' + userfile, "r") as usertimetable:
                usertimetable = usertimetable.read()
                usertimetable = json.loads(usertimetable)
            year = usertimetable['year']
            link = grablink(period, year)
            link += '&entry.' + periodids[year][week][today.strftime("%A")][period[-1]] + '=' + usertimetable[periodcode].replace(' ', '+')
            link += '&entry.' + periodids[year]['firstname'] + '=' + usertimetable['firstname']
            link += '&entry.' + periodids[year]['lastname'] + '=' + usertimetable['lastname']
            if usertimetable[periodcode] == 'free period':
                embed = discord.Embed(colour=discord.colour.Colour.from_rgb(
                    255, 255, 255), title=period,
                    description=f'it is now {period.lower()}\nyou have a free period now')
            else:
                embed = discord.Embed(colour=discord.colour.Colour.from_rgb(
                                    255, 255, 255), title = period, description = f'it is now {period.lower()}\n[Your personalised attendance form]({link})')
            await dmembed(usertimetable['id'], embed)

            print(userfile, period)

        else:
            with open(r'C:\Users\Therealtin\Desktop\Learning\Coding\Discord\Timetable\User Timetables\\' + userfile, "r") as usertimetable:
                usertimetable = usertimetable.read()
                usertimetable = json.loads(usertimetable)
            embed = discord.Embed(colour=discord.colour.Colour.from_rgb(
                                255, 255, 255), title = period, description = f'It is now {period.lower()}')
            await dmembed(usertimetable['id'], embed)
            print(userfile, 'linkless')


@bot.event
async def on_ready():
    # Checks for the right Guild to connect to
    for guild in bot.guilds:
        if guild.name == GUILD:
            print(
                f'{bot.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})\n'
            )
            break

# commands

# for time
fields = {}
for day in listoftimes:
    if weekday() == day:
        n = 0
        for time in day.keys():
            fields[time] = n
            timetableembed.fields[n] = timetableembed.add_field(name = day[time], value = time, inline = False)
            n += 1
        break
@bot.command()
async def time(ctx):
    pinged = []
    await ctx.message.delete()
    global currenttime
    global fields

    if weekday() not in listoftimes:
        ctx.channel.send("*Wait, it isn't a weekday I'm pre sure*")
        exit()

    currenttime = datetime.datetime.now().strftime('%I:%M %p')
    secount = datetime.datetime.now().strftime('%S')
    updatetimetable(currenttime, weekday())

    timetablemessage = await ctx.channel.send(embed = timetableembed)
    print(f'time active in channel: {ctx.channel.name}')

    while True:
        sleep(0.1)
        if secount != datetime.datetime.now().strftime('%S'):
            secount = datetime.datetime.now().strftime('%S')
            if int(secount) % 5 == 0:
                currenttime = datetime.datetime.now().strftime('%I:%M %p')
                updatetimetable(currenttime, weekday())

                await timetablemessage.edit(embed=timetableembed)

                for time in weekday().keys():
                    if currenttime == time:
                        if weekday()[time] in pinged:
                            break
                        try:
                            await pingmsg.delete()
                        except UnboundLocalError:
                            print("Variable error, pingmsg doesn't exist")
                            pass
                        print(weekday()[time] + '\n')
                        pinged.append(weekday()[time])

                        # if "Period" in weekday()[time]:
                        if False:
                            #global ping msg
                            pingmsg = await ctx.channel.send("<@&877323402329866240>",
                                embed=discord.Embed(title=weekday()[time],
                                description=f"It is now {weekday()[time].lower()}\n\n"
                                            f"Generic pre-filled forms:\n"
                                            f"[Year 7 Attendance Form]({grablink(weekday()[time].lower(), 7)})\n"
                                            f"[Year 8 Attendance Form]({grablink(weekday()[time].lower(), 8)})\n"
                                            f"[Year 9 Attendance Form]({grablink(weekday()[time].lower(), 9)})\n"
                                            f"[Year 10 Attendance Form]({grablink(weekday()[time].lower(), 10)})\n"
                                            f"[Year 11 Attendance Form]({grablink(weekday()[time].lower(), 11)})\n"
                                            f"[Year 12 Attendance Form]({grablink(weekday()[time].lower(), 12)})",
                                colour=discord.colour.Colour.from_rgb(
                                255, 255, 255)))
                        else:
                            pingmsg = await ctx.channel.send("<@&877323402329866240>", embed=discord.Embed(title=weekday()[time], description=f"It is now {weekday()[time].lower()}", colour=discord.colour.Colour.from_rgb(255, 255, 255)))

                        await sendpersonallinks(weekday()[time])

                if not any(currenttime == time for time in weekday().keys()):
                    pinged = []

@bot.command()
async def test(ctx):
    time = "02:15 PM"


bot.run(TOKEN)

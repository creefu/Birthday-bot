import discord
from discord.ext import commands

import datetime
from datetime import date

# detect the key symbol to start the command
bot =  commands.Bot(command_prefix = '!')

# the command name bd will follow right after !, the key symbol
@bot.command()
async def bd(ctx, dob):
  # split the string  
  dobstr = dob.split('/')

  # saperate the year, month and date
  y = int(dobstr[0])
  m = int(dobstr[1])
  d = int(dobstr[2])
  
  # use today's date to set up, no point knowing the birthdays already happen
  today = date.today()
  
  # future 50 years since dob
  last = y+50

  while(y<=last):
    # print(datetime.date(y,m,d))
    # print(datetime.date(y,m,d).weekday())
# there is not point of knowing the pass birthdays, use today's year to see if applies to the future
    if(today.year <= y):
      if(datetime.date(y,m,d).weekday() == 5):
        # responde with years and the day of it
        await ctx.send("Years of your bday weekend: %d Saturday" %(y))
      if(datetime.date(y,m,d).weekday() == 6):
        await ctx.send("Years of your bday weekend: %d Sunday" %(y))

    # await ctx.send(y)
    #add 1 year per loop
    y+=1

  await ctx.send('Happy early birthdays :)')


# token
bot.run('Nzk3MjE2MzI4NDg1NTY4NTQy.X_jPkA.xJLiQqoUgTi3VZS0IO0Ir1RLhPM')

# original script without using discord's python library
def main(dob):
    # request user bday
    #dob = '1999/08/05'

    # break the string apart
    dobar = dob.split('/')
    # saperate the year, month and date
    y = int(dobar[0])
    m = int(dobar[1])
    d = int(dobar[2])
    # print(type(y))
    print(y)
    print(m)
    print(d)

    next50(y,m,d)

def next50(y, m, d):
    last = y+50
    while(y<= last):
      # from the return values, check if they are weekends or not 5 is saturday, 6 is sunday
      if(checkWeekend(y, m, d) == 5 or checkWeekend(y, m, d) == 6):
        print("Your birthday weekeds are in the years of: %d" %(y))
      # add up to 50 years
      y+=1
        
def checkWeekend(y, m, d):
  # setting up the date
  dob = datetime.date(y,m,d)
  # too see what is the day of the week for the dob
  check = dob.weekday()
  #should return the number of the weeek (0 is monday)
  return check

# resource
# https://discordpy.readthedocs.io/en/stable/

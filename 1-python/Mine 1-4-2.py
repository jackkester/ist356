import datetime

mdy_slashes = "%m/%d/%Y"

def parsedate_mdy( text:str) -> datetime:
    return datetime.datetime.strptime(text, mdy_slashes)

def formatdate_ymd(date:datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d")

date = "06/07/2005"
date_dt = parsedate_mdy(date)
date_str = formatdate_ymd(date_dt)
print(date_str)
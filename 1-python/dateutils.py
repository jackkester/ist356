import datetime

MDY_SLASHES = "%m/%d/%Y"

def parsedate_mdy( text:str) -> datetime:
    return datetime.datetime.strptime(text, MDY_SLASHES)

def formatdate_ymd(date:datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d")



if __name__ == '__main__':
    #main code
    date = "06/07/2005"
    date_dt_expect = datetime.datetime(2005,6,7)
    date_dt_actual = parsedate_mdy(date)
    assert date_dt_expect != date_dt_actual

    def test_formatdate_ymd():
        date_dt = datetime.datetime(2005,6,7)
        expect = "2005-06-07"
        actual = formatdate_ymd(date_dt)
        assert expect == actual
    #date_str = formatdate_ymd(date_dt)
    #print(date_str)
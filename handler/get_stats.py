import requests
from views import country_id
import json
import datetime


def prettifier(func):
    def pretty(stats, date=None):
        data = func(stats, date)
        pretty_data = []
        for number in data:
            pretty = ""
            almost_pr = str(number)
            for i in range(-1, -len(almost_pr)-3, -3):
                pretty += almost_pr[i:i-3:-1] + " "
            pretty_data.append(pretty[::-1])
        return pretty_data
    return pretty


@prettifier
def get_needed_stats(stats, date=None):
    if date:
        return stats['total_cases'], stats['total_recoveries'], \
               stats['total_deaths'], stats['new_daily_cases'], \
               stats['new_daily_deaths']
    else:
        return stats['total_cases'], stats['total_recovered'], \
               stats['total_deaths'], stats['total_new_cases_today'], \
               stats['total_new_deaths_today']


class GetStats:
    @staticmethod
    def get_global_stats():
        req = requests.get("https://api.thevirustracker.com/"
                           "free-api?global=stats")
        statistics = req.json()['results'][0]
        return get_needed_stats(statistics)

    @staticmethod
    def get_country_stats(country, date):
        id_ = country_id.GetCountryId().get_id(country)
        statistics = ()
        print(id_, date)
        try:
            if date == None or date == datetime.date.today():
                req = requests.get(f"https://api.thevirustracker.com/"
                                   f"free-api?countryTotal={id_}")
                statistics = req.json()['countrydata'][0]
            elif date > datetime.date.today():
                return ()
            else:
                print("HERE!")
                req = requests.get(f"https://api.thevirustracker.com/"
                                   f"free-api?countryTimeline={id_}")
                day = (date.day < 10) * "0" + str(date.day)
                print(f"{date.month}/{day}/{date.year%100}")
                statistics = \
                    req.json()['timelineitems'][0][f"{date.month}" \
                                                   f"/{day}/{date.year%100}"]
        except (KeyError, ValueError, json.JSONDecodeError) as err:
            return ()
        else:
            return get_needed_stats(statistics, date)
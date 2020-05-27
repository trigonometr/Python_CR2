import requests
import views.country_id
import json
import datetime


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
        try:
            statistics = req.json()['results'][0]
            return get_needed_stats(statistics)
        except json.JSONDecodeError:
            return None

    @staticmethod
    def get_country_stats(country, date):
        id_ = views.country_id.GetCountryId().get_id(country)
        statistics = ()
        try:
            if date == None or date == datetime.date.today():
                req = requests.get(f"https://api.thevirustracker.com/"
                                   f"free-api?countryTotal={id_}")
                statistics = req.json()['countrydata'][0]
            elif date > datetime.date.today():
                return None
            else:
                req = requests.get(f"https://api.thevirustracker.com/"
                                   f"free-api?countryTimeline={id_}")
                day = (date.day < 10) * "0" + str(date.day)
                statistics = \
                    req.json()['timelineitems'][0][f"{date.month}" \
                                                   f"/{day}/{date.year%100}"]
            return get_needed_stats(statistics, date)
        except (KeyError, ValueError, json.JSONDecodeError) as err:
            return None

import pytest
import views.country_id
import handler.get_stats


@pytest.mark.parametrize('country_name,code', [
    ("Russia", "RU"), ("rusSia", "RU"),
    ("ussia", "Country404")
], ids=['normal', 'register mistake',
          "doesn't exist"])
def test_country_id_getter(country_name, code):
    assert views.country_id.GetCountryId().get_id(country_name) == code


@pytest.mark.parametrize('cntry,date,no_stats', [
    ('USA', '2020-05-05', False),
    ('USA', '2200-05-05', True),
    ('ASASHAI', '2020-05-05', True),
    ('ASASHAI', '2200-05-05', True)
], ids=['normal', 'fake-date', 'fake-country',
        'both fake cntry n date'])
def test_country_stats_getter_existing(cntry, date, no_stats):
    assert (handler.get_stats.GetStats().get_country_stats(
        cntry, date) is None) == no_stats

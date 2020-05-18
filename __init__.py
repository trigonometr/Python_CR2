import views.input_form
import handler.get_stats
import flask

app = flask.Flask(__name__, static_folder="static")
app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
def index():
    """ form for getting input data """
    data_form = views.input_form.InputForm()
    global_statistics = ()
    country_statistics = ()
    getter = handler.get_stats.GetStats()
    global_statistics = getter.get_global_stats()
    if data_form.validate_on_submit():
        country_statistics = \
            getter.get_country_stats(data_form.country_name.data,
                                     data_form.date.data)
    return flask.render_template('index.html', gl_st=global_statistics,
                                 cntry_st=country_statistics, form=data_form,
                                 country = data_form.country_name.data)


if __name__ == '__main__':
    app.run()




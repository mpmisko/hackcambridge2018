from www.web import create_app


app = create_app('dev')
app.run(debug=True, host="0.0.0.0",port=8085, threaded=True)
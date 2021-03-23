from flask import Flask, render_template, request

from models import word_corr

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', name='')




@app.route("/proj1",methods=["GET", 'POST'])
def Proj1():
    if request.method == 'POST':
        f = request.files['file'].read()
    # do logic here
    return render_template('proj1.html')



@app.route("/proj2", methods=["GET", 'POST'])
def proj2():
    content = {}
    option = ''
    if request.method == 'POST':
        f = request.form['sample']
        print(f)
        # word,options = word_corr(f)
        # content['words'] = word
        # option = options
        # print('no')
        # do logic here
    return render_template('proj2.html', value=content, value2=option)




@app.route("/styles")
def styles():
    return render_template('styles.html')


@app.route("/base")
def base():
    return render_template('base.html')






if __name__ == "__main__":
    app.run(debug=True)

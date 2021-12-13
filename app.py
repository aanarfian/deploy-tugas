from flask import Flask, render_template, request
import pickle
# import

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=['POST', 'GET'])
def home():
    hasil = []
    if request.method == "POST":
        if request.form.get("MCU") == '1':
            loaded_model = pickle.load(open('finalized_model_haji.sav', 'rb'))
        elif request.form.get("MCU") == '5':
            loaded_model = pickle.load(open('finalized_model_eks.sav', 'rb'))
        elif request.form.get("MCU") == '6':
            loaded_model = pickle.load(open('finalized_model_haji2.sav', 'rb'))
        elif request.form.get("MCU") == '7':
            loaded_model = pickle.load(open('finalized_model_karyawan.sav', 'rb'))
        elif request.form.get("MCU") == '3':
            loaded_model = pickle.load(open('finalized_model_perusahaan.sav', 'rb'))
        elif request.form.get("MCU") == '2':
            loaded_model = pickle.load(open('finalized_model_pns.sav', 'rb'))
        elif request.form.get("MCU") == '8':
            loaded_model = pickle.load(open('finalized_model_tkhi.sav', 'rb'))
        elif request.form.get("MCU") == '4':
            loaded_model = pickle.load(open('finalized_model_umum.sav', 'rb'))
        else:
            return render_template("index.html", content=[len(hasil),hasil])
        bulan = int(request.form.get("bulan"))
        for i in range(bulan):
            hasil.append(round(max(0, loaded_model.predict([[i+1+56]])[0][0])))
	
    return render_template("index.html", content=[len(hasil),hasil], is_home = True)

@app.route("/about", methods=['GET'])
def about():	
    return render_template("about.html", is_about= True)


if __name__ == "__name_-":
    app.run(debug=True)

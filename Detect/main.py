from flask import Flask,session, flash, url_for, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage 
import random
import os
import shutil
import json
import glob
from opencv_yolo import yolo_object_detection as yolo
import blueprints

app = Flask(__name__)
app.secret_key = 'secret_key'
#To prevent file naming conflicts
dir_id_list = []

@app.route('/', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
	    if request.files:
	        #Remove previously uploaded files
	        if session.get('id', False):
	            if os.path.exists(session.get('dir', None)):
	                shutil.rmtree(session['dir'])
	                try:
	                	dir_id_list.remove(session['id'])
	                except ValueError:
	                	pass
	        session['id'] = ''
	        while session.get('id', '') == '':
	            global new_dir
	            #Generate random id to add dir_name, such that two files cannot have the same name
	            num = random.randint(1, 2000)  
	            if num not in dir_id_list:
	                dir_id_list.append(num)
	                dir_id = str(num)
	                session['id'] = dir_id
	                new_dir = os.path.join('static/uploads', session['id'])
	                session['dir'] = new_dir

	        
	        if not os.path.exists(new_dir):
	            os.makedirs(new_dir)
	        
	      
	        for file in request.files.getlist('file[]'):
	            #Put image in new directory created
	            dir_name = os.path.join(new_dir, file.filename)
	            filename = file.save(dir_name)
	           
	        return 'Success'  
	return render_template('index.html')
@app.route('/detect', methods = ['POST'])
def detect():
    if request.method == 'POST':
        new_dir = session['dir']
        yolo.detect_land(new_dir, app.root_path)
        images = glob.glob(os.path.join(new_dir, '*'))
        
        return json.dumps(images)

@app.route('/blueprint', methods = ['GET'])
def blueprint():
	#blueprints.web()
	#blueprints.map()
	wid=int(yolo.returning_width())
	len=int(yolo.returning_length())
	squareInch=wid*len
	squareFoot=squareInch*0.00694444

	if squareFoot > 0 and squareFoot <= 1000:
		blueprints.web3()
		blueprints.three_marla()
		return render_template('home.html')
	elif squareFoot > 1000 and squareFoot <= 1700:
		blueprints.web5()
		blueprints.five_marla()
		return render_template('home.html')
	elif squareFoot > 1700 and squareFoot <= 2400:
		blueprints.web7()
		blueprints.seven_marla()
		return render_template('home.html')
	elif squareFoot > 2400 and squareFoot <= 3000:
		blueprints.web10()
		blueprints.ten_marla()
		return render_template('home.html')
	elif squareFoot > 3000 and squareFoot <= 6000:
		blueprints.web1Kanal()
		blueprints.one_kanal()
		return render_template('home.html')
	else:
		return render_template('temp.html')
	blueprints.web()
	blueprints.three_marla()

if __name__ == '__main__':
	app.run(debug = True)
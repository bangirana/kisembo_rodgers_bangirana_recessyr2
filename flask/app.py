from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a new WildConservation Species List
species_list = [
  {'name': 'Elephant', 'Habitat': 'Africa'},
  {'name': 'Lion', 'Habitat': 'Africa'},
  {'name': 'Girraffe', 'Habitat': 'Africa'},
  {'name': 'Wild Dog', 'Habitat': 'Africa'},
  {'name': 'Penguin', 'Habitat': 'Antarctica'},
  {'name': 'Polar Bear', 'Habitat': 'Antarctica'},
  {'name': 'Kangaroo', 'Habitat': 'Australia'},
  {'name': 'Koala', 'Habitat': 'Australia'},
  {'name': 'Tasmanian Devil', 'Habitat': 'Australia'},
  {'name': 'Panda', 'Habitat': 'Asia'},
  {'name': 'Tiger', 'Habitat': 'Asia'},
  {'name': 'Gorilla', 'Habitat': 'Africa'},
  {'name': 'Orangutan', 'Habitat': 'Asia'},
 ]

@app.route('/')
def index():
    return render_template('index.html', species_list = species_list)


@app.route('/add_species', methods = ['GET', 'POST'])
def add_species():
    if request.method == 'GET':
        return render_template('add_species.html')
    else:
        name = request.form['name']
        habitat = request.form['habitat']
        species_list.append({'name': name, 'Habitat': habitat})
        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=5005)
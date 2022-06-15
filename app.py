from flask import Flask, flash, jsonify, render_template, request, redirect, session, url_for
from model import Model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
db = Model()

@app.route('/')
def indeks():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registering', methods=['POST','GET'])
def registering():
    if request.method == 'POST' and request.form['tambahUser']:
        nama = request.form['nama']
        username = request.form['username']
        password = request.form['password']

        if db.register(nama,username,password):
            flash('User Berhasil Ditambahkan!')
        else:
            flash('User Gagal Ditambahkan')
        return render_template('register.html')
    else:
        return render_template('register.html')


@app.route('/login', methods=("GET","POST"))
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        user_key = request.form['password']

        db_user = db.index()
        cur = db_user.cursor()
        cur.execute('SELECT * from user where username=%s',(user_name,))
        user = cur.fetchone()
        cur.close()

        try:
            if len(user) > 0:
                if user_name == user[2] and user_key == user[3]:
                    session['user'] = user[1]
                    session['user_name'] = user[2]
                    session['user_key']  = user[3]
                    return render_template('home.html')
                else:
                    flash("Password Anda Salah!")
                    return render_template('login.html')
        except:
            flash("Username tidak ditemukan")
            return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/buku')
def buku():
    return render_template('buku.html')

@app.route('/apibuku', methods=['GET'])
def apibuku():
    data = db.lihatBuku()
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/formbuku')
def formBuku():
    return render_template('formbuku.html')

@app.route('/addbuku', methods=['POST','GET'])
def addBuku():
    if request.method =='POST' and request.form['tambahBuku']:
        id_user = request.form['id']
        judul   = request.form['judul']
        lokasi  = request.form['lokasi']
        penulis = request.form['penulis']
        thn_terbit = request.form['terbit']
        jenis   = request.form['jenis']
        status  = request.form['status']

        if db.tambahBuku(id_user,judul,lokasi,penulis,thn_terbit,jenis,status):
            flash("Data berhasil ditambah!")
        else:
            flash("Data gagal ditambah!")
        return redirect(url_for('buku'))
        
    else:
        return redirect(url_for('buku'))

@app.route('/detailbuku/<int:id>', methods=['GET','POST'])
def detailbuku(id):
    data = db.readByIdBuku(id)
    return render_template('detailbuku.html', data=data)

@app.route('/updatebuku/<int:id>', methods=['POST','GET'])
def updateBuku(id):
    data = db.readByIdBuku(id)
    session['update'] = id
    return render_template('updatebuku.html', update=data)

@app.route('/ubahbuku', methods=['POST','GET'])
def ubahBuku():
    if request.method == 'POST' and request.form['ubahBuku']:
        user_id = request.form['id']
        judul = request.form['judul']
        lokasi = request.form['lokasi']
        penulis = request.form['penulis']
        thn_terbit = request.form['terbit']
        jenis = request.form['jenis']
        status = request.form['status']

        if db.updateBuku(user_id,judul,lokasi,penulis,thn_terbit,jenis,status,session['update']):
            flash("Data berhasil diubah!")
        else:
            flash("Data gagal diubah!")

        return redirect(url_for('buku')) 
    else:  
        return redirect(url_for('buku'))

@app.route('/deletebuku/<int:id>', methods=['POST','GET'])
def deleteBuku(id):
    if request.method == 'GET':
        if db.deleteBuku(id):
            flash('ID : {} berhasil dihapus!'.format(id))
        else:
            flash('Data gagal dihapus!')
        return redirect(url_for('buku'))
    else:
        return redirect(url_for('buku'))

@app.route('/majalah')
def majalah():
    return render_template('majalah.html')

@app.route('/apimajalah', methods=['GET'])
def apimajalah():
    data = db.lihatMajalah()
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/formmajalah')
def formMajalah():
    return render_template('formmajalah.html')

@app.route('/addmajalah', methods=['POST','GET'])
def addMajalah():
    if request.method =='POST' and request.form['tambahMajalah']:
        id_user = request.form['id']
        judul   = request.form['judul']
        lokasi  = request.form['lokasi']
        volume = request.form['volume']
        edisi = request.form['edisi']
        status  = request.form['status']

        if db.tambahMajalah(id_user,judul,lokasi,volume,edisi,status):
            flash("Data berhasil ditambah!")
        else:
            flash("Data gagal ditambah!")
        return redirect(url_for('majalah'))
        
    else:
        return redirect(url_for('majalah'))

@app.route('/updatemajalah/<int:id>', methods=['POST','GET'])
def updateMajalah(id):
    data = db.readByIdMajalah(id)
    session['update'] = id
    return render_template('updatemajalah.html', update=data)

@app.route('/ubahmajalah', methods=['POST','GET'])
def ubahMajalah():
    if request.method == 'POST' and request.form['ubahMajalah']:
        user_id = request.form['id']
        judul = request.form['judul']
        lokasi = request.form['lokasi']
        volume = request.form['volume']
        edisi = request.form['edisi']
        status = request.form['status']

        if db.updateMajalah(user_id,judul,lokasi,volume,edisi,status,session['update']):
            flash("Data berhasil diubah!")
        else:
            flash("Data gagal diubah!")

        return redirect(url_for('majalah')) 
    else:  
        return redirect(url_for('majalah'))

@app.route('/deletemajalah/<int:id>', methods=['POST','GET'])
def deleteMajalah(id):
    if request.method == 'GET':
        if db.deleteMajalah(id):
            flash('ID : {} berhasil dihapus!'.format(id))
        else:
            flash('Data gagal dihapus!')
        return redirect(url_for('majalah'))
    else:
        return redirect(url_for('majalah'))
    
@app.route('/dvd')
def dvd():
    data = db.lihatDVD()
    return render_template('dvd.html', dvd=data)

@app.route('/apidvd', methods=['GET'])
def apidvd():
    data = db.lihatDVD()
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/formdvd')
def formDVD():
    return render_template('formdvd.html')

@app.route('/adddvd', methods=['POST','GET'])
def addDVD():
    if request.method =='POST' and request.form['tambahDVD']:
        id_user = request.form['id']
        judul   = request.form['judul']
        lokasi  = request.form['lokasi']
        direktor = request.form['direktor']
        thn_terbit = request.form['terbit']
        aktor = request.form['aktor']
        genre = ', '.join(request.form.getlist('genre'))
        status  = request.form['status']

        if db.tambahDVD(id_user,judul,lokasi,direktor,thn_terbit,aktor,genre,status):
            flash("Data berhasil ditambah!")
        else:
            flash("Data gagal ditambah!")
        return redirect(url_for('dvd'))
        
    else:
        return redirect(url_for('dvd'))

@app.route('/updatedvd/<int:id>', methods=['POST','GET'])
def updateDVD(id):
    data = db.readByIdDVD(id)
    session['update'] = id
    return render_template('updatedvd.html', update=data)

@app.route('/ubahdvd', methods=['POST','GET'])
def ubahDVD():
    if request.method == 'POST' and request.form['ubahDVD']:
        user_id = request.form['id']
        judul = request.form['judul']
        lokasi = request.form['lokasi']
        direktor = request.form['direktor']
        thn_terbit = request.form['terbit']
        aktor = request.form['aktor']
        genre = ', '.join(request.form.getlist('genre'))
        status = request.form['status']

        if db.updateDVD(user_id,judul,lokasi,direktor,thn_terbit,aktor,genre,status,session['update']):
            flash("Data berhasil diubah!")
        else:
            flash("Data gagal diubah!")

        return redirect(url_for('dvd')) 
    else:  
        return redirect(url_for('dvd'))

@app.route('/deletedvd/<int:id>', methods=['POST','GET'])
def deleteDVD(id):
    if request.method == 'GET':
        if db.deleteDVD(id):
            flash('ID : {} berhasil dihapus!'.format(id))
        else:
            flash('Data gagal dihapus!')
        return redirect(url_for('dvd'))
    else:
        return redirect(url_for('dvd'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
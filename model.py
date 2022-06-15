import mysql.connector

class Model:
    def index(self):
        db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'db'
        )

        return db

    def register(self,nama,username,password):
        idUser = ""
        db = Model.index(self)
        cur = db.cursor()
        sql = 'INSERT INTO user VALUES(%s,%s,%s,%s)'
        val = (idUser,nama,username,password)
        cur.execute(sql,val)
        db.commit()
        return True

    def lihatBuku(self):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('SELECT * from buku')
        return cur.fetchall()

    def tambahBuku(self,id_user,judul,lokasi,penulis,thn_terbit,jenis,status):
        db = Model.index(self)
        cur = db.cursor()
        sql = 'INSERT INTO buku VALUES(%s,%s,%s,%s,%s,%s,%s)'
        val = (id_user,judul,lokasi,penulis,thn_terbit,jenis,status)
        cur.execute(sql,val)
        db.commit()
        return True

    def readByIdBuku(self,id):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('SELECT * from buku where id = %s', (id,))
        return cur.fetchall()

    def updateBuku(self,id_user,judul,lokasi,penulis,thn_terbit,jenis,keterangan,id):
        db = Model.index(self)
        cur = db.cursor()
        sql = "UPDATE buku SET id=%s, judul=%s, lokasi=%s, penerbit=%s, thn_terbit=%s, jenis=%s, keterangan=%s WHERE id=%s"
        val = (id_user,judul,lokasi,penulis,thn_terbit,jenis,keterangan,id)
        cur.execute(sql,val)
        db.commit()
        return True

    def deleteBuku(self,id):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('DELETE from buku WHERE id=%s', (id,))
        db.commit()
        return True

    def lihatMajalah(self):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('SELECT * from majalah')
        return cur.fetchall()

    def tambahMajalah(self,id_user,judul,lokasi,volume,edisi,status):
        db = Model.index(self)
        cur = db.cursor()
        sql = 'INSERT INTO majalah VALUES(%s,%s,%s,%s,%s,%s)'
        val = (id_user,judul,lokasi,volume,edisi,status)
        cur.execute(sql,val)
        db.commit()
        return True

    def readByIdMajalah(self,id):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('SELECT * from majalah where id = %s', (id,))
        return cur.fetchall()

    def updateMajalah(self,id_user,judul,lokasi,volume,edisi,keterangan,id):
        db = Model.index(self)
        cur = db.cursor()
        sql = "UPDATE majalah SET id=%s, judul=%s, lokasi=%s, volume=%s, edisi=%s, keterangan=%s WHERE id=%s"
        val = (id_user,judul,lokasi,volume,edisi,keterangan,id)
        cur.execute(sql,val)
        db.commit()
        return True

    def deleteMajalah(self,id):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('DELETE from majalah WHERE id=%s', (id,))
        db.commit()
        return True

    def lihatDVD(self):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('SELECT * from dvd')
        return cur.fetchall()

    def tambahDVD(self,id_user,judul,lokasi,direktor,thn_terbit,aktor,genre,status):
        db = Model.index(self)
        cur = db.cursor()
        sql = 'INSERT INTO dvd VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (id_user,judul,lokasi,direktor,thn_terbit,aktor,genre,status)
        cur.execute(sql,val)
        db.commit()
        return True

    def readByIdDVD(self,id):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('SELECT * from dvd where id = %s', (id,))
        return cur.fetchall()

    def updateDVD(self,id_user,judul,lokasi,direktor,thn_terbit,aktor,genre,keterangan,id):
        db = Model.index(self)
        cur = db.cursor()
        sql = "UPDATE dvd SET id=%s, judul=%s, lokasi=%s, direktor=%s, tahun=%s, aktor=%s, genre=%s, keterangan=%s WHERE id=%s"
        val = (id_user,judul,lokasi,direktor,thn_terbit,aktor,genre,keterangan,id)
        cur.execute(sql,val)
        db.commit()
        return True

    def deleteDVD(self,id):
        db = Model.index(self)
        cur = db.cursor()
        cur.execute('DELETE from dvd WHERE id=%s',(id,))
        db.commit()
        return True
from flask import Flask, render_template, jsonify, request, redirect, url_for
import cx_Oracle
import json

app = Flask(__name__)


def connect_to_database():
    connection_details = {
        'user': 'intro_user',
        'password': 'mariaadina#22',
        'dsn': 'localhost:1521/xe'
    }
    return cx_Oracle.connect(**connection_details)




@app.route('/voluntari')
def list_voluntari():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM VOLUNTARI ORDER BY ID_VOLUNTAR")
        voluntari_data = cursor.fetchall()
        connection.close()
        return render_template('list_voluntari_sorted.html', voluntari_data=voluntari_data)
    else:
        return "Failed to connect to the database."

@app.route('/departamente')
def list_departamente():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM DEPARTAMENTE ORDER BY ID_DEPARTAMENT")
        departamente_data = cursor.fetchall()
        connection.close()
        return render_template('list_departamente_sorted.html', departamente_data=departamente_data)
    else:
        return "Failed to connect to the database."

@app.route('/functii')
def list_functii():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM FUNCTII ORDER BY ID_FUNCTIE")
        functii_data = cursor.fetchall()
        connection.close()
        return render_template('list_functii_sorted.html', functii_data=functii_data)
    else:
        return "Failed to connect to the database."

@app.route('/proiecte')
def list_proiecte():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PROIECTE ORDER BY ID_PROIECT")
        proiecte_data = cursor.fetchall()
        connection.close()
        return render_template('list_proiecte_sorted.html', proiecte_data=proiecte_data)
    else:
        return "Failed to connect to the database."

@app.route('/task_uri')
def list_task_uri():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM TASK_URI ORDER BY ID_TASK")
        task_uri_data = cursor.fetchall()
        connection.close()
        return render_template('list_task_uri_sorted.html', task_uri_data=task_uri_data)
    else:
        return "Failed to connect to the database."

@app.route('/task_voluntar')
def list_task_voluntar():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM TASK_VOLUNTAR ORDER BY ID_ASOC")
        task_voluntar_data = cursor.fetchall()
        connection.close()
        return render_template('list_task_voluntar_sorted.html', task_voluntar_data=task_voluntar_data)
    else:
        return "Failed to connect to the database."

@app.route('/sponsori')
def list_sponsori():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SPONSORI ORDER BY ID_SPONSOR")
        sponsori_data = cursor.fetchall()
        connection.close()
        return render_template('list_sponsori_sorted.html', sponsori_data=sponsori_data)
    else:
        return "Failed to connect to the database."

@app.route('/sponsor_proiect')
def list_sponsor_proiect():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SPONSOR_PROIECT ORDER BY ID_SPONSOR_PROIECT")
        sponsor_proiect_data = cursor.fetchall()
        connection.close()
        return render_template('list_sponsor_proiect_sorted.html', sponsor_proiect_data=sponsor_proiect_data)
    else:
        return "Failed to connect to the database."

@app.route('/locatii')
def list_locatii():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM LOCATII ORDER BY ID_LOCATIE")
        locatii_data = cursor.fetchall()
        connection.close()
        return render_template('list_locatii_sorted.html', locatii_data=locatii_data)
    else:
        return "Failed to connect to the database."

@app.route('/editii')
def list_editii():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM EDITIE ORDER BY ID_EDITIE")
        editii_data = cursor.fetchall()
        connection.close()
        return render_template('list_editie_sorted.html', editii_data=editii_data)
    else:
        return "Failed to connect to the database."


class Voluntar():
    def __init__(self):
        self.ID_VOLUNTAR = None
        self.NUME = None
        self.PRENUME = None
        self.NR_TELEFON = None
        self.DEPARTAMENT = None

    def to_dict(self):
        return {
            'ID_VOLUNTAR': self.ID_VOLUNTAR,
            'NUME': self.NUME,
            'PRENUME': self.PRENUME,
            'NR_TELEFON': self.NR_TELEFON,
            'DEPARTAMENT': self.DEPARTAMENT
        }

class Departament():
    def __init__(self):
        self.ID_DEPARTAMENT = None
        self.NUME = None
        self.ID_VOLUNTAR = None
        self.DIRECTOR = None

    def to_dict(self):
        return{
            'ID_DEPARTAMENT': self.ID_DEPARTAMENT,
            'NUME': self.NUME,
            'ID_VOLUNTAR': self.ID_VOLUNTAR,
            'DIRECTOR': self.DIRECTOR
        }

class Functie():
    def __init__(self):
        self.ID_FUNCTIE = None
        self.NUME = None
        self.DURATA = None
        self.ID_VOLUNTAR = None
        self.DATA = None


    def to_dict(self):
        return{
            'ID_FUNCTIE': self.ID_FUNCTIE,
            'NUME': self.NUME,
            'DURATA': self.DURATA,
            'ID_VOLUNTAR': self.ID_VOLUNTAR,
            'DATA': self.DATA
        }

class Proiect():
    def __init__(self):
        self.ID_PROIECT = None
        self.NUME = None
        self.DEPARTAMENT = None

    def to_dict(self):
        return {
            'ID_PROIECT': self.ID_PROIECT,
            'NUME': self.NUME,
            'DEPARTAMENT': self.DEPARTAMENT
        }

class Task():
    def __init__(self):
        self.ID_TASK = None
        self.ID_PROIECT = None
        self.DATA = None
        self.DURATA = None
        self.ORA = None
        self.DENUMIRE = None

    def to_dict(self):
        return {
            'ID_TASK': self.ID_TASK,
            'ID_PROIECT': self.ID_PROIECT,
            'DATA': self.DATA,
            'DURATA': self.DURATA,
            'ORA': self.ORA,
            'DENUMIRE': self.DENUMIRE
        }

class TaskVoluntar():
    def __init__(self):
        self.ID_ASOC = None
        self.ID_TASK = None
        self.ID_VOLUNTAR = None


    def to_dict(self):
        return{
            'ID_ASOC': self.ID_ASOC,
            'ID_TASK': self.ID_TASK,
            'ID_VOLUNTAR': self.ID_VOLUNTAR
        }

class Sponsor():
    def __init__(self):
        self.ID_SPONSOR = None
        self.SPONSOR = None
        self.SUMA = None

    def to_dict(self):
        return {
            'ID_SPONSOR': self.ID_SPONSOR,
            'SPONSOR': self.SPONSOR,
            'SUMA': self.SUMA
        }

class Sponsor_Proiect():
    def __init__(self):
        self.ID_SPONSOR_PROIECT = None
        self.ID_SPONSOR = None
        self.ID_PROIECT = None
        self.FINANTARE = None

    def to_dict(self):
        return {
            'ID_SPONSOR_PROIECT': self.ID_SPONSOR_PROIECT,
            'ID_SPONSOR': self.ID_SPONSOR,
            'ID_PROIECT': self.ID_PROIECT,
            'FINANTARE': self.FINANTARE
        }

class Locatie():
    def __init__(self):
        self.ID_LOCATIE = None
        self.JUDET = None
        self.ORAS = None
        self.STRADA = None
        self.DENUMIRE = None

    def to_dict(self):
        return {
            'ID_LOCATIE': self.ID_LOCATIE,
            'JUDET': self.JUDET,
            'ORAS': self.ORAS,
            'STRADA': self.STRADA,
            'DENUMIRE':self.DENUMIRE
        }


class Editie():
    def __init__(self):
        self.ID_EDITIE = None
        self.ID_PROIECT = None
        self.ID_LOCATIE = None
        self.PM_1 = None
        self.PM_2 = None

    def to_dict(self):
        return {
            'ID_EDITIE': self.ID_EDITIE,
            'ID_PROIECT': self.ID_PROIECT,
            'ID_LOCATIE': self.ID_LOCATIE,
            'PM_1': self.PM_1,
            'PM_2': self.PM_2
        }




@app.route('/voluntari_data')
def get_voluntari_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM VOLUNTARI ORDER BY ID_VOLUNTAR")
        voluntari_data = cursor.fetchall()
        connection.close()
        print(jsonify(voluntari_data))
    voluntari_reworked = []

    for i in voluntari_data:
        voluntar_instance = Voluntar()

        voluntar_instance.ID_VOLUNTAR = i[0]
        voluntar_instance.NUME = i[1]
        voluntar_instance.PRENUME = i[2]
        voluntar_instance.NR_TELEFON = i[3]
        voluntar_instance.DEPARTAMENT = i[4]

        voluntar_dict = voluntar_instance.to_dict()

        voluntari_reworked.append(voluntar_dict)

    return jsonify({'data': voluntari_reworked})

@app.route('/departamente_data')
def get_departamente_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM DEPARTAMENTE ORDER BY ID_DEPARTAMENT")
        departamente_data = cursor.fetchall()
        connection.close()
        print(jsonify(departamente_data))
    departamente_reworked = []

    for i in departamente_data:
        departament_instance = Departament()

        # Populate the attributes
        departament_instance.ID_DEPARTAMENT = i[0]
        departament_instance.NUME = i[1]
        departament_instance.ID_VOLUNTAR = i[2]
        departament_instance.DIRECTOR = i[3]

        departament_dict = departament_instance.to_dict()

        departamente_reworked.append(departament_dict)

    return jsonify({'data': departamente_reworked})

@app.route('/functii_data')
def get_functii_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM FUNCTII ORDER BY ID_FUNCTIE")
        functii_data = cursor.fetchall()
        connection.close()
        print(jsonify(functii_data))
    functii_reworked = []

    for i in functii_data:
        functie_instance = Functie()

        functie_instance.ID_FUNCTIE = i[0]
        functie_instance.NUME = i[1]
        functie_instance.DURATA = i[2]
        functie_instance.ID_VOLUNTAR = i[3]
        functie_instance.DATA = i[4]

        functie_dict = functie_instance.to_dict()

        functii_reworked.append(functie_dict)

    return jsonify({'data': functii_reworked})

@app.route('/proiecte_data')
def get_proiecte_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PROIECTE ORDER BY ID_PROIECT")
        proiecte_data = cursor.fetchall()
        connection.close()
        print(jsonify(proiecte_data))
    proiecte_reworked = []

    for i in proiecte_data:
        proiect_instance = Proiect()

        proiect_instance.ID_PROIECT = i[0]
        proiect_instance.NUME = i[1]
        proiect_instance.DEPARTAMENT = i[2]
        proiect_dict = proiect_instance.to_dict()

        proiecte_reworked.append(proiect_dict)

    return jsonify({'data': proiecte_reworked})

@app.route('/task_uri_data')
def get_task_uri_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM TASK_URI ORDER BY ID_TASK")
        task_uri_data = cursor.fetchall()
        connection.close()
        print(jsonify(task_uri_data))
    task_uri_reworked = []

    for i in task_uri_data:
        task_instance = Task()

        task_instance.ID_TASK = i[0]
        task_instance.ID_PROIECT = i[1]
        task_instance.DATA = i[2]
        task_instance.DURATA = i[3]
        task_instance.ORA = i[4]
        task_instance.DENUMIRE = i[5]

        task_dict = task_instance.to_dict()

        task_uri_reworked.append(task_dict)

    return jsonify({'data': task_uri_reworked})

@app.route('/task_voluntar_data')
def get_task_voluntar_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM TASK_VOLUNTAR ORDER BY ID_ASOC")
        task_voluntar_data = cursor.fetchall()
        connection.close()
        print(jsonify(task_voluntar_data))
    task_voluntar_reworked = []

    for i in task_voluntar_data:
        task_voluntar_instance = TaskVoluntar()

        task_voluntar_instance.ID_ASOC = i[0]
        task_voluntar_instance.ID_TASK = i[1]
        task_voluntar_instance.ID_VOLUNTAR = i[2]

        task_voluntar_dict = task_voluntar_instance.to_dict()

        task_voluntar_reworked.append(task_voluntar_dict)

    return jsonify({'data': task_voluntar_reworked})

@app.route('/sponsori_data')
def get_sponsori_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SPONSORI ORDER BY ID_SPONSOR")
        sponsori_data = cursor.fetchall()
        connection.close()
        print(jsonify(sponsori_data))
    sponsori_reworked = []

    for i in sponsori_data:
        sponsor_instance = Sponsor()

        sponsor_instance.ID_SPONSOR = i[0]
        sponsor_instance.SPONSOR = i[1]
        sponsor_instance.SUMA = i[2]


        sponsor_dict = sponsor_instance.to_dict()

        sponsori_reworked.append(sponsor_dict)

    return jsonify({'data': sponsori_reworked})

@app.route('/sponsor_proiect_data')
def get_sponsor_proiect_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SPONSOR_PROIECT ORDER BY ID_SPONSOR_PROIECT")
        sponsor_proiect_data = cursor.fetchall()
        connection.close()
        print(jsonify(sponsor_proiect_data))
    sponsor_proiect_reworked = []

    for i in sponsor_proiect_data:
        sponsor_proiect_instance = Sponsor_Proiect()

        sponsor_proiect_instance.ID_SPONSOR_PROIECT = i[0]
        sponsor_proiect_instance.ID_SPONSOR = i[1]
        sponsor_proiect_instance.ID_PROIECT = i[2]
        sponsor_proiect_instance.FINANTARE = i[3]


        sponsor_proiect_dict = sponsor_proiect_instance.to_dict()

        sponsor_proiect_reworked.append(sponsor_proiect_dict)

    return jsonify({'data': sponsor_proiect_reworked})

@app.route('/locatii_data')
def get_locatii_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM LOCATII ORDER BY ID_LOCATIE")
        locatii_data = cursor.fetchall()
        connection.close()
        print(jsonify(locatii_data))
    locatii_reworked = []

    for i in locatii_data:
        locatie_instance = Locatie()

        locatie_instance.ID_LOCATIE = i[0]
        locatie_instance.JUDET = i[1]
        locatie_instance.ORAS = i[2]
        locatie_instance.STRADA = i[3]
        locatie_instance.DENUMIRE = i[4]

        locatie_dict = locatie_instance.to_dict()

        locatii_reworked.append(locatie_dict)

    return jsonify({'data': locatii_reworked})

@app.route('/editii_data')
def get_editii_data():
    connection = connect_to_database()

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM EDITIE ORDER BY ID_EDITIE")
        editii_data = cursor.fetchall()
        connection.close()
        print(jsonify(editii_data))
    editie_reworked = []

    for i in editii_data:
        editie_instance = Editie()

        editie_instance.ID_EDITIE = i[0]
        editie_instance.ID_PROIECT = i[1]
        editie_instance.ID_LOCATIE = i[2]
        editie_instance.PM_1 = i[3]
        editie_instance.PM_2 = i[4]

        editie_dict = editie_instance.to_dict()

        editie_reworked.append(editie_dict)

    return jsonify({'data': editie_reworked})

#inserturi

@app.route('/add_editie', methods=['POST'])
def add_editie():
    id_editie = request.form.get('id_editie')
    id_proiect = request.form.get('id_proiect')
    id_locatie = request.form.get('id_locatie')
    pm_1 = request.form.get('pm_1')
    pm_2 = request.form.get('pm_2')


    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO EDITIE (ID_EDITIE, ID_PROIECT, ID_LOCATIE, PM_1, PM_2) "
                       "VALUES (:id_editie, :id_proiect, :id_locatie, :pm_1, :pm_2)",
                       id_editie=id_editie, id_proiect=id_proiect, id_locatie=id_locatie, pm_1=pm_1, pm_2=pm_2)
        connection.commit()
        connection.close()

    return redirect(url_for('list_editii'))

@app.route('/add_voluntar', methods=['POST'])
def add_voluntar():
    id_voluntar = request.form.get('id_voluntar')
    nume = request.form.get('nume')
    prenume = request.form.get('prenume')
    nr_telefon = request.form.get('nr_telefon')
    departament = request.form.get('departament')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO VOLUNTARI (ID_VOLUNTAR, NUME, PRENUME, NR_TELEFON, DEPARTAMENT) "
                       "VALUES (:id_voluntar, :nume, :prenume, :pm_1, :pm_2)",
                       id_voluntar=id_voluntar, nume=nume, prenume=prenume, nr_telefon=nr_telefon, departament=departament)
        connection.commit()
        connection.close()

    return redirect(url_for('list_voluntari'))

@app.route('/add_departament', methods=['POST'])
def add_departament():
    id_departament = request.form.get('id_departament')
    nume = request.form.get('nume')
    id_voluntar = request.form.get('id_voluntar')
    director = request.form.get('director')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO DEPARTAMENTE (ID_DEPARTAMENT, NUME, ID_VOLUNTAR, DIRECTOR) "
                       "VALUES (:id_departament, :nume, :id_voluntar, :director)",
                       id_departament=id_departament, nume=nume, id_voluntar=id_voluntar, director=director)
        connection.commit()
        connection.close()

    return redirect(url_for('list_departamente'))

@app.route('/add_functie', methods=['POST'])
def add_functie():
    id_functie = request.form.get('id_functie')
    nume = request.form.get('nume')
    durata = request.form.get('durata')
    id_voluntar = request.form.get('id_voluntar')
    data = request.form.get('data')


    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO FUNCTII (ID_FUNCTIE, NUME, DURATA, ID_VOLUNTAR, DATA) "
                       "VALUES (:id_functie, :nume, :durata, :id_voluntar, :data)",
                       id_functie=id_functie, nume=nume, durata=durata, id_voluntar=id_voluntar,  data=data)
        connection.commit()
        connection.close()

    return redirect(url_for('list_functii'))

@app.route('/add_proiect', methods=['POST'])
def add_proiect():
    id_proiect = request.form.get('id_proiect')
    nume = request.form.get('nume')
    departament = request.form.get('departament')


    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO PROIECTE (ID_PROIECT, NUME, DEPARTAMENT) "
                       "VALUES (:id_proiect, :nume, :departament)",
                       id_proiect=id_proiect, nume=nume, departament=departament)
        connection.commit()
        connection.close()

    return redirect(url_for('list_proiecte'))

@app.route('/add_task', methods=['POST'])
def add_task():
    id_task = request.form.get('id_task')
    id_proiect = request.form.get('id_proiect')
    data = request.form.get('data')
    durata = request.form.get('durata')
    ora = request.form.get('ora')
    denumire = request.form.get('denumire')



    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO TASK_URI (ID_TASK, ID_PROIECT, DATA, DURATA, ORA, DENUMIRE) "
                       "VALUES (:id_task, :id_proiect, :data, :durata, :ora, :denumire)",
                       id_task=id_task, id_proiect=id_proiect, data=data, durata=durata, ora=ora, denumire=denumire)
        connection.commit()
        connection.close()

    return redirect(url_for('list_task_uri'))

@app.route('/add_task_voluntar', methods=['POST'])
def add_task_voluntar():
    id_asoc = request.form.get('id_asoc')
    id_task = request.form.get('id_task')
    id_voluntar = request.form.get('id_voluntar')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO TASK_VOLUNTAR (ID_ASOC, ID_TASK, ID_VOLUNTAR) "
                       "VALUES (:id_asoc, :id_task, :id_voluntar)",
                       id_asoc=id_asoc, id_task=id_task, id_voluntar=id_voluntar)
        connection.commit()
        connection.close()

    return redirect(url_for('list_task_voluntar'))

@app.route('/add_sponsor', methods=['POST'])
def add_sponsor():
    id_sponsor = request.form.get('id_sponsor')
    sponsor = request.form.get('sponsor')
    suma = request.form.get('suma')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO SPONSORI (ID_SPONSOR, SPONSOR, SUMA) "
                       "VALUES (:id_sponsor, :sponsor, :suma)",
                       id_sponsor=id_sponsor, sponsor=sponsor, suma=suma)
        connection.commit()
        connection.close()

    return redirect(url_for('list_sponsori'))

@app.route('/add_sponsor_proiect', methods=['POST'])
def add_sponsor_proiect():
    id_sponsor_proiect = request.form.get('id_sponsor_proiect')
    id_sponsor = request.form.get('id_sponsor')
    id_proiect = request.form.get('id_proiect')
    finantare = request.form.get('finantare')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO SPONSOR_PROIECT (ID_SPONSOR_PROIECT, ID_SPONSOR, ID_PROIECT, FINANTARE) "
                       "VALUES (:id_sponsor_proiect, :id_sponsor, :id_proiect, :finantare)",
                       id_sponsor_proiect=id_sponsor_proiect, id_sponsor=id_sponsor, id_proiect=id_proiect, finantare=finantare)
        connection.commit()
        connection.close()

    return redirect(url_for('list_sponsor_proiect'))

@app.route('/add_locatie', methods=['POST'])
def add_locatie():
    id_locatie = request.form.get('id_locatie')
    judet = request.form.get('judet')
    oras = request.form.get('oras')
    strada = request.form.get('strada')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO LOCATII (ID_LOCATIE, JUDET, ORAS, STRADA) "
                       "VALUES (:id_locatie, :judet, :oras, :strada)",
                       id_locatie=id_locatie, judet=judet, oras=oras, strada=strada)
        connection.commit()
        connection.close()

    return redirect(url_for('list_locatii'))

#deleteeeeee

@app.route('/delete_editie', methods=['POST'])
def delete_editie():
    id_editie = request.form.get('id_editie')
    # Delete the data from the database
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM EDITIE WHERE ID_EDITIE = :id_editie", id_editie=id_editie)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_locatie', methods=['POST'])
def delete_locatie():
    id_locatie = request.form.get('id_locatie')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM LOCATII WHERE ID_LOCATIE = :id_locatie", id_locatie=id_locatie)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_voluntar', methods=['POST'])
def delete_voluntar():
    id_voluntar = request.form.get('id_voluntar')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM VOLUNTARI WHERE ID_VOLUNTAR = :id_voluntar", id_voluntar=id_voluntar)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_sponsor_proiect', methods=['POST'])
def delete_sponsor_proiect():
    id_sponsor_proiect = request.form.get('id_sponsor_proiect')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM SPONSOR_PROIECT WHERE ID_SPPONSOR_PROIECT = :id_sponsor_proiect", id_sponsor_proiect=id_sponsor_proiect)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_sponsor', methods=['POST'])
def delete_sponsor():
    id_sponsor = request.form.get('id_sponsor')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM SPONSORI WHERE ID_SPPONSOR = :id_sponsor", id_sponsor=id_sponsor)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_task_voluntar', methods=['POST'])
def delete_task_voluntar():
    id_asoc = request.form.get('id_asoc')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM TASK_VOLUNTAR WHERE ID_ASOC = :id_asoc", id_asoc=id_asoc)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_task_uri', methods=['POST'])
def delete_task_uri():
    id_task = request.form.get('id_task')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM TASK_URI WHERE ID_TASK = :id_task", id_task=id_task)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_proiect', methods=['POST'])
def delete_proiect():
    id_proiect = request.form.get('id_proiect')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM PROIECTE WHERE ID_PROIECT = :id_proiect", id_proiect=id_proiect)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_functie', methods=['POST'])
def delete_functie():
    id_functie = request.form.get('id_functie')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM FUNCTII WHERE ID_FUNCTIE = :id_functie", id_functie=id_functie)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

@app.route('/delete_departament', methods=['POST'])
def delete_departament():
    id_departament = request.form.get('id_departament')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM DEPARTAMENTE WHERE ID_DEPARATAMENT = :id_departament", id_departament=id_departament)
        connection.commit()
        connection.close()

    return jsonify({'message': 'Success'})

#cerere c

@app.route('/cerere')
def rezultat():
    conn = connect_to_database()

    cursor = conn.cursor()
    query = """
    SELECT V.ID_VOLUNTAR, TV.ID_TASK, T.ID_PROIECT
    FROM VOLUNTARI V
    JOIN TASK_VOLUNTAR TV ON TV.ID_VOLUNTAR = V.ID_VOLUNTAR
    JOIN TASK_URI T ON T.ID_TASK = TV.ID_TASK
    WHERE V.ID_VOLUNTAR > 12 AND T.ID_PROIECT > 3
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('cerere.html', results=results)

#cerere cu having
@app.route('/cerere2')
def rezultat2():
    conn = connect_to_database()
    cursor = conn.cursor()
    query = """
    SELECT
    V.ID_VOLUNTAR,
    V.NUME,
    COUNT(TV.ID_ASOC)AS NUMAR_TASK_URI
    FROM VOLUNTARI V
    JOIN TASK_VOLUNTAR TV ON V.ID_VOLUNTAR = TV.ID_VOLUNTAR
    GROUP BY V.ID_VOLUNTAR, V.NUME
    HAVING COUNT(TV.ID_ASOC) >1
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('cerere2.html', results=results)




if __name__ == '__main__':
    app.run(debug=True)

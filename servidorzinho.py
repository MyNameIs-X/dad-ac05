from flask import Flask, jsonify, request

app = Flask(__name__)

database = {}
database['teacher'] = []
database['student'] = []

@app.route('/')
def all():
    return jsonify(database)

@app.route('/alunos')
def get_all_student():
    return jsonify(database['student'])

@app.route('/alunos', methods=["POST"])
def store_student():
    if not 'nome' in request.json.keys():
        return jsonify({ 'erro':'aluno sem nome' }), 400

    new_student = request.json
    for student in database['student']:
        if student['id'] == new_student['id']:
            return jsonify({ 'erro':'id ja utilizada' }), 400
    
    database['student'].append(new_student)
    return { 'success': True }, 200

@app.route('/alunos/<int:id_student>')
def get_single_stundent(id_student):
    for student in database['student']:
        if student['id'] == id_student:
            return jsonify(student)

    return jsonify({ 'erro': 'aluno nao encontrado' }), 400

@app.route('/alunos/<int:id_student>', methods=["DELETE"])
def del_student(id_student):
    for student in database['student']:
        if student['id'] == id_student:
            database['student'].remove(student)
            return jsonify({ 'success': True }), 200

    return jsonify({ 'erro': 'aluno nao encontrado' }), 400

@app.route('/alunos/<int:id_student>', methods=["PUT"])
def change_student(id_student):
    if 'nome' not in request.json.keys():
        return jsonify({ 'erro':'aluno sem nome' }), 400

    for student in database['student']:
        if student['id'] == id_student:
            student['nome'] = request.json['nome']
            return jsonify({ 'success': True }), 200

    return jsonify({ 'erro': 'aluno nao encontrado' }), 400

@app.route('/professores')
def get_all_teachers():
    return jsonify(database['teacher'])

@app.route('/professores', methods=["POST"])
def store_teacher():
    new_teacher = request.json
    if not 'nome' in new_teacher.keys():
        return jsonify({ 'erro': 'professor sem nome' }), 400

    for teacher in database['teacher']:
        if teacher['id'] == new_teacher['id']:
            return jsonify({ 'erro': 'id ja utilizada' }), 400

    database['teacher'].append(new_teacher)
    return jsonify({ 'success': True }), 200

@app.route('/professores/<int:id_teacher>')
def get_single_teacher(id_teacher):
    for teacher in database['teacher']:
        if teacher['id'] == id_teacher:
            return teacher

    return jsonify({ 'erro': 'professor nao encontrado' }), 400

@app.route('/professores/<int:id_teacher>', methods=["DELETE"])
def del_teacher(id_teacher):
    for teacher in database['teacher']:
        if teacher['id'] == id_teacher:
            database['teacher'].remove(teacher)
            return jsonify({ 'success': True })

    return jsonify({ 'erro': 'professor nao encontrado' }), 400

@app.route('/professores/<int:id_teacher>', methods=["PUT"])
def change_teacher(id_teacher):
    if not 'nome' in request.json.keys():
        return jsonify({ 'erro': 'professor sem nome' }), 400

    for teacher in database['teacher']:
        if teacher['id'] == id_teacher:
            teacher['nome'] = request.json['nome']
            return jsonify({ 'success': True })

    return jsonify({ 'erro': 'professor nao encontrado' }), 400

@app.route('/reseta', methods=["POST"])
def reset():
    database['student'] = []
    database['teacher'] = []

    return { 'success': True }, 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)

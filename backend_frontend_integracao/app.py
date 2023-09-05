from flask import Flask, request, render_template
from sqlalchemy.orm import Session
from models import engine, Base, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
Base.metadata.create_all(engine)


@app.route('/cadastrousuarios', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name: str = request.form.get('name')
        lastname: str = request.form.get('lastnbame')
        email: str = request.form.get('email')
        password: str = request.form.get('password')

        hashed: str = generate_password_hash(password, method='scrypt')

        with Session(engine) as session:
            user: User = User(name=name, lastname=lastname,
                              email=email, password=hashed)

            session.add(user)
            session.commit()

        return render_template('cadastro.html')

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('')


if __name__ == '__main__':
    app.run(debug=True)

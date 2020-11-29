from flask import Flask, render_template

# from controllers.member_controller import members_blueprint
# from controllers.fitness_class_controller import fitness_classes_blueprint
# from controllers.class_type_controller import class_types_blueprint
# from controllers.bookings_controller import bookings_blueprint

app = Flask(__name__)

# app.register_blueprint(members_blueprint)
# app.register_blueprint(fitness_classes_blueprint)
# app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
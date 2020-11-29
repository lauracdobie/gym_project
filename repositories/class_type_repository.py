from db.run_sql import run_sql
from models.class_type import ClassType
import pdb

#delete all
def delete_all():
    sql = "DELETE  FROM class_types"
    run_sql(sql)


#delete selected
def delete(id):
    sql = "DELETE  FROM class_types WHERE id = %s"
    value = [id]
    run_sql(sql, value)

#add
def add(class_type):
    sql = "INSERT INTO class_types(name, description, intensity, difficulty) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [class_type.name, class_type.description, class_type.intensity, class_type.difficulty]
    result = run_sql(sql, values)
    id = result[0]['id']
    class_type.id = id

#edit
def edit(class_type):
    sql = "UPDATE class_types SET (name, description, intensity, difficulty) = (%s, %s, %s, %s) WHERE id = %s"
    values = [class_type.name, class_type.description, class_type.intensity, class_type.difficulty, class_type.id]
    result = run_sql(sql, values)

#select all
def select_all():
    all_class_types = []
    sql = "SELECT * FROM class_types"
    results = run_sql(sql)

    for row in results:
        class_type = ClassType(row['name'], row['description'], row['intensity'], row['difficulty'], row['id'])
        all_class_types.append(class_type)
    
    return all_class_types

#select
def select(id):
    class_type = None
    sql = "SELECT * from class_types WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        class_type = ClassType(result['name'], result['description'], result['intensity'], result['difficulty'], result['id'])
    return class_type
from db.run_sql import run_sql
from models.member import Member
import pdb

#delete all
def delete_all():
    #Write a sql query to delete everything from the members table and save it as variable called sql
    sql = "DELETE  FROM members"
    #Run the run_sql function, passing in the sql variable as an argument
    run_sql(sql)


#delete selected
def delete_selected(id):
    sql = "DELETE  FROM members WHERE id = %s"
    value = [id]
    run_sql(sql, value)

#add
def add(member):
    sql = "INSERT INTO members(name, address, phone, email, premium, membership_no) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.name, member.address, member.phone, member.email, member.premium, member.membership_no]
    result = run_sql(sql, values)
    id = result[0]['id']
    member.id = id

#edit
def edit(member):
    sql = "UPDATE members SET (name, address, phone, email, premium, membership_no) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.name, member.address, member.phone, member.email, member.premium, member.membership_no, member.id]
    result = run_sql(sql, values)

#select all
def select_all():
    all_members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['address'], row['phone'], row['email'], row['premium'], row['membership_no'], row['id'])
        all_members.append(member)
    
    return all_members

#select
def select(id):
    member = None
    sql = "SELECT * from members WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        member = Member(result['name'], result['address'], result['phone'], result['email'], result['premium'], result['membership_no'], result['id'])
    return member


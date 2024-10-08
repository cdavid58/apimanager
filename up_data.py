import sqlite3, pymysql.cursors

db = "p9$Xv4#Tn7@q.sqlite3"
con = sqlite3.connect(db)
c = con.cursor()
tables = ["setting_municipalities", "setting_payment_form", "setting_payment_method", "setting_payroll_type_document_identification", "setting_sub_type_worker", "setting_type_contract", 
	"setting_type_document", "setting_type_document_i", "setting_type_organization", "setting_type_regimen", 
	"setting_type_worker", "setting_unit_measures"]

list_table = [
'municipalities', 'payment_forms', 'payment_methods', 'payroll_type_document_identifications', 'sub_type_workers', 'type_contracts', 'type_documents', 'type_document_identifications',
'type_organizations','type_regimes','type_workers','unit_measures'
]

count = 0
for i in tables:
	MyDB = pymysql.connect(
	    host="159.203.170.123",
	    port=3306,
	    user="root",
	    passwd="medellin100",
	    db="apidian",
	    charset='utf8',
	    cursorclass=pymysql.cursors.DictCursor
	)
	cursor = MyDB.cursor()
	query = (f"SELECT id, name from {list_table[count]}")
	cursor.execute(query)
	data = cursor.fetchall()
	for j in data:
		c.execute(f"insert into {i}(_id, name)values({j['id']},'{j['name']}')")
		con.commit()
	count += 1


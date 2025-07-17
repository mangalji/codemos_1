#standard library(module)
import mysql.connector 

#third party library
from faker import Faker
import random

FAKE_DATA = Faker('en_IN')

# FAKE_DATA generates the fake data in our database tables for checking tables work properly or not

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "RajMangal",
        passwd = "raj12345",
        database ="pet_adoption_system_database"
        )
    mycursor = mydb.cursor() #here we connect with our DBMS

except Exception as e:
    print("The error in your program is: ",e)

'''mycursor.execute("CREATE DATABASE pet_adoption_system_database")  #here we create our database
print("Database created successfully")       

mycursor.execute("SHOW DATABASES")  #here we show our all databases present in our DBMS
for x in mycursor:
    print(x)  
'''

'''
mycursor.execute("CREATE TABLE user_table(user_id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255), phone VARCHAR(255), email varchar(255), password varchar(255),address VARCHAR(255),city varchar(100),created_at DATETIME(6),last_login DATETIME(6))")    
mycursor.execute("CREATE TABLE pet_table(pet_id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255), category varchar(255), breed varchar(255), age varchar(3), weight varchar(5), medical_history varchar(255),added_at DATETIME(6))")
mycursor.execute("CREATE TABLE call_request_table(request_id INT AUTO_INCREMENT PRIMARY KEY, pet_id int,user_id int,status varchar(255), FOREIGN KEY(pet_id)references pet_table(pet_id), foreign key(user_id) references user_table(user_id))")
mycursor.execute("CREATE TABLE transaction_table(tr_id INT AUTO_INCREMENT PRIMARY KEY,request_id int, foreign key(request_id)references call_request_table(request_id), pet_id int, FOREIGN KEY(pet_id)references pet_table(pet_id),user_id int,foreign key(user_id) references user_table(user_id),status varchar(255))")
print("successfully created tables")
'''

mycursor.execute("SELECT DATABASE()") #this command is showing which database is running

for database in mycursor:
    print(database)
print("------------------------------")

mycursor.execute("SHOW TABLES")     #this command showing tables in database                                           

for row in mycursor:
    print(row)
print("------------------------------")

breeds = {
    'Dog': ['Labrador', 'Pug', 'German Shepherd', 'Beagle'],
    'Cat': ['Persian', 'Siamese', 'Maine Coon'],
    'Rabbit': ['Dutch', 'Mini Rex', 'Lionhead'],
    'Cow': ['Sahiwal', 'Red Sindhi', 'Gir', 'Tharparkar', 'Kankrej'],
    'Buffalo': ['Anatolian buffalo','Australian buffalo',
    'Azi Kheli','Azari','Badavan','Murrah']
}
#this dictionary is for fetching pet's breed


pet_names = {
    'Dog': ["Sheru","Rani","Moti","Tommy","Chiku","Raja",
    "Golu","Simba","Bholu","Sonu","Kalu","Sweety","Mithu",
    "Guddu","Champ","Sultan","Bablu","Laila","Pinky","Babloo"],

    'Cat': [ "Simmi","Munni","Tinku","Chintu","Gudiya","Raja"
    "Sheru","Sweety","Chiku","Kittu","Billi","Moti","Sonu",                
    "Mishri","Pinky","Laila","Guddi","Sona","Bholi","Tofu"],

    'Rabbit': ["Golu","Chini","Mithu","Snowy","Tofu","Ladoo",
    "Puchi","Bunny","Chhotu","Lassi","Guddu","Kaju","Rasgulla",
    "Babloo","Sweety","Dolu","Nikki","Tuffy","Simmi","Bhalu"],

    'Cow': [ "Gauri","Kamdhenu","Lakshmi","Radha","Sita",
    "Surabhi","Nandini","Ganga","Parvati","Rani","Dhenu","Shyama",
    "Gomti","Lali","Basanti","Munni","Gaura","Bhuri","Champa","Babli"], 

    'Buffalo': ["Kali","Munni","Rani","Ganga","Lali","Bhuri","Gaura",
    "Basanti","Chameli","Gomti","Sundari","Shyama","Dhanno","Billo",
    "Lakshmi","Toofan","Rambha","Bijli","Nandini","Chandni"]
}
#this is pet's name dictionary


def deleting_data_from_table():         #this func will deleted all data from tables
    
    try:
        mycursor.execute("DELETE FROM transaction_table")  #this is the query for removing every data 
        mycursor.execute("DELETE FROM call_request_table")
        mycursor.execute("DELETE FROM user_table")
        mycursor.execute("DELETE FROM pet_table")
        
        mydb.commit()                                      #this command execute changes into database     
        print("Table's data deleted successfully")

    except Exception as e:
        print("error in deleting data is: ",e)


def adding_data_into_table():   #here we are feeding data to the tables
    
    entries = int(input("How many entries you want to enter in the tables: "))
    #this 'entries' store the total no. of entries we want to feed in database

    try:
        my_user_table_func(entries)
        my_pet_table_func(entries)
        my_callrequests_table_func(entries)
        my_transactions_table_func(entries)
        
        mydb.commit() 
        print("Entries inserted successfully")

    except Exception as e:
        print("error in adding data is: ",e)


def get_existing_ids(table_name, column_name):      

    query = f"SELECT {column_name} FROM {table_name}"   #this query select the data from the table 
    mycursor.execute(query)
    results = mycursor.fetchall()
    return [row[0] for row in results]

'''this function gave us the primary keys of user_table and pet_table so we use them as a foreign 
key in call_request_table and trasaction_table'''

def my_user_table_func(entries):

    insert_data = '''INSERT INTO user_table(      #this is the query for inserting data into table
        name,phone,email,password,
        address,city,created_at,last_login) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''

    records = []
    
    for _ in range(1,entries+1):  

        name = FAKE_DATA.name()                         
        phone = FAKE_DATA.phone_number()                 
        email = FAKE_DATA.email()                       
        password = FAKE_DATA.password()                 
        address = FAKE_DATA.address()
        city = FAKE_DATA.city()
        created_at = FAKE_DATA.date_between(start_date='-1y',end_date='now')             
        last_login = FAKE_DATA.date_between(start_date=created_at,end_date='now')
        record = (name,phone,email,password,address,city,created_at,last_login)
        records.append(record)

    mycursor.execute("ALTER TABLE user_table AUTO_INCREMENT = 1;")
    mycursor.executemany(insert_data,records)
    print(records)
    print("User data feeded successfully")
#this function store the data of user's is our user_table 

'''date random generated lene ke liye humein FAKE_DATA.date_time_between
(start_date='',end_date='') ka use hoga'''


def my_pet_table_func(entries):

    insert_data = '''INSERT INTO pet_table(
        name,category,breed,age,
        weight,medical_history,added_at) 
        VALUES(%s,%s,%s,%s,%s,%s,%s)'''

    records = []
    
    for i in range(1,entries+1):

        category = FAKE_DATA.random_element(['Dog', 'Cat', 'Rabbit', 'Cow','Buffalo'])  
        name = random.choice(pet_names[category])         
        breed = random.choice(breeds[category]) 
        age = FAKE_DATA.random_int(min=0,max=20)        
        weight = FAKE_DATA.random_int(min=20,max=2000)  
        medical_history = FAKE_DATA.text()              
        added_at = FAKE_DATA.date_between(start_date='-1y',end_date='now')
        record = (name,category,breed,age,weight,medical_history,added_at)
        records.append(record)

    mycursor.execute("ALTER TABLE pet_table AUTO_INCREMENT = 1;")
    mycursor.executemany(insert_data,records)
    print(records)
    print("Pet data feeded successfully")
    #this function stores the pet's data in pet_table 


def my_callrequests_table_func(entries):

    insert_data = '''INSERT INTO call_request_table(
        pet_id,user_id,status) 
        VALUES(%s,%s,%s)'''

    records = []

    user_ids = get_existing_ids("user_table", "user_id")    

    #this line stores the user's id and use these ids in call_request_table as a foreign key

    pet_ids = get_existing_ids("pet_table", "pet_id")

    #this line stores the pet's id and use these ids in call_request_table as a foreign key

    for i in range(1,entries+1):        

        pet_id = FAKE_DATA.random.choice(pet_ids)            
        user_id = FAKE_DATA.random.choice(user_ids)           
        status = FAKE_DATA.random_element(['Accepted','Pending','Rejected'])     
        record = (pet_id,user_id,status)
        records.append(record)

    mycursor.execute("ALTER TABLE call_request_table AUTO_INCREMENT = 1;")
    mycursor.executemany(insert_data,records)
    print(records)
    print("Call request table filled successfully")
'''this function fetch the call request from the webpage and fetch the user's_id 
and pet_id and stored in the table'''


def my_transactions_table_func(entries):
    insert_data = '''INSERT INTO transaction_table(
        request_id,pet_id,user_id,status) 
        VALUES(%s,%s,%s,%s)'''

    records = []

    user_ids = get_existing_ids("user_table", "user_id")
    pet_ids = get_existing_ids("pet_table", "pet_id")
    request_ids = get_existing_ids("call_request_table","request_id")

    for i in range(1,entries+1):

        pet_id = FAKE_DATA.random.choice(pet_ids)                
        user_id = FAKE_DATA.random.choice(user_ids)
        request_id = FAKE_DATA.random.choice(request_ids)        
        status = FAKE_DATA.random_element(['listed','got'])         
        record = (request_id,pet_id,user_id,status)
        records.append(record)

    mycursor.execute("ALTER TABLE transaction_table AUTO_INCREMENT = 1;")
    mycursor.executemany(insert_data,records)   
    print(records)
    print("Transaction table filled successfully")

'''this is the transaction table where we see the transaction on the website 
like listing of pet's or complete transaction of adoption and donation of pet's
'''


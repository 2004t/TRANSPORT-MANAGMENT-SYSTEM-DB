import random as rand
from datetime import datetime, timedelta, time

import pyodbc
from faker import Faker

# Initialize Faker
fake = Faker()

# Database connection
connection = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-QUTS9KN;'
    'DATABASE=project;'
    'Trusted_Connection=yes;'
)
cursor = connection.cursor()


#INSERTION IN DRIVER TABLE:
# Insert data into the driver table
# pakistan_names = [
#     'Ali', 'Hareem', 'Ahmed', 'Fatima', 'Muhammad', 'Zainab', 'Usman', 'Tabish',
#     'Hamza', 'Laiba', 'Umair', 'Manahil', 'Hassan', 'Talha', 'Khan'
# ]
# def generate_pakistani_phone_number():
#     return '03' + str(rand.randint(100000000, 999999999))  # Generate a random Pakistani phone number
# generated_names = set()
# used_driver_ids = set()
# while len(generated_names) < 15:  # Insert 15 records
#     driver_id = generate_unique_driver_id(used_driver_ids)
#     driver_name = rand.choice(pakistan_names)
#     phone_no = generate_pakistani_phone_number()
#     if driver_name not in generated_names:
#         cursor.execute("INSERT INTO driver (driver_id, driver_name, phone_no) VALUES (?, ?, ?)",
#                        (driver_id, driver_name, phone_no))
#         generated_names.add(driver_name)
#         print(f"Inserted record: {driver_id}, {driver_name}, {phone_no}")



#INSERTION IN BUS TABLE:
# def get_existing_driver_ids():
#     cursor.execute("SELECT driver_id FROM driver")
#     return [row.driver_id for row in cursor.fetchall()]
# # Retrieve existing driver IDs
# existing_driver_ids = get_existing_driver_ids()
# # List of Pakistani company names
# pakistani_companies = ['Toyota', 'Honda', 'Suzuki', 'KIA', 'Hyundai', 'United']
# # List of model years from 2010 to 2024
# model_years = [str(year) for year in range(2010, 2024)]
# # Insert new data into the bus table
# for _ in range(15):
#     # Generate random data for the bus table
#     bus_id = fake.random_number(digits=3)
#     driver_id = rand.choice(existing_driver_ids)
#     company_name = rand.choice(pakistani_companies)
#     model = rand.choice(model_years)
#     license_plate = fake.license_plate()
#
#     # Insert data into the bus table
#     cursor.execute("INSERT INTO bus (bus_id, driver_id, company_name, license_plate, model) VALUES (?, ?, ?, ?, ?)",
#                    (bus_id, driver_id, company_name, license_plate, model))




#INSERTION INTO ROUTESS TABLE:
# def generate_unique_route_id(used_ids):
#     while True:
#         route_id = fake.random_number(digits=2, fix_len=True)
#         if route_id not in used_ids:
#             used_ids.add(route_id)
#             return route_id
#
# # Retrieve existing route IDs
# def get_existing_route_ids():
#     cursor.execute("SELECT route_id FROM routess")
#     return [row.route_id for row in cursor.fetchall()]
#
# existing_route_ids = set(get_existing_route_ids())
#
# # Insert new data into the routess table
# for i in range(1, 16):
#     # Generate random data for the routess table
#     route_id = generate_unique_route_id(existing_route_ids)
#     route_name = f"Route {i}"
#     fee_pkr = rand.randint(5000, 10000)
#
#     # Retrieve a random bus ID from the original bus table
#     cursor.execute("SELECT TOP 1 bus_id FROM bus ORDER BY NEWID()")
#     bus_id = cursor.fetchone().bus_id
#
#     # Insert data into the routess table
#     cursor.execute("INSERT INTO routess (route_id, route_name, fee, bus_id) VALUES (?, ?, ?, ?)",
#                    (route_id, route_name, fee_pkr, bus_id))



#insertion into routestops table
# route_stops = {
#     75: [
#         (101, 'Muredky'), (102, 'Rana Town'), (103, 'Shahdra Round About'), (104, 'Ahmad Travel'),
#         (105, 'Sanda'), (106, 'Shera Kot'), (107, 'Motorway Babu Sabu'), (108, 'Thokar Niaz Baig'),
#         (109, 'EME Canal Road'), (110, 'Jubilee Town')
#     ],
#     83: [
#         (201, 'Batii Chowk'), (202, 'Yadgaar'), (203, 'Bhatti'), (204, 'MAO College'), (205, 'Chuburji'),
#         (206, 'Samanabad Mor'), (207, 'Chowk Yattem Khana'), (208, 'Scheme Mor'), (209, 'Multan Chungi'),
#         (210, 'Thokar Niaz Baig'), (211, 'Raiwind Road'), (212, 'Qazlabash Chowk'), (213, 'Manoo Chowk'),
#
#     ],
#     88: [
#         (301, 'Shahdra Round About'), (302, 'Band Road'), (303, 'Sanda'), (304, 'Babu Sabu'),
#         (305, 'Qazlabash Chowk'), (306, 'Rehman CNG'), (307, 'Manoo Chowk')
#
#
#     ],
#     42: [
#         (401, 'Gulshan Ravi'), (402, 'Samanabad Mor'), (403, 'Chowk Yattem Khana'), (404, 'Scheme Mor'),
#         (405, 'Moon Market'), (406, 'Bekhywal Mor'), (407, 'Multan Chungi'), (408, 'Thokar Niaz Baig'),
#         (409, 'Canal Road'), (410, 'Muhafiz Town'), (411, 'Jubilee Town'), (412, 'Shakam Chowk'),
#
#     ],
#     13: [
#         (501, 'Railway Station'), (502, 'Shimla Hill'), (503, 'Assembly Hall'), (504, 'Ganga Ram Hospital'),
#         (505, 'Mozang Chungi'), (506, 'Ichhra'), (507, 'Muslim Town Mor'), (508, 'Bekhywal Mor'),
#         (509, 'Campus Bridge'), (510, 'Jinnah Hospital'), (511, 'Allah Hoo Chowk'), (512, 'Shadewal Chowk'),
#
#     ],
#     12: [
#         (601, 'New Bridge'), (602, 'Harbans Pura'), (603, 'Darogha Wala'), (604, 'Pakistan Mint'),
#         (605, 'Shalimar Garden'), (606, 'UET'), (607, 'Garhi Shaho'), (608, 'Dharam Pura'),
#         (609, 'Campus Bridge'), (610, 'Nursery Stop')
#
#     ],
#     17: [
#         (701, 'Askari 10'), (702, 'Joray Pull'), (703, 'Sadar Cantt'), (704, 'Tufail Road'),
#         (705, 'R.A. Bazar'), (706, 'Cavalary Ground'), (707, 'Firdous Market'), (708, 'Kalma Chowk'),
#         (709, 'Faisal Town Round About'), (710, 'Jinnah Hospital')
#
#     ],
#     70: [
#         (801, 'R.A. Bazar'), (802, 'Cavalary Ground'), (803, 'Firdous Market'), (804, 'Kalma Chowk'),
#         (805, 'Barkat Market'), (806, 'Faisal Town Round About'), (807, 'Central Flats'), (808, 'Akbar Chowk'),
#         (809, 'College Road'), (810, 'Ghazi Chowk'), (811, 'Wapda Town Round About')
#
#     ],
#     11: [
#         (901, 'Nishtar Colony'), (902, 'Ghazi Road'), (903, 'Qainchi Phatak'), (904, 'Kot Lakhpat Station'),
#         (905, 'Pindi Stop'), (906, 'Hamdard Chowk'), (907, 'Bagriaan Chowk'), (908, 'Wapda Town Round About')
#
#     ],
#     49: [
#         (1001, 'Ghazi Road'), (1002, 'Qainchi Phatak'), (1003, 'Kot Lakhpat Station'), (1004, 'Pindi Stop'),
#         (1005, 'Hamdard Chowk'), (1006, 'Bagriaan Chowk'), (1007, 'Wapda Town Round About'), (1008, 'Nash-e-Man Iqbal'),
#
#     ],
#     62: [
#         (1101, 'Masjid Chowk Defence'), (1102, 'Defence Mor'), (1103, 'Walton Road'), (1104, 'Qainchi'),
#         (1105, 'Kot Lakhpat Station'), (1106, 'Peeco Road'), (1107, 'Hamdard Chowk'), (1108, 'Bagriaan Chowk'),
#         (1109, 'Ghazi Chowk')
#       ],
# 86: [
#         (1201, 'Saddique Trade Centre'), (1202, 'Main Market Gulberg'), (1203, 'Kalma Chowk'),
#         (1204, 'Ittefaq Hospital'), (1205, 'Model Town Link Road'), (1206, 'Al Karim Chowk'),
#         (1207, 'Chandani Chowk'), (1208, 'Ghazi Chowk'), (1209, 'Wapda Town Round About')],
#     67: [
#         (1301, 'Muredky'), (1302, 'Rana Town'), (1303, 'Shahdra Round About'), (1304, 'Ahmad Travel'),
#         (1305, 'Sanda'), (1306, 'Shera Kot'), (1307, 'Motorway Babu Sabu'), (1308, 'Thokar Niaz Baig'),
#         (1309, 'EME Canal Road'), (1310, 'Jubilee Town'), (1311, 'New Bridge'), (1312, 'Harbans Pura'),
#         (1313, 'Darogha Wala'), (1314, 'Pakistan Mint'), (1315, 'Shalimar Garden')
#     ],
#     52: [
#         (1401, 'R.A. Bazar'), (1402, 'Cavalary Ground'), (1403, 'Firdous Market'), (1404, 'Kalma Chowk'),
#         (1405, 'Barkat Market'), (1406, 'Faisal Town Round About'), (1407, 'Central Flats'), (1408, 'Akbar Chowk'),
#         (1409, 'College Road'), (1410, 'Ghazi Chowk'), (1411, 'Wapda Town Round About'), (1412, 'Gulshan Ravi'),
#         (1413, 'Samanabad Mor'), (1414, 'Chowk Yattem Khana'), (1415, 'Scheme Mor')
#     ],
# 87: [
#         (1501, 'Askari 10'), (1502, 'Joray Pull'), (1503, 'Sadar Cantt'), (1504, 'Tufail Road'),
#         (1505, 'R.A. Bazar'), (1506, 'Cavalary Ground'), (1507, 'Firdous Market'), (1508, 'Kalma Chowk'),
#         (1509, 'Faisal Town Round About'), (1510, 'Jinnah Hospital'), (1511, 'Saddique Trade Centre'),
#         (1512, 'Main Market Gulberg'), (1513, 'Kalma Chowk'), (1514, 'Ittefaq Hospital'), (1515, 'Model Town Link Road')],
#     # Add stops for other routes here
# }
# # Insert data into the routestops table for each route
# for route_id, stops in route_stops.items():
#     for routestop_id, stop_name in stops:
#          cursor.execute("INSERT INTO routestops (route_id, routestop_id, stop_name) VALUES (?, ?, ?)",
#             (route_id, routestop_id, stop_name))





#INSERTION INTO STUDENTS TABLE:
# num_students = 495
# def generate_student_ids(num_students):
#     return rand.sample(range(1, 500), num_students)
#
# # Sample Pakistani names
# pakistani_names = [
#     'Aamir', 'Aamna', 'Aarif', 'Aasia', 'Aatif', 'Aayat', 'Abbas', 'Abida', 'Abdullah', 'Abia',
#     'Abdul', 'Abira', 'Abid', 'Afia', 'Abu', 'Afshan', 'Adam', 'Afsheen', 'Adil', 'Afsar',
#     'Afaq', 'Afsheena', 'Aftab', 'Afroz', 'Ahmad', 'Afsheen', 'Ahmed', 'Afshan', 'Ajmal', 'Afsheen',
#     'Akbar', 'Aisha', 'Akhtar', 'Alia', 'Akram', 'Alina', 'Akhtar', 'Aliza', 'Akram', 'Almas',
#     'Alam', 'Amara', 'Ali', 'Amber', 'Altaf', 'Amina', 'Amir', 'Amna', 'Amjad', 'Anam',
#     'Anwar', 'Aneesa', 'Arif', 'Anila', 'Arij', 'Anisa', 'Arif', 'Anjum', 'Arshad', 'Aqsa',
#     'Asad', 'Aruba', 'Asghar', 'Asma', 'Ashfaq', 'Asrar', 'Asif', 'Atia', 'Asim', 'Atiya',
#     'Aslam', 'Ayesha', 'Asmat', 'Aziza', 'Asrar', 'Azra', 'Asif', 'Bano', 'Atif', 'Bilquis',
#     'Azam', 'Bushra', 'Azhar', 'Faiza', 'Aziz', 'Farah', 'Babar', 'Farida', 'Baqar', 'Farwa',
#     'Fareed', 'Fauzia', 'Farid', 'Fiza', 'Faisal', 'Ghazala', 'Faiz', 'Gul', 'Faizan', 'Gulzar',
#     'Farhan', 'Habiba', 'Faroq', 'Haleema', 'Farrukh', 'Hamida', 'Fasih', 'Hamna', 'Fateh', 'Hasina',
#     'Fayyaz', 'Hina', 'Fazal', 'Hira', 'Feroz', 'Huma', 'Furqan', 'Iqra', 'Ghulam', 'Jamila',
#     'Habib', 'Kalsoom', 'Habibullah', 'Kanwal', 'Haider', 'Kausar', 'Hakim', 'Khadija', 'Hameed', 'Kiran',
#     'Hamid', 'Maham', 'Hamza', 'Mahira', 'Haneef', 'Maheen', 'Haroon', 'Mahnoor', 'Hasan', 'Maimoona',
#     'Hashim', 'Maira', 'Hassan', 'Majida', 'Hidayat', 'Maliha', 'Ibrahim', 'Mamoona', 'Iftikhar', 'Maria',
#     'Ikram', 'Marium', 'Ilyas', 'Maryam', 'Imran', 'Mehwish', 'Inayat', 'Misbah', 'Irfan', 'Mubashir',
#     'Irshad', 'Mudassir', 'Ishtiaq', 'Mumtaz', 'Ishtiaque', 'Munawar', 'Israr', 'Muneeb', 'Jalal', 'Muneer',
#     'Jameel', 'Musarrat', 'Jamshed', 'Musharraf', 'Javed', 'Nadia', 'Jawad', 'Naeem', 'Jawaid', 'Naheed',
#     'Junaid', 'Naila', 'Kabeer', 'Najma', 'Kaleem', 'Nargis', 'Kamal', 'Nazia', 'Kamran', 'Nighat',
#     'Karamat', 'Noreen', 'Kareem', 'Nosheen', 'Kashif', 'Parveen', 'Kausar', 'Qudsia', 'Khaleel', 'Quratulain',
#     'Khalid', 'Raheela', 'Khalil', 'Rahila', 'Khawar', 'Rahima', 'Khurram', 'Raziya', 'Maqbool', 'Riffat',
#     'Maqsood', 'Rubina', 'Maroof', 'Saba', 'Masood', 'Sabah', 'Mazhar', 'Sabiha', 'Mehboob', 'Sadaf',
#     'Mehdi', 'Sadia', 'Mehmood', 'Sadika', 'Mehmood', 'Saeeda', 'Mohammad', 'Safia', 'Mohammed', 'Saima',
#     'Mohsin', 'Saira', 'Moiz', 'Sajida', 'Mubarak', 'Sakina', 'Mudassar', 'Samiya', 'Muhammad', 'Samina',
#     'Mukhtar', 'Samreen', 'Mumtaz', 'Samina', 'Munir', 'Samra', 'Mushtaq', 'Sana', 'Mustafa', 'Sara',
#     'Nadeem', 'Sarah', 'Naeem', 'Sarwar', 'Najeeb', 'Seema', 'Naseem', 'Shabana', 'Nasir', 'Shabnam',
#     'Naveed', 'Shagufta', 'Nazir', 'Shahida', 'Nisar', 'Shahla', 'Noor', 'Shahzadi', 'Nooruddin', 'Shahnaz',
#     'Nur', 'Shaista', 'Nusrat', 'Shakeela', 'Qadir', 'Shameem', 'Qasim', 'Shazia', 'Qayyum', 'Shazma',
#     'Qurban', 'Shireen', 'Rafiq', 'Shumaila', 'Rahat', 'Sobia', 'Raheem', 'Sofia', 'Rahim', 'Sumaira',
#     'Rahman', 'Sultana', 'Rais', 'Sumbal', 'Raja', 'Suriya', 'Rashid', 'Tabassum', 'Rasheed', 'Tahira',
#     'Rehan', 'Tahzeeb', 'Rizwan', 'Tanzila', 'Saeed', 'Tasneem', 'Safdar', 'Tayyaba', 'Sajjad', 'Tehmina',
#     'Sajid', 'Uzma', 'Salahuddin', 'Wajiha', 'Saleem', 'Yasmeen', 'Salman', 'Zahida']
#
#
# # Sample phone numbers (randomly generated)
# def generate_phone_numbers(num_students):
#     phone_numbers = []
#     for _ in range(num_students):
#         phone = '03' + ''.join(rand.choices('0123456789', k=9))
#         phone_numbers.append(phone)
#     return phone_numbers
#
# # Sample route stop IDs (assuming you have a list of route stop IDs)
# sample_route_stop_ids = [
#     101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
#     201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213,
#     301, 302, 303, 304, 305, 306, 307,
#     401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412,
#     501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512,
#     601, 602, 603, 604, 605, 606, 607, 608, 609, 610,
#     701, 702, 703, 704, 705, 706, 707, 708, 709, 710,
#     801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811,
#     901, 902, 903, 904, 905, 906, 907, 908,
#     1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008,
#     1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109,
#     1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209,
#     1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315,
#     1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415,
#     1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515
# ]
#
#
# # Number of students
# num_students = 495
#
# # Generate student IDs, names, phone numbers, and route stop IDs
# student_ids = generate_student_ids(num_students)
# student_names = rand.choices(pakistani_names, k=num_students)
# phone_numbers = generate_phone_numbers(num_students)
# route_stop_ids = rand.choices(sample_route_stop_ids, k=num_students)
#
# # Assuming you have a cursor object for executing SQL queries
# for i in range(num_students):
#     cursor.execute("INSERT INTO Students (std_id, std_name, phone_no, routestop_id) VALUES (?, ?, ?, ?)",
#                    (student_ids[i], student_names[i], phone_numbers[i], route_stop_ids[i]))





#INSERTION INTO BOOKINGS TABLE:


# Function to generate a unique booking ID
def generate_unique_booking_id():
    while True:
        booking_id = rand.randint(1, 10000)  # Assuming booking IDs range from 1 to 10000
        cursor.execute("SELECT booking_id FROM bookings WHERE booking_id = ?", (booking_id,))
        if not cursor.fetchone():
            return booking_id

# Function to retrieve a valid student ID
def get_valid_student_id():
    cursor.execute("SELECT std_id FROM students")
    valid_student_ids = [row.std_id for row in cursor.fetchall()]
    return rand.choice(valid_student_ids)

# Function to retrieve route_id and bus_id based on student ID
def get_route_and_bus_ids(std_id):
    cursor.execute("""
        SELECT rs.route_id, r.bus_id 
        FROM routeStops rs 
        JOIN routess r ON rs.route_id = r.route_id 
        WHERE rs.routestop_id = (SELECT s.routestop_id FROM students s WHERE s.std_id = ?)
    """, (std_id,))
    route_bus_row = cursor.fetchone()
    if route_bus_row:
        return route_bus_row
    else:
        # Handle the case where no route_id and bus_id are found for the given student ID
        print(f"No route_id and bus_id found for student ID {std_id}")
        return None, None

def generate_booking_datetime(semester):
    semester_dates = {
        'SP24': (datetime(2024, 2, 1), datetime(2024, 6, 16)),
        'FA23': (datetime(2023, 9, 1), datetime(2023, 12, 31)),
        'SP23': (datetime(2023, 2, 1), datetime(2023, 6, 16)),
        'FA22': (datetime(2022, 9, 1), datetime(2022, 12, 31)),
        'SP22': (datetime(2022, 2, 1), datetime(2022, 6, 16))
    }
    start_date, end_date = semester_dates.get(semester)
    random_days = rand.randint(0, (end_date - start_date).days)
    random_time = time(rand.randint(8, 20), rand.randint(0, 59), rand.randint(0, 59))  # Random time between 8:00 AM and 8:00 PM
    booking_datetime = datetime.combine(start_date + timedelta(days=random_days), random_time)
    return booking_datetime

# Insert data into the bookings table
num_bookings = 1000  # Specify the number of bookings to generate
student_route_bus_map = {}  # Dictionary to store route and bus for each student

for _ in range(num_bookings):
    # Generate unique booking ID
    booking_id = generate_unique_booking_id()

    # Generate a valid student ID
    std_id = get_valid_student_id()

    # Retrieve or assign route_id and bus_id based on student ID
    if std_id not in student_route_bus_map:
        route_id, bus_id = get_route_and_bus_ids(std_id)
        if route_id is None or bus_id is None:
            continue  # Skip this iteration if route_id or bus_id is not found
        student_route_bus_map[std_id] = (route_id, bus_id)
    else:
        route_id, bus_id = student_route_bus_map[std_id]

    # Generate random semester
    semester = rand.choice(['SP24', 'FA23', 'SP23', 'FA22', 'SP22'])

    # Generate random booking datetime for the selected semester
    booking_datetime = generate_booking_datetime(semester)

    # Insert data into the bookings table
    cursor.execute("INSERT INTO bookings (booking_id, std_id, route_id, bus_id, booking_datetime, semester) VALUES (?, ?, ?, ?, ?, ?)",
                   (booking_id, std_id, route_id, bus_id, booking_datetime, semester))













# cursor.execute('delete from students')
# connection.commit()
#cursor.execute("DELETE FROM bookings")
connection.commit()
# Close the connection
connection.close()

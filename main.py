import datetime as dt
from ntpath import join
import sqlite3 as db
import uuid
from prettytable import PrettyTable as pt

conn = db.connect("presensi.db")
cur = conn.cursor()

def squek():
    def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS "student" (
                    	"ID"	INTEGER,
                    	"name"	TEXT NOT NULL,
                        "phone" TEXT NOT NULL,
                    	"alamat"	TEXT NOT NULL,
                        "userID" INTEGER NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT),
                        FOREIGN KEY("userID") REFERENCES [account] (ID)
                    );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "teacher" (
                    	"ID"	INTEGER,
                    	"name"	TEXT NOT NULL,
                        "phone" TEXT NOT NULL,
                    	"alamat"	TEXT NOT NULL,
                        "userID" INTEGER NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT),
                        FOREIGN KEY("userID") REFERENCES [account] (ID)
                    );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "account" (
                    	"ID"	INTEGER,
                    	"username"	TEXT NOT NULL,
                        "password" TEXT NOT NULL,
                        "email" TEXT NOT NULL,
                    	"type"	INTEGER NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT)
                    );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "course" (
                    	"ID"	INTEGER,
                    	"name"	TEXT NOT NULL,
                        "teachID" INTEGER NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT),
                        FOREIGN KEY("teachID") REFERENCES [teacher] (ID)                
                    );""")        
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "academic_year" (
                    	"ID"	INTEGER,
                    	"year"	TEXT NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT)
                    );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "semester" (
                    	"ID"	INTEGER,
                    	"name"	TEXT NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT)
                    );""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "attendance_header" (
                    	"ID"	INTEGER,
                    	"semesterID"	INTEGER NOT NULL,
                        "acaID" INTEGER NOT NULL,
                        "studentID" INTEGER NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT),
                        FOREIGN KEY("semesterID") REFERENCES [semester] (ID),        
                        FOREIGN KEY("studentID") REFERENCES [student] (ID),
                        FOREIGN KEY("acaID") REFERENCES [academic_year] (ID) 
                    );""")        
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "attendance_detail" (
                    	"ID"	INTEGER,
                        "headerID" INTEGER NOT NULL,
                    	"courseID"	INTEGER NOT NULL,
                        "meet1" INTEGER,
                        "meet2" INTEGER,
                        "meet3" INTEGER,
                        "meet4" INTEGER,
                        "meet5" INTEGER,
                        "meet6" INTEGER,
                        "meet7" INTEGER,
                        "meet8" INTEGER,
                        "meet9" INTEGER,
                        "meet10" INTEGER,
                        "meet11" INTEGER,
                        "meet12" INTEGER,
                        "meet13" INTEGER,
                        "meet14" INTEGER,
                        FOREIGN KEY("courseID") REFERENCES [course] (ID),                
                        FOREIGN KEY("headerID") REFERENCES [attendance_header] (ID)                
                    	PRIMARY KEY("ID" AUTOINCREMENT)
                    );""")    
        
        cur.execute("""CREATE TABLE IF NOT EXISTS "meeting_code" (
                    	"ID"	INTEGER,
                        "courseID" INTEGER NOT NULL,
                        "storedCode" INTEGER NOT NULL,
                        "whichMeeting" INTEGER NOT NULL,
                        "startDate" TEXT NOT NULL,
                        "endDate" TEXT NOT NULL,
                    	PRIMARY KEY("ID" AUTOINCREMENT)
                    );""")
        dataCount()               
    
    def dataCount():
        cur.execute("select count(*) as count from student")
        for r1 in cur.fetchall():
            count1 = r1[0]    
        cur.execute("select count(*) as count from teacher")
        for r2 in cur.fetchall():
            count2 = r2[0]   
        cur.execute("select count(*) as count from account")
        for r3 in cur.fetchall():
            count3 = r3[0]   
        cur.execute("select count(*) as count from course")
        for r4 in cur.fetchall():
            count4 = r4[0]         
        cur.execute("select count(*) as count from semester")
        for r5 in cur.fetchall():
            count5 = r5[0]      
        cur.execute("select count(*) as count from attendance_header")
        for r6 in cur.fetchall():
            count6 = r6[0]      
        cur.execute("select count(*) as count from attendance_detail")
        for r7 in cur.fetchall():
            count7 = r7[0]       
            
        countAll = [count1, count2, count3, count4, count5, count6, count7]
        
        if(all(v == 0 for v in countAll)):
            exampleData()
            
    def exampleData():
        cur.execute("""INSERT INTO "student" 
                     VALUES (1,'Allan Bil Faqih','698521421442','7th Heaven, Wutai',2),
                     (2,'Zack Fair','4205557892102','Sector 5, Midgar',4),
                     (3,'Linus Sebastian','666251778921','Vancouver, Canada',6),
                     (4,'Thio Joe','178942314979','Detroit, USA',8);
                     """)
        cur.execute("""INSERT INTO "teacher" 
                     VALUES (1,'Erik Salvia','33318748412','Salvia City, Salvia Nation',1),
                     (2,'Princess Zelda','5551124579','Central Hyrule, Hyrule',3),
                     (3,'Kuboyasu Aren','898447511205','Tokyo Prefecture, Japan',5),
                     (4,'The Ashen One','0','Firelink Shrine, Lothric',7);
                     """)
        cur.execute("""INSERT INTO "account" 
                     VALUES (1,'salvia','salvia','salvia@erik.com',1),
                     (2,'allan','nalla','nalla@allan.com',0),
                     (3,'zelda','linkplshelp','zelda@royal.com',1),
                     (4,'zacksoldier22','soldierlifesucks','zack@soldier.com',0),
                     (5,'arenteach21','bkbyeah!','aren@pkgakuen.com',1),
                     (6,'linuses','lttstore.com','linus@lmg.com',0),
                     (7,'ashenone','imonfire!!','firekeeper@feet.com',1),
                     (8,'thiojoe','thisisjoe','thio@joe.com',0);
                     """)
        cur.execute("""INSERT INTO "course" 
                     VALUES (1,'Internet Comment Etiquette Kelas Z',1),
                     (2,'Stopping Ganon Kelas X',2),
                     (3,'Sporty Things Kelas Ψ',3),
                     (4,'Try Not Death Kelas ☠',4);
                     """)
        cur.execute("""INSERT INTO "academic_year" 
                     VALUES (1,'2018/2019'),
                     (2,'2019/2020'),
                     (3,'2020/2021'),
                     (4,'2021/2022'),
                     (5,'2022/2023'),
                     (6,'2023/2024')
                     """)
        cur.execute("""INSERT INTO "semester" (name)
                     VALUES ('Semester 1'),
                     ('Semester 2'),
                     ('Semester 3'),
                     ('Semester 4'),
                     ('Semester 5'),
                     ('Semester 6'),
                     ('Semester 7'),
                     ('Semester 8'),
                     ('Semester 9'),
                     ('Semester 10'),
                     ('Semester 11'),
                     ('Semester 12'),
                     ('Semester 13'),
                     ('Semester 14')
                     """)
        cur.execute("""INSERT INTO "attendance_header" 
                     VALUES (1,1,4,1),
                     (2,1,4,2),
                     (3,1,4,3),
                     (4,1,4,4);
                     """)
        cur.execute("""INSERT INTO "attendance_detail" 
                     VALUES (1,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (2,1,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (3,1,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (4,1,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (5,2,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (6,2,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (7,2,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (8,2,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (9,3,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (10,3,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (11,3,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (12,3,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (13,4,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (14,4,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (15,4,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
                     (16,4,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)                                                               ;
                     """)

        conn.commit()
    
    createTable()
    
def main():
    main.userID = 0
    print("\n[ SISTEM PRESENSI ]")

    def auth(username, password):
        cur.execute("""select count(*) from account
                    where username=? and password=?""", (username, password),)
        for row in cur.fetchall():
            usercount = row[0] 

        if(usercount == 0):
            print("[!] Username atau Password salah!")
            return login()
        else:
            cur.execute("select * from account where username=?", (username,) )
            for row in cur.fetchall():
                status = row[4]

            if(status == 1):
                cur.execute("""select teacher.ID, teacher.name, account.ID, 
                        account.username, account.password, account.type 
                        from teacher 
                        left join account on teacher.userID = account.ID
                        where account.username=?""", (username,) )
                for row in cur.fetchall():
                    main.userID = row[0]
                print("\n[i] Selamat Datang Dosen.")
                pageTeacher()
                
            elif(status == 0):
                cur.execute("""select student.ID, student.name, account.ID, 
                    account.username, account.password, account.type 
                    from student
                    left join account on student.userID = account.ID
                    where account.username=?""", (username,) )
                for row in cur.fetchall():
                    main.userID = row[0]                    
                print("\n[i] Selamat Datang Mahasiswa")
                pageStudent()
    
    def login():
        print("\n[i] Login Page ")
        inpUsername = input("[=] Input Username : ")
        inpPassword = input("[=] Input Password : ")
        
        if(inpUsername == "" or inpPassword == ""):
            print("[!] Input Tidak boleh kosong")
            return login()
        else:
            auth(inpUsername, inpPassword)
    
    def pageTeacher():
        studMenu = ["[1] LIHAT KEHADIRAN MAHASISWA", 
                    "[2] EDIT KEHADIRAN MAHASISWA", 
                    "[3] BUAT KODE PRESENSI",
                    "[4] KEMBALI KE LOGIN",
                    "[0] KELUAR APLIKASI"]
        
        print("\n[i] Pilih Menu. \n") 

        for i in studMenu:
            print(i)

        selectMenu = input("\n[=] Masukkan Angka : ")

        if(selectMenu == "1"):
            showAtdforTch()
            return pageTeacher()
        elif(selectMenu == "2"):
            editAtd()  
            return pageTeacher()   
        elif(selectMenu == "3"):
            createCode()
            return pageTeacher()
        elif(selectMenu == "4"):
            return login()
        elif(selectMenu == "0"):
            print("[i] Goodbye!")
            return
        else:
            print("[!] Input Salah!")

    def pageStudent():
        studMenu = ["[1] LIHAT KEHADIRAN", 
                    "[2] SCAN KODE PRESENSI", 
                    "[3] KEMBALI KE LOGIN",
                    "[0] KELUAR APLIKASI"]
        
        print("\n[i] Pilih Menu. \n") 

        for i in studMenu:
            print(i)

        selectMenu = input("\n[=] Masukkan Angka : ")

        if(selectMenu == "1"):
            showAtdforStd()
            return pageStudent()
        elif(selectMenu == "2"):
            scanCode()
            return pageStudent()
        elif(selectMenu == "3"):
            return login()
        elif(selectMenu == "0"):
            print("[i] Goodbye!")
            return
        else:
            print("[!] Input Salah!")       
                
    def showAtdforStd():      
        thisYear = dt.datetime.now()
        lastYear = dt.datetime(thisYear.year - 1, thisYear.month, thisYear.day, 
                               thisYear.hour, thisYear.minute, thisYear.second, thisYear.microsecond)

        cur.execute("select * from attendance_header where studentID=?", (main.userID,))
        for row in cur.fetchall():
            getSemes = row[1]
            getHeaderID = row[0]

        print("\n[i] Keaktifan Kehadiran Mahasiswa | Tahun Akademik ", 
            lastYear.year, "/", thisYear.year, "- Semester", getSemes)
        
        colAtd = ['Mata Kuliah', '1', '2', '3', '4', '5', '6', '7', '8' , '9', '10', '11', '12', '13', '14']
        cur.execute("""select course.name, meet1, meet2, 
                    meet3, meet4, meet5, meet6, meet7, 
                    meet8, meet9, meet10, meet11, 
                    meet12, meet13, meet14 from attendance_detail
                    left join course on attendance_detail.courseID = course.ID
                    where headerID=?""", (getHeaderID,))

        newPT = pt()
        newPT.field_names = colAtd
        for r in cur.fetchall():
            newPT.add_row(r)
        print(newPT)

    def processingCode(startDate, endDate, numMeet, courseID):
        format = "%Y-%m-%d %H:%M:%S.%f"
        if(dt.datetime.now() <= dt.datetime.strptime(startDate, format)):
            print("[!] Tidak Waktunya untuk Presensi.")

        elif(dt.datetime.now() >= dt.datetime.strptime(startDate, format) and dt.datetime.now() <= dt.datetime.strptime(endDate, format)):
            getMeet = "meet" + str(numMeet)
            cur.execute("""select * from attendance_header 
                        where studentID=?""", (main.userID,))
            for i in cur.fetchall():
                getHeaderID = i[0]

            try:
                cur.execute("""update attendance_detail set {whatMeet}=? 
                            where courseID=? and headerID=?""".format(whatMeet=getMeet), ("HADIR", courseID, getHeaderID))
            except:
                print("[!] Ada Kesalahan!")                
                return scanCode()
            finally:
                conn.commit()

        elif(dt.datetime.now() >= dt.datetime.strptime(endDate, format)):
            print("[!] Waktu Presensi Habis")

    def scanCode():
        print("[i] Scan Presensi | Ketik 'Exit' atau '0' untuk kembali")
        inpCode = input("[=] Silakan Input Kode yang sudah di share oleh Dosen Pengampu : ")
        
        if(inpCode == "exit" or inpCode == "Exit" or inpCode == "0"):
            return pageStudent()
            
        try:
            cur.execute("select * from meeting_code where storedCode=?", (inpCode,))
        except:
            print("[!] Ada Kesalahan!")
            return scanCode()
        finally:
            for r in cur.fetchall():
                getCourseID = r[1]
                #getCode = r[2]
                getNumMeeting = r[3]
                getStartDate = r[4]
                getEndDate = r[5]
                print(getStartDate, getEndDate, dt.datetime.now)
                processingCode(getStartDate, getEndDate, getNumMeeting, getCourseID)
        
    def showAtdforTch():      
        thisYear = dt.datetime.now()
        lastYear = dt.datetime(thisYear.year - 1, thisYear.month, thisYear.day, 
                               thisYear.hour, thisYear.minute, thisYear.second, thisYear.microsecond)

        cur.execute("""select * from attendance_detail
                        left join course on attendance_detail.courseID = course.ID
                        left join teacher on course.teachID = teacher.ID
                        left join attendance_header on attendance_detail.headerID = attendance_header.ID
                        where course.teachID=?""", (main.userID,))
        for row in cur.fetchall():
            getSemes = row[26]
            getCourseID = row[17]
            getCourseName = row[18]

        print("\n[i] Keaktifan Kehadiran Mahasiswa | Tahun Akademik ", 
            lastYear.year, "/", thisYear.year, "- Semester", getSemes, "| Mata Kuliah -", getCourseName)
        
        colAtd = ['Nama Mahasiswa', '1', '2', '3', '4', '5', '6', '7', '8' , '9', '10', '11', '12', '13', '14']
        cur.execute("""select student.name,
					meet1, meet2, meet3, meet4, 
					meet5, meet6, meet7, 
                    meet8, meet9, meet10, meet11, 
                    meet12, meet13, meet14 from attendance_detail
					left join attendance_header on attendance_detail.headerID = attendance_header.ID
					left join student on attendance_header.studentID = student.ID
                    where courseID=?""", (getCourseID,))

        newPT = pt()
        newPT.field_names = colAtd
        for r in cur.fetchall():
            newPT.add_row(r)
        print(newPT)            

    def updateingAtd(numMeet, textMeet, studName):
        cur.execute("""select * from attendance_header 
                    left join student on student.ID = attendance_header.studentID
                    where student.name like ?""", (studName,))
        for i in cur.fetchall():
            getHeaderID = i[0]

        getMeet = "meet" + str(numMeet)

        try:
            cur.execute("""update attendance_detail set {whatMeet}=? 
                        where headerID=?""".format(whatMeet=getMeet), (textMeet, getHeaderID,))
        except:
            print("[!] Ada Kesalahan!")
            return editAtd()
        finally:
            conn.commit()

    def editAtd():        
        showAtdforTch()
        print("[i] Rubah Kehadiran Mahasiswa | Ketik 'Exit' atau '0' di kolom Nama dan kosongkan kolom Meeting untuk kembali")
        inpName = input("\n[=] Masukkan Nama Mahasiswa : ")
        inpMeet = input("[=] Meeting Keberapa? : ")

        if(inpName == "exit" or inpName == "Exit" or inpName == "0"):
            return pageTeacher()

        studMenu = ["\n[1] HADIR", "[2] SAKIT", "[3] IZIN", "[4] ALPHA"]
        for i in studMenu:
            print(i)    

        inpChange = input("\n[=] Silahkan Pilih Nomor : ")
        if(inpChange == "1"):
            updateingAtd(inpMeet, "HADIR", inpName)
        elif(inpChange == "2"):
            updateingAtd(inpMeet, "SAKIT", inpName)
        elif(inpChange == "3"):
            updateingAtd(inpMeet, "IZIN", inpName)
        elif(inpChange == "4"):
            updateingAtd(inpMeet, "ALPHA", inpName)
        else:
            print("[!] Input Salah!")
            return editAtd()

    def createCode():
        dateNow = dt.datetime.now()
        dateLater = dateNow + dt.timedelta(minutes = 30)
        cur.execute("select * from course where teachID=?",(main.userID,))

        for r in cur.fetchall():
            getCourseID = r[0]

        getCode = ''.join(str(uuid.uuid4()).split('-'))
        print("[i] Buat Kode Untuk Kehadiran Mahasiswa | Ketik 'Exit' atau '0' di kolom Nama untuk kembali")
        print("[i] Kode ini hanya bisa digunakan selama 1 jam dari pembuatan kode ini.")
        inpWhichMeet = int(input("[=] Pilih Meeting ke berapa : "))

        if(inpWhichMeet == "exit" or inpWhichMeet == "Exit" or inpWhichMeet == "0"):
            return pageTeacher()
        try:
            cur.execute("""insert into meeting_code(courseID, storedCode, 
                            whichMeeting, startDate, endDate) values(?, ?, ?, ?, ?)""",
                            (getCourseID, getCode, inpWhichMeet, dateNow, dateLater,))
        except:
            print("[!] Ada Kesalahan")
            return createCode()
        finally:
            print("[i] Kode Yang telah dibuat : ", getCode)
            conn.commit()            
    
    login()
    
squek()
main()
conn.close()
#created by ABF 383

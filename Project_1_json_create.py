import json
All_List_In_Bank =[
  {
    "ID": 1,
    "Name": "mohamed",
    "Password": "a",
    "Phone number": "01010223344",
    "Mail": "mohamed@gmail.com",
    "Gender": "Male",
    "Age": 23,
    "City": "Giza",
    "Balance": 100.0
  },
  {
    "ID": 2,
    "Name": "ahmed",
    "Password": "b",
    "Phone number": "01011223344",
    "Mail": "ahmed@gmail.com",
    "Gender": "Male",
    "Age": 21,
    "City": "Tanta",
    "Balance": 350.0
  },
  {
    "ID": 3,
    "Name": "aya",
    "Password": "c",
    "Phone number": "01012223344",
    "Mail": "aya@gmail.com",
    "Gender": "Female",
    "Age": 19,
    "City": "Tanta",
    "Balance": 270
  },
  {
    "ID": 4,
    "Name": "salma",
    "Password": "d",
    "Phone number": "01013223344",
    "Mail": "salma@gmail.com",
    "Gender": "Female",
    "Age": 20,
    "City": "October",
    "Balance": 300
  },
  {
    "ID": 5,
    "Name": "abdullah",
    "Password": "e",
    "Phone number": "01014223344",
    "Mail": "abdullah@gmail.com",
    "Gender": "Male",
    "Age": 26,
    "City": "Ramses",
    "Balance": 400
  },
  {
    "ID": 6,
    "Name": "moamen",
    "Password": "f",
    "Phone number": "01015223344",
    "Mail": "moamen@gmail.com",
    "Gender": "Male",
    "Age": 24,
    "City": "Shebin el kom",
    "Balance": 350
  },
  {
    "ID": 7,
    "Name": "maher",
    "Password": "g",
    "Phone number": "01016223344",
    "Mail": "maher@gmail.com",
    "Gender": "Male",
    "Age": 25,
    "City": "Banha",
    "Balance": 430
  },
  {
    "ID": 8,
    "Name": "mona",
    "Password": "h",
    "Phone number": "01017223344",
    "Mail": "mona@gmail.com",
    "Gender": "Female",
    "Age": 29,
    "City": "El shorouk",
    "Balance": 560
  },
  {
    "ID": 9,
    "Name": "nourhan",
    "Password": "i",
    "Phone number": "01018223344",
    "Mail": "nourhan@gmail.com",
    "Gender": "Female",
    "Age": 31,
    "City": "El shorouk",
    "Balance": 590
  },
  {
    "ID": 10,
    "Name": "khaled",
    "Password": "j",
    "Phone number": "01019223344",
    "Mail": "khaled@gmail.com",
    "Gender": "Male",
    "Age": 36,
    "City": "Menouf",
    "Balance": 790
  },
  {
    "ID": 11,
    "Name": "rofida",
    "Password": "k",
    "Phone number": "01011203344",
    "Mail": "rofida@gmail.com",
    "Gender": "Female",
    "Age": 22,
    "City": "Domyat",
    "Balance": 610
  },
  {
    "ID": 12,
    "Name": "shimaa",
    "Password": "l",
    "Phone number": "01011213344",
    "Mail": "shimaa@gmail.com",
    "Gender": "Female",
    "Age": 38,
    "City": "Domyat",
    "Balance": 900
  },
  {
    "ID": 13,
    "Name": "hussein",
    "Password": "m",
    "Phone number": "01011233344",
    "Mail": "hussein@gmail.com",
    "Gender": "Male",
    "Age": 30,
    "City": "Alexandria",
    "Balance": 1020
  },
  {
    "ID": 14,
    "Name": "youssef",
    "Password": "n",
    "Phone number": "01011243344",
    "Mail": "youssef@gmail.com",
    "Gender": "Male",
    "Age": 33,
    "City": "Ashmoun",
    "Balance": 1130
  },
  {
    "ID": 15,
    "Name": "medhat",
    "Password": "o",
    "Phone number": "01011253344",
    "Mail": "medhat@gmail.com",
    "Gender": "Male",
    "Age": 39,
    "City": "Ashmoun",
    "Balance": 930
  },
  {
    "ID": 16,
    "Name": "nouran",
    "Password": "p",
    "Phone number": "01011263344",
    "Mail": "nouran@gmail.com",
    "Gender": "Female",
    "Age": 34,
    "City": "Cairo",
    "Balance": 730
  },
  {
    "ID": 17,
    "Name": "yara",
    "Password": "q",
    "Phone number": "01011273344",
    "Mail": "yara@gmail.com",
    "Gender": "Female",
    "Age": 24,
    "City": "Cairo",
    "Balance": 1280
  },
  {
    "ID": 18,
    "Name": "soad",
    "Password": "r",
    "Phone number": "01011283344",
    "Mail": "soad@gmail.com",
    "Gender": "Female",
    "Age": 26,
    "City": "Egypt",
    "Balance": 1050
  },
  {
    "ID": 19,
    "Name": "omar",
    "Password": "s",
    "Phone number": "01011293344",
    "Mail": "omar@gmail.com",
    "Gender": "Male",
    "Age": 40,
    "City": "Egypt",
    "Balance": 1650
  },
  {
    "ID": 20,
    "Name": "hosny",
    "Password": "t",
    "Phone number": "01013293344",
    "Mail": "hosny@gmail.com",
    "Gender": "Male",
    "Age": 37,
    "City": "menouf",
    "Balance": 2030
  },
  {
    "Name": "Reda",
    "ID": 21,
    "Password": "r",
    "Phone number": "010141516128",
    "Mail": "reda@gmail.com",
    "Gender": "Male",
    "Age": "36",
    "City": "Syez",
    "Balance": 2000.0
  }
]





file = open ("Project_1_json.json","w")   # write data
json.dump(All_List_In_Bank,file,indent=2)
file.close()
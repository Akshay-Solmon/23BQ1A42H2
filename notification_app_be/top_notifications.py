from datetime import datetime

TYPE_WEIGHT = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

notifications = [
    {"ID":"1","Type":"Placement","Message":"Google Hiring","Timestamp":"2026-04-22 17:51:18"},
    {"ID":"2","Type":"Placement","Message":"Amazon Hiring","Timestamp":"2026-04-22 17:50:18"},
    {"ID":"3","Type":"Placement","Message":"Microsoft Hiring","Timestamp":"2026-04-22 17:49:18"},
    {"ID":"4","Type":"Placement","Message":"Infosys Hiring","Timestamp":"2026-04-22 17:48:18"},
    {"ID":"5","Type":"Placement","Message":"TCS Hiring","Timestamp":"2026-04-22 17:47:18"},
    {"ID":"6","Type":"Placement","Message":"Wipro Hiring","Timestamp":"2026-04-22 17:46:18"},
    {"ID":"7","Type":"Placement","Message":"Accenture Hiring","Timestamp":"2026-04-22 17:45:18"},

    {"ID":"8","Type":"Result","Message":"Mid Sem Results","Timestamp":"2026-04-22 17:51:30"},
    {"ID":"9","Type":"Result","Message":"Project Review","Timestamp":"2026-04-22 17:50:42"},
    {"ID":"10","Type":"Result","Message":"Lab Results","Timestamp":"2026-04-22 17:49:30"},
    {"ID":"11","Type":"Result","Message":"External Results","Timestamp":"2026-04-22 17:48:30"},
    {"ID":"12","Type":"Result","Message":"Internal Marks","Timestamp":"2026-04-22 17:47:30"},
    {"ID":"13","Type":"Result","Message":"Semester Results","Timestamp":"2026-04-22 17:46:30"},

    {"ID":"14","Type":"Event","Message":"Tech Fest","Timestamp":"2026-04-22 17:50:06"},
    {"ID":"15","Type":"Event","Message":"Farewell","Timestamp":"2026-04-22 17:49:06"},
    {"ID":"16","Type":"Event","Message":"Hackathon","Timestamp":"2026-04-22 17:48:06"},
    {"ID":"17","Type":"Event","Message":"Workshop","Timestamp":"2026-04-22 17:47:06"},
    {"ID":"18","Type":"Event","Message":"Seminar","Timestamp":"2026-04-22 17:46:06"},
    {"ID":"19","Type":"Event","Message":"Coding Contest","Timestamp":"2026-04-22 17:45:06"},
    {"ID":"20","Type":"Event","Message":"Alumni Meet","Timestamp":"2026-04-22 17:44:06"}
]

def calculate_priority(notification):
    type_score = TYPE_WEIGHT.get(notification["Type"], 0)

    timestamp = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    return (type_score * 10000000000) + timestamp.timestamp()

def get_top_notifications(notifications, top_n=10):
    return sorted(
        notifications,
        key=calculate_priority,
        reverse=True
    )[:top_n]

def main():
    top10 = get_top_notifications(notifications, 10)

    print("\n===== TOP 10 PRIORITY NOTIFICATIONS =====\n")

    for i, n in enumerate(top10, start=1):
        print(f"{i}.")
        print(f"ID        : {n['ID']}")
        print(f"Type      : {n['Type']}")
        print(f"Message   : {n['Message']}")
        print(f"Timestamp : {n['Timestamp']}")
        print("-" * 50)

if __name__ == "__main__":
    main()

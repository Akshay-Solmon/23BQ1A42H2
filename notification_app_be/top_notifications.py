import requests
from datetime import datetime

API_URL = "http://4.224.186.213/evaluation-service/notifications"

TYPE_WEIGHT = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

def fetch_notifications():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()["notifications"]

def calculate_priority(notification):
    type_score = TYPE_WEIGHT.get(
        notification["Type"],
        0
    )

    timestamp = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    recency_score = timestamp.timestamp()

    return (
        type_score * 10000000000
        + recency_score
    )

def get_top_notifications(
    notifications,
    top_n=10
):
    return sorted(
        notifications,
        key=calculate_priority,
        reverse=True
    )[:top_n]

def main():
    notifications = fetch_notifications()

    top10 = get_top_notifications(
        notifications,
        10
    )

    print("\nTOP 10 NOTIFICATIONS\n")

    for n in top10:
        print(n)

if __name__ == "__main__":
    main()

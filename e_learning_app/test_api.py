import requests

url = "http://localhost:8069/api/create_course"
payload = {
    "school_name": "Dummy School",
    "level": "secondary",
    "academic_year": "2022",
    "semester": "2nd",
    "faculty": "Science",
    "department": "Physics",
    "course_title": "Dummy Course",
    "course_code": "DC101"
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)

print(response.json())

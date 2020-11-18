import requests

res = requests.post('http://localhost:5000/postdata?collection=activity', json={"customer_id":"1001", "activity":"dance", "duration":"01:30:00", "calorie_burn":"700", "heart_rate_max":"130", "acc_id":"1002"})

print(res)

res = requests.post('http://localhost:5000/postdata?collection=activity', json={"customer_id":"1002", "activity":"running", "duration":"00:30:00", "calorie_burn":"250","distance":"4", "distance_unit":"km", "calorie_unit":"Kcal", "steps":"10000", "heart_rate_max":"130", "heart_rate_unit":"bpm", "acc_id":"1002"})

print(res)

res = requests.post('http://localhost:5000/postdata?collection=activity', json={"customer_id":"1004", "activity":"running", "duration":"01:30:00", "calorie_burn":"500","distance":"5", "distance_unit":"km", "calorie_unit":"Kcal", "steps":"50000", "heart_rate_unit":"bpm", "heart_rate_max":"140", "acc_id":"1004"})

print(res)

res = requests.post('http://localhost:5000/postdata?collection=activity', json={"customer_id":"1004", "activity":"yoga", "duration":"00:54:00", "calorie_burn":"90", "heart_rate_max":"80", "heart_rate_unit":"bpm", "acc_id":"1004"})

print(res)

res = requests.post('http://localhost:5000/postdata?collection=activity', json={"customer_id":"1005", "activity":"weight_lifting", "duration":"00:30:00", "calorie_burn":"300", "heart_rate_max":"100", "heart_rate_unit":"bpm", "acc_id":"1005"})

print(res)

res = requests.post('http://localhost:5000/postdata?collection=activity', json={"customer_id":"1005", "activity":"walking", "duration":"01:00:00","distance_unit": "km", "distance":"5", "calorie_burn":"300", "steps":"30000","heart_rate_max":"110", "heart_rate_unit":"bpm", "acc_id":"1005"})

print(res)

res = requests.post('http://localhost:5000/postdata?collection=activity', json={"customer_id":"1003", "activity":"cycle", "duration":"01:00:00", "calorie_burn":"400", "heart_rate_max":"140", "heart_rate_unit":"bpm", "acc_id":"1003"})

print(res)

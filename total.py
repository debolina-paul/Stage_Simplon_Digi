import requests

res = requests.post('http://localhost:5000/postdata?collection=total', json={"customer_id":"1001", "steps":"13254", "duration":"01:30:00", "calorie_burn":"700", "heart_rate_max":"130", "acc_id":"1001", "distance":"4km"})

print(res)

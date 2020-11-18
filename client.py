import requests
res = requests.post('http://localhost:5000/postdata?collection=customer', json={"first_name":"Debayan", "last_name":"Paul", "data_of_birth":"01/07/1993", "city":"Milan", "country":"Italy", "age":"27", "payment":"true", "customer_id":"1001", "acc_id":"1001"})
print(res)

res = requests.post('http://localhost:5000/postdata?collection=customer', json={"first_name":"Tanmay", "last_name":"Chakraborty", "data_of_birth":"15/05/1998", "city":"Valbonne", "country":"France", "age":"23", "payment":"true", "customer_id":"1003", "acc_id":"1003"})
print(res)

res = requests.post('http://localhost:5000/postdata?collection=customer', json={"first_name":"Nicole", "last_name":"Parrigot", "data_of_birth":"02/07/1982", "city":"Nice", "country":"France", "age":"38", "payment":"true", "customer_id":"1004", "acc_id":"1004"})
print(res)

res = requests.post('http://localhost:5000/postdata?collection=customer', json={"first_name":"Fernanda", "last_name":"D'Costa", "data_of_birth":"12/03/1992", "city":"Nice", "country":"France", "age":"28", "payment":"true", "customer_id":"1005", "acc_id":"1005"})
print(res)

res = requests.post('http://localhost:5000/postdata?collection=customer', json={"first_name":"Debolina", "last_name":"Paul", "data_of_birth":"18/05/1988", "city":"Antibes", "country":"France", "age":"32", "payment":"true", "customer_id":"1002", "acc_id":"1002"})
print(res)






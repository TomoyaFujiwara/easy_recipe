var obj;

fetch('http://localhost:5000/api/v1/users/test_id')
  .then(res => res.json())
  .then(data => obj = data)
  .then(() => console.log(obj))

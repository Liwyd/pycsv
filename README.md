# CSV db Manager
## How To Install
```
git clone https://github.com/Liwyd/csv-database-Manager.git
```

## How To Use
- Import dManager in your .py file
```python
from dManager import Managedb

user1 = Managedb('123456789', 'users.csv')
user1.ADD_user()
user1.READ_info(2)
user1.CHANGE_info(2,1000)
user1.ADD_info(2, 500)
```

- Result in 'users.csv':
```
123456789,0,1500,0,0,2,1,3
```

- you can cahnge the defult values of each new user at line 35

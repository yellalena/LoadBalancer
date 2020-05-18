to test:

install project dependencies
```
pip install -r dependencies.txt 
```

then in one terminal start the server
```bash
python manage.py runserver 
```
then in another run
```
python3 limiter.py
```
if everything is ok, the result should be
```
all 200 OK
len of rountine_counters is 4
```
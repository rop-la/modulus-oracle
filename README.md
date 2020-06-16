
# Modulus Oracle Demo

## How to run

- Clone the repository

```
git clone https://github.com/rop-la/modulus-oracle.git
```

- Change the directory

```
cd modulus-oracle
```

- Generate a private key with `openssl`

```
openssl genrsa -out priv.key 512
```

- Create a Python virtual environment

```
virtualenv -p python3 venv
```

- Activate the virtual environment

```
source venv/bin/activate
```

- Install requirements

```
pip install -r requirements.txt
```

- Run the Flask application

```
python main.py
```

- Run the demo script

```
python modulus-oracle.py
```

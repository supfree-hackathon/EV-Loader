EV-Loader
==========


## Project Summary
![alt text](./project_summary.png)


## Requirements
* python 3
* pipenv


## Instructions

### Web App
```
cd web
pipenv install
pipenv shell
python manage.py runserver
```
### Mobile
```
cd mobile
yarn install
npm install expo-cli --global
expo start
```
### Rasberry Pi
## POC Hardware
![alt text](./rpi/docs/images/Wiring.png)
```
cd rpi
python nfc.py
```
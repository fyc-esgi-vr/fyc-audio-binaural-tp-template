# FYC TP AUDIO

## **Prerequisites**

#### <u>Python version 3:</u>

* [Windows](https://www.python.org/downloads/release/python-3100/) 
* Linux: 

    > `sudo apt update`

    > `sudo apt install python3`

    > `sudo apt install pip`

    > `sudo pip install venv`

<br>

#### <u>Install OpenAL dependency:</u>

* [Windows](https://www.openal.org/) 
* Linux: 

    > `git clone https://github.com/kcat/openal-soft`

    > `cd openal-soft/build`

    > `cmake ..`

    > `sudo cmake --build .`

<br>

## **Run application**

### **Create virtual environment**

> `python -m venv venv` or `python3 -m venv venv`

> `source venv/bin/activate`

> `pip install python-openal`

<br>


### **Execute program**

> `python src/tp2.py` or `python3 src/tp2.py`
> `python src/tp3.py` or `python3 src/tp3.py`

<br>

### **Stop virtual environment**

> `deactivate`



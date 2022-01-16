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

    > `cd PyAL/build`

    > `cmake ..`

    > `make install`
    
<br>

## **Run application**

### **Create virtual environment**

> `python -m venv venv` or `python3 -m venv venv`

> `source venv/bin/activate`

> `pip install python-openal`

<br>


### **Execute program**

> `python src/main.py` or `python3 src/main.py`

<br>

### **Stop virtual environment**

> `deactivate`



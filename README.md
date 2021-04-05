# Azure Hackathon SABJ Team - LIDAS Application # 

This is the code repository to our web app at [lidas.herokuapp.com](http://lidas.herokuapp.com/).

## 1. Overview ## 

This repository stores all scripts that are used for Azure Hackathon LIDAS Application.
Let's get started!

## 2. Ground Rules ##

* Always keep your credentials on local! Do not ever push your password and username to remote repository
* Check with each other before pushing to main branch. Check out another branch if you plan to work on it using ```git branch [yourbranch]``` and ```git checkout [yourbranch]``` 

## 3. Getting started ##

1. Clone the repository to your destination 
```
cd my/dir
git clone https://github.com/JasonZhangHub/azure_hackathon.git
```
2. Setup your virtual environment and activate
```
conda create --name [yourenvname] python=3.7
conda activate [yourenvname] 
```
or 
```
python3 -m venv [yourenvname]
source [yourenvname]/bin/activate
```
3. Install requirements

```
conda install --file requirements.txt
```
or 
```
pip install -r requirements.txt
```

4. Run LIDAS application locally
```
cd lidas
streamlit run main_app.py
```

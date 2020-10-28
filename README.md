# Vesper Commit Severity Predictor

[![HitCount](http://hits.dwyl.io/margaritageleta/vesper-tech-debt.svg)](http://hits.dwyl.io/margaritageleta/vesper-tech-debt)[![GitHub stars](https://img.shields.io/github/stars/margaritageleta/vesper-tech-debt.svg)](https://GitHub.com/margaritageleta/vesper-tech-debt/stargazers/)[![GitHub forks](https://img.shields.io/github/forks/margaritageleta/vesper-tech-debt.svg)](https://GitHub.com/margaritageleta/vesper-tech-debt/network/)[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/margaritageleta/vesper-tech-debt.svg)](https://github.com/margaritageleta/vesper-tech-debt)[![GitHub contributors](https://img.shields.io/github/contributors/margaritageleta/vesper-tech-debt.svg)](https://GitHub.com/margaritageleta/vesper-tech-debt/graphs/contributors/)[![GitHub license](https://img.shields.io/github/license/margaritageleta/vesper-tech-debt.svg)](https://github.com/margaritageleta/vesper-tech-debt/blob/master/LICENSE)



**Authors**: Dànae Canillas Sánchez, Alex Carrillo Alza, Margarita Geleta, Xavier Rubiés Cullell





## Table of Contents





## Description

Data processing, Model creation and App deployment of **Vesper Commit Severity Predictor**. Trained with data from the *Technical Debt Dataset*.

The goal of the tool is to analyze a set of messages of various large open-source Java projects which used the Git version control system.



## Usage

### Virtual environment setup

**1. Create a virtual environment on your local repository**

Check you have Python 3 version:

```py
$ python3 --version
Python 3.6.2
```

Create venv:

```
$ python3 -m venv vesper_env
```



**2. Activate it to install packages and to execute scripts (ALWAYS!)**

```
$ source ./vesper_env/bin/activate
(vesper_env) @Username/:
```

You can deactivate it with:

```
$ deactivate
```



**3. Install `requirements.txt`**

With the environment activated:

```
(vesper_env) $ pip install -r requirements.txt 
```



**4. Add new packages to the project, if needed**

```
(vesper_env) $ pip install new_package_name
(vesper_env) $ pip freeze -l > requirements.txt 
```

### Install a Jupyter kernel

This will install a kernel inside the environment, to use to run in the Jupyter notebook there:

```
(vesper_env) $ ipython kernel install --user --name=vesper_env
```



### Project files

```
├─ data
│  ├─ our_data
│  │  ├─ commits_violations.pkl
│  │  └─ commits_violations_8.pkl
│  └─ README.md
├─ models
│  ├─ models.md
│  ├─ scaler.pickle
│  └─ tf_idf.pickle
├─ notebooks
│  ├─ models.ipynb
│  ├─ notebooks.md
│  └─ tables_creation.ipynb
├─ src
│  ├─ static
│  │  ├─ logo.jpeg
│  │  └─ style.css
│  ├─ templates
│  │  └─ index.html
│  ├─ Procfile
│  ├─ README.md
│  ├─ analyze.py
│  ├─ app.py
│  ├─ requirements.txt
│  └─ save_models.py
├─ .gitattributes
├─ .gitignore
├─ LICENSE
├─ Procfile
├─ README.md
└─ requirements.txt
```



### Execution steps

**1. Download the database**

Access the GitHub repository of [The Technical Debt Dataset](https://github.com/clowee/The-Technical-Debt-Dataset) and download the latest version of the `.db.zip`  file:

```
TechnicalDebtDataset_v1.01.db.zip  (634 MB)
```



**2. Generate the dataset and the models**

First, execute `tables_creation.ipynb` notebook in order to generate the dataset.

- This notebook saves the **main data table** used in the project: `commits_violations_8.pkl`.

Then, if necessary, execute `model.ipynb` notebook to explore some results regarding the modelling step.

Finally, execute

```
(vesper_env) $ python3 save_models.py
```

in order to save the **final model** `model.pickle` ,  the **tf-idf vectorizer** object `tf_idf.pickle` and the **StandardScaler** object `scaler.pickle` used on preprocessing the input for predictions.



**3. **



## Contributing



## License


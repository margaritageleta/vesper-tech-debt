# Vesper Commit Severity Predictor

[![HitCount](http://hits.dwyl.io/margaritageleta/vesper-tech-debt.svg)](http://hits.dwyl.io/margaritageleta/vesper-tech-debt)  [![GitHub stars](https://img.shields.io/github/stars/margaritageleta/vesper-tech-debt.svg)](https://GitHub.com/margaritageleta/vesper-tech-debt/stargazers/)  [![GitHub forks](https://img.shields.io/github/forks/margaritageleta/vesper-tech-debt.svg)](https://GitHub.com/margaritageleta/vesper-tech-debt/network/)  [![GitHub repo size in bytes](https://img.shields.io/github/repo-size/margaritageleta/vesper-tech-debt.svg)](https://github.com/margaritageleta/vesper-tech-debt)  [![GitHub contributors](https://img.shields.io/github/contributors/margaritageleta/vesper-tech-debt.svg)](https://GitHub.com/margaritageleta/vesper-tech-debt/graphs/contributors/)  [![GitHub license](https://img.shields.io/github/license/margaritageleta/vesper-tech-debt.svg)](https://github.com/margaritageleta/vesper-tech-debt/blob/master/LICENSE)



**Authors**: Dànae Canillas Sánchez, Alex Carrillo Alza, Margarita Geleta, Xavier Rubiés Cullell

*Universitat Politècnica de Catalunya, UPC*

![](https://i.imgur.com/aKAerNT.png)

Visit [vespertd.herokuapp.com](https://vespertd.herokuapp.com/) to access the app!



## Table of Contents

1. [Description](#description)
2. [Usage](#usage)
3. [Project files](#Project files)
4. [Execution steps](#Execution steps)
5. [Contributing](#Contributing)
6. [License](#License)



## Description

This repository contains the development of the **Vesper Commit Severity Predictor** application, including the data processing, model creation and app deployment stages. The model is trained with data from the *Technical Debt Dataset*.

> […] The goal of the tool is to predict the commit violations (of type “blocker”, “critical” and “major or minor”) using the commit message text along with some other numeric variables that help. [...]



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
(vesper_env) $ python3 src/save_models.py
```

in order to save the **final model** `model.pickle` ,  the **tf-idf vectorizer** object `tf_idf.pickle` and the **StandardScaler** object `scaler.pickle` used on preprocessing the input for predictions.



**3. Execute the app locally**

To execute the app, just run:
```
(vesper_env) $ python3 src/app.py
```
Open the [0.0.0.0:8000](0.0.0.0:8000) in your browser to see the app.




## Contributing
Please refer to each project's style and contribution guidelines for submitting patches and additions. In general,  we follow the *fork-and-pull* Git workflow:

1. **Fork** the repo on GitHub.
2. **Clone** the project to your own machine.
3. **Commit** changes to your own branch.
4. **Push** your work back up to your fork.
5. Submit a **Pull request** so that we can review your changes.

NOTE: be sure to merge the latest from *upstream* before making a pull request.



## License
MIT © Vesper

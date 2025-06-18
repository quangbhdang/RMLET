# RMIT MACHINE LEARNING ENVIRONMENT TEMPLATE (RMLET)
This is a template for a machine learning, deep learning project based on the requirements for coursework at RMIT University.
The idea is to create a flexible template environment that caters to multiple machine learning, deep learning, and AI development projects.

**Table of content**:
1. [JUST SET UP GUIDE](#quick-guide)
2. [I WANT TO KNOW MORE](#the-rant-about-the-project)


## QUICK-GUIDE
### Set up using Anaconda (Recommended)

For the sake of simplifying the set up process for our data science project as well as ensure consistent environment set up I recommend using Anaconda for set up. Anaconda or Conda is a data science tool which user to set up data science environment and manage them.

Compare to using PIP (Python Installer Program) to manage the project environment Conda is less complex to set up and manage. Thus unless there are package that you believe can't be install using Conda only then should you consider PIP for project mangement.

Use the following code to install Miniconda on your system if you have not yet for Linux/MacOs

```.sh-session
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

If you are using Window you can use
```.sh-session
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
del miniconda.exe
```
---
NOTE: While WINDOWS is my main OS, I have move to using WSL2 (Windows Subsystem for Linux) as my primary development environment. This is due to the fact that most of the tools and package I use are more compatible with Linux environment. Additionally alot of GPU accelarated project are built for Linux. Thus I highly recommend you use WSL2 if you are using Windows. You can find more information about WSL2 [here](https://docs.microsoft.com/en-us/windows/wsl/install). 
---

After which run the following command to start conda and create conda environment using the provided recommended environment files on this repository.
```
conda init
conda env create --f environment.yml
```

Once done use the following code to active the environment.
```
conda activate myenv
```

CONGRAT you can now start code as normal! All your new package installation should be constrain within this newly create environment.

Once you complete use the following command to turn the environment off
```
conda deactivate
```


## THE RANT ABOUT THE PROJECT
### Goal of this github
1. Create an environment where ML and AI student can quickly use to set up their project.
2. The project repo is clear, well defined and allows for good programming practice.
3. Give a high level of flexibility so it can be further developed into a more complex project.
4. Allow for easy collaboration and replication of experiment results.

### Why this GitHub repository was created
When starting in machine learning, and data science I was stumped as to where to begin my project. In most online material and even at my university the material is often skipped over the setting of the environment and the workspace of the project in favour of rapid prototyping and general theory. Additionally, with the use of Collab most environment set up is done for you and you can just start coding.

While this might work for smaller projects or early introduction to machine learning concepts this quickly becomes a hurdle for more advanced courses and practice projects where complex functions and libraries need to be maintained. This often results in a janky way in which I have to keep track of parameters, experiments result in separate Excel sheets and multiple files just to keep track of my project and collaborate with my peers. This repository was design base on my research on common good practice in managing and collaborating on machine learning environment. In addition, I have include tools and package that I found beneficial during my time of learning AI/Data Science.

### Selected pacakges
The following package was installed.

- Pandas (Or Polar)
- Scikit-learn
- Numpy
- Matplotlib
- Seaborn
- JupyterLab (Instead of Jupyter Notebook as it is more flexible and has more features)

All of the above package are installed using Conda and can be found in the `environment.yml` file. You can add more packages to this file as you see fit.

For more complex project I recommend using:

[DagsHub](https://dagshub.com/) or [Weights & Biases](https://wandb.ai/site) to keep track of your experiment and results. This will allow you to keep track of your experiment and results in a more structured way. DagsHub specifically will give you a Gihub-like interface, Free S3 storage for your data and MLFlow server for your experiment tracking thus I highly recommend it.

[DVC](https://dvc.org/) is also a great tool to keep track of your data and models. It is a version control system for data science projects that allows you to keep track of your data, models, and experiments in a structured way. I use it instead of Git LFS as it is more simple to use and has more features.

[Latex](https://www.latex-project.org/) is also a great tool to use for writing reports and papers. It is a typesetting system that allows you to create professional looking documents with details mathematic and reference controls. In this repository I have included a `report` folder where you can write your report using Latex. You can use the `simple_report.tex` file as a template to get started or download the RMIT Assignment Template Zip to use on Overleaf or local environment. If setting up Latex is too complex for you, you can use [Overleaf](https://www.overleaf.com/) which is an online Latex editor that allows you to write and collaborate on Latex documents easily. There is a great series by Dr Trevor regarding How to use Latex or Overleaf [YouTube](https://www.youtube.com/watch?v=Jp0lPj2-DQA&list=PLHXZ9OQGMqxcWWkx2DMnQmj5os2X5ZR73) which I highly recommend you watch it if you are new to Latex.

### Deep Learning and ML frameworks
For deep learning and ML frameworks, you can use the following frameworks:
- [TensorFlow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)
- [Keras](https://keras.io/)

Depending on your Uni or Project requirement you might need to use one of the above frameworks. I recommend using PyTorch for more academic research since it have more paper implement in this frameworks. Tensorflow on the other hand catered slightly more for industry thus likely will be more relevant for industry specific project. Keras is a high-level API that runs on top of TensorFlow and is great for rapid prototyping and experimentation.

For more information on how to set up these frameworks, you can refer to their official documentation. I keep the installation of these frameworks out of this repository as they are quite large and can be installed using Conda or PIP easily. You can add them to the `environment.yml` file if you want to include them in your copy of the environments.

### The folder structure
Design to aid with keeping each component self contain.

```Mermaid
DATA # Contain your data
├── FINAL # Final data used for training and testing
├── RAW # Raw data that you download from the internet or other sources
├── PROCESSED # Processed data that you use for training and testing
├── INTERIM # Intermediate data that you use for processing

MODEL
├── WEIGHT # Saved model weights
├── CONFIG # Model configuration files
├── LOG # Model training logs

SRC # Source code for your project
├── Data.py # Data processing code
├── Preprocess.py # Model training and evaluation code
├── utils.py # Utility functions for your project

NOTEBOOKS # Jupyter notebooks for your project
├── EDA.ipynb # Exploratory data analysis notebook
├── Model.ipynb # Model training and evaluation notebook

REPORT # Report for your project
├── simple_report.tex # Simple report template using Latex
├── reference.bib # Reference file for your report
├── report.pdf # Compiled report in PDF format

environment.yml # Conda environment file for your project
```

### Suggested workflow

Main thing to keep in mind is your should keep Notebook as visualisation tools instead of your main code base. The main code base should be in the `src` folder. This will allow you to keep your code clean and organized. You can do this by coding your initial code in the notebook and then save your code as a Python file in the `src` folder. You can then import the functions from the `src` folder into your notebook and use them to run your experiments. Here are my suggested workflow:

#### For individual project (Or up to 2 peoples)
1. Duplicate this repository to your own GitHub account.
2. Clone the repository to your local machine.
3. Set up the Conda environment using the `environment.yml` file.

4. Collect your data and place it in the `data` folder. You can create subfolders like `raw`, `processed`, `interim`, and `final` to organize your data. 

5. Start coding in the `src` folder. Use Git to track your changes and commit your code regularly.
6. Use the `notebooks` folder for exploratory data analysis and model training.
7. Use the `report` folder to write your report using Latex. Or you can use other tools like Overleaf or Google Docs to write your report.
8. Once you are done with your project, you can push your code to GitHub and share it with your peers or submit it to your university.

#### For group project (More than 2 peoples)
1. Create a new repository on GitHub and invite your team members to collaborate.
2. Clone the repository to your local machine. Each team member should clone the repository to their own machine.
3. Set up the Conda environment using the `environment.yml` file. Share the environment file with your team members so they can set up the same environment.
4. Collect your data and place it in the `data` folder. You can create subfolders like `raw`, `processed`, `interim`, and `final` to organize your data.
5. Start coding in the `src` folder. Each team member can work on their own code and then merge their changes into the main branch using Git.
6. Use the `notebooks` folder for exploratory data analysis and model training. Each team membe should create their own notebook and share it with the team. Keep a ``main.ipynb`` notebook for the final model training and evaluation for submission.
7. During experimentation, you should use DagsHub or Weights & Biases to keep track of your experiments and results. This will allow each team member to see the results of their experiments and collaborate on the project. (Optional: You can also use DVC to keep track of your data and models if your project have multiple data processing and versioning is required.)
8. Use the `report` folder to write your report using Latex. Each team member can work on their own section of the report and then merge their changes into the main report using ```\subfile{}``` or ```\include{}```. You can also use Overleaf or Google Docs to collaborate on the report. (Recommend: Use Zotero, Endnote or Mendeley to keep track of your references and citations. You can export your references to a BibTeX file and include it in your report using the `reference.bib` file. This prevent overlapping of references and make it easier to manage your references.)

In most cases, you should use Git to track your changes and commit your code regularly. This will allow you to keep track of your changes and collaborate with your team members easily. You can also use GitHub Issues to keep track of your tasks and assign them to team members.

**TIPS**: For Group project, while not required, I recommend you to assign each members specific tasks or roles to work on (Ex: Data Engineer, Report Experiment Design, MLDevOps). Additionally when first start create dummy data and code to test the environment and ensure that everyone can run the code. This will allow team members to focus on their own tasks and not worry about the environment set up.

### Note on sharing notebooks & data.
Notebook files don't play well with Git and can cause merge conflicts. Thus I recommend you to ensure keeping a single notebook for final model training but use multiple notebooks for exploratory data analysis and model training. This will allow you to keep your notebooks clean and organized. You can also use JupyterLab to manage your notebooks and code files easily. If using Collab instead you want to include a link to the notebook in your GitHub repository and ensure that your team members have access to the notebook or add environment installation code in the notebook itself.

Some data files is private or too large to be shared on GitHub. In this case you can use DagsHub or Weights & Biases to share your data and models with your team members (They offer free s3 bucket so a good way to practice datastreaming as well). 

For smaller data files you can save it directly on Google Drive or Dropbox and share the link with your team members. However, be aware that this is not a good practices and can cause issues with loading data files in your code. If this approach is used, ensure to document the data loading process in your code and notebooks so that your team members can easily load the data files.
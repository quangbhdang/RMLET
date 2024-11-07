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
### Goal of this project
1. Create an environment where ML and AI student can quickly use to set up their project.
2. The project repo is clear, well defined and allows for good programming practice.
3. Give a high level of flexibility so it can be further developed into a more complex project.

### Why this GitHub repository was created
When starting in machine learning, and data science I was stumped as to where to begin my project. In most online material and even at my university the material is often skipped over the setting of the environment and the workspace of the project in favour of rapid prototyping and general theory.

While this might work for smaller projects or early introduction to machine learning concepts this quickly becomes a hurdle for more advanced courses and practice projects where complex functions and libraries need to be maintained. This often results in a janky way in which I have to keep track of parameters, experiments result in separate Excel sheets and multiple files just to keep track of my project and collaborate with my peers.

This repository was design base on my research on common good practice in managing and collaborating on machine learning environment. In addition, I have take care of keeping track of tools and package that I found beneficial during my time of learning AI.

### Selected pacakges
The following package was installed.

- Pandas
- Scikit-learn
- Numpy
- Matplotlib
- Seaborn

### The folder structure
Design to aid with keeping each component self contain.

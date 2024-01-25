# james-harding
Collection of memories on how to do whatever it is that I do. 


# Environment Setup
## Create Python Environment

**Create a pyton environment**
```
# Install pipenv
pip install pipenv --user

# Create project directory
mkdir ~/repo/vertexai
cd ~/repo/vertexai

# Create a new virtual environment and generate a Pipfile
pipenv --python 3.11.5

# Activate the virtual environment
pipenv shell

# Setup a kernel 
pipenv install setuptools ipykernel

# Install kernel (Google Cloud Vertex AI, TF and Pytorch)
python -m ipykernel install --user --name=vertexai
```

## Setup Git 

```
git config --global user.name "First Last"
git config --global user.email "somebody@home.com"
```


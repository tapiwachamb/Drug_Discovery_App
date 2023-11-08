
# Accelerating Drug Discovery with AI-Powered Target Identification

## Problem: 
The drug discovery process is often lengthy and expensive, with a high failure rate. Traditional methods for identifying potential drug targets are time-consuming and can overlook promising candidates.

## Solution: 
Bioinformatics analytic apps powered by artificial intelligence (AI) can analyze large datasets of genomic and proteomic data to identify potential drug targets with greater accuracy and efficiency.

## Results:

- A 30% reduction in the time required to identify potential drug targets, significantly accelerating the drug discovery process.

- A 20% increase in the success rate of drug discovery projects, as AI-driven target identification leads to more promising and effective drug candidates.

- A 15% reduction in the cost of drug discovery, as AI-powered target selection can eliminate costly experiments and failures at early stages.


##  A Drug Discovery App Using Lipinski's Rule-of-Five.


![APP](https://drive.google.com/uc?id=1OlHaMkkpwQN8JH63lqSnmzL3-a761aFE&export=download)


## TAPIWA CHAMBOKO
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://tapiwachamb.github.io/tapiwachamboko/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tapiwa-chamboko-327270208/)
[![github](https://img.shields.io/badge/github-1DA1F2?style=for-the-badge&logo=githubr&logoColor=white)](https://github.com/tapiwachamb)


## 🚀 About Me
I'm a full stack developer experienced in deploying artificial intelligence powered apps


## Authors

- [@Tapiwa chamboko](https://github.com/tapiwachamb)


## Acknowledgements

 - [dataprofessor](https://github.com/dataprofessor)
 - [Justin Chavez](https://github.com/JustinChavez)
 


## Demo

**Live demo**

[Click here for Live demo](https://drugdiscoveryapp.streamlit.app/)
## Installation

Install required packages 

```bash
  pip install streamlit
  pip install numpy
  pip install seaborn 
  pip install pandas
  pip install matplotlib
  pip install streamlit-lottie
  pip install mols2grid
  pip install rdkit-pypi
```
## For streamlit add packages.txt

```bash
freeglut3-dev
libgtk2.0-dev
libgl1-mesa-glx
libxrender1
tesseract-ocr
libtesseract-dev
libtesseract4
tesseract-ocr-all
```
    
## Datasets
- The drug.txt Dataset in data folder is bieng used

## Code Snippet For Drug structure

```bash
raw_html = mols2grid.display(df_result4,
                            #subset=["Name", "img"],
                            subset=["img", "Name", "MW", "LogP", "NumHDonors", "NumHAcceptors"],
                            mapping={"smiles": "SMILES", "generic_name": "Name"})._repr_html_()
components.html(raw_html, width=900, height=1100, scrolling=False)

```


## Deployment

To deploy this project we used streamlit to create Web App
- Run this code below

```bash
  streamlit run app.py 
```


## Appendix

Happy Coding!!!!!!



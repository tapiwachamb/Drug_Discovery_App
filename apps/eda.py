import mols2grid
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from rdkit import Chem
from rdkit.Chem.Descriptors import ExactMolWt, MolLogP, NumHDonors, NumHAcceptors

def app():
    st.title("Drug Discovery")


    @st.cache_data
    def download_dataset():
        """Loads once then cached for subsequent runs"""
        df = pd.read_csv(
            "data/drugs.txt", sep="\t"
        ).dropna()
        return df
#https://www.cureffi.org/wp-content/uploads/2013/10/drugs.txt
# Calculate descriptors
    def calc_mw(smiles_string):
        """Given a smiles string (ex. C1CCCCC1), calculate and return the molecular weight"""
        mol = Chem.MolFromSmiles(smiles_string)
        return ExactMolWt(mol)

    def calc_logp(smiles_string):
        """Given a smiles string (ex. C1CCCCC1), calculate and return the LogP"""
        mol = Chem.MolFromSmiles(smiles_string)
        return MolLogP(mol)

    def calc_NumHDonors(smiles_string):
        """Given a smiles string (ex. C1CCCCC1), calculate and return the NumHDonors"""
        mol = Chem.MolFromSmiles(smiles_string)
        return NumHDonors(mol)

    def calc_NumHAcceptors(smiles_string):
        """Given a smiles string (ex. C1CCCCC1), calculate and return the NumHAcceptors"""
        mol = Chem.MolFromSmiles(smiles_string)
        return NumHAcceptors(mol)


# Copy the dataset so any changes are not applied to the original cached version
    df = download_dataset().copy()
    df["SMILES"] = df["smiles"]  # Create a "SMILES" column
    df["Name"] = df["generic_name"]  # Create a "Name" column
    df["MW"] = df.apply(lambda x: calc_mw(x["smiles"]), axis=1)
    df["LogP"] = df.apply(lambda x: calc_logp(x["smiles"]), axis=1)
    df["NumHDonors"] = df.apply(lambda x: calc_NumHDonors(x["smiles"]), axis=1)
    df["NumHAcceptors"] = df.apply(lambda x: calc_NumHAcceptors(x["smiles"]), axis=1)


# Sidebar panel
    st.sidebar.header('Set parameters')
    st.sidebar.write('*Note: Display compounds having values less than the following thresholds*')
    weight_cutoff = st.sidebar.slider(
        label="Molecular weight",
        min_value=0,
        max_value=1000,
        value=500,
        step=10,
    )
    logp_cutoff = st.sidebar.slider(
        label="LogP",
        min_value=-10,
        max_value=10,
        value=-3,
        step=1,
    )
    NumHDonors_cutoff = st.sidebar.slider(
        label="NumHDonors",
        min_value=0,
        max_value=15,
        value=6,
        step=1,
    )
    NumHAcceptors_cutoff = st.sidebar.slider(
        label="NumHAcceptors",
        min_value=0,
        max_value=20,
        value=8,
        step=1,
    )

    df_result = df[df["MW"] < weight_cutoff]
    df_result2 = df_result[df_result["LogP"] < logp_cutoff]
    df_result3 = df_result2[df_result2["NumHDonors"] < NumHDonors_cutoff]
    df_result4 = df_result3[df_result3["NumHAcceptors"] < NumHAcceptors_cutoff]

   # st.write(df_result4.shape)
    st.write(df_result4)
    #st.write("**Structure**")

    st.markdown("""
                ### Structure
""")

    


    raw_html = mols2grid.display(df_result4,
                                subset=["img", "Name", "MW", "LogP", "NumHDonors", "NumHAcceptors"],
                                mapping={"smiles": "SMILES", "generic_name": "Name"})._repr_html_()
    components.html(raw_html, width=900, height=1100, scrolling=False)

    



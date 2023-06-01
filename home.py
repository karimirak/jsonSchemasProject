import database as db
import pageConfig
import streamlit as st
import json
import pandas as pd

def main():
    pageConfig.main()

    # Create_DB if not exist: Projet Config
    collections = db.DB_CONFIG.list_collection_names()
    if not collections:
        db.create_DB('Proj_Config')

    # Load Schema, otherwise, add it to Proj_Config
    schema = db.get_collection(db=db.DB_CONFIG, collection='schema')
    if not schema:
        with open('schema.json', 'r') as file:
            json_schema = [json.load(file)]
        schema = db.create_schema(db.DB_CONFIG, json_schema)

    df_schema = pd.DataFrame(schema)
    st.dataframe(df_schema)

if __name__ == "__main__":
    main()
import streamlit as st
import streamlit.components.v1 as components
import json

def main():
    st.set_page_config(
        page_title="Project...",
        page_icon=":scroll:",
        layout='wide'
    )
    load_css()
    load_js()

def load_css():
    st.markdown("""
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" 
                rel="stylesheet" 
                integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" 
                crossorigin="anonymous">
                """,
                unsafe_allow_html=True
                )
    st.markdown(
        "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css'>",
        unsafe_allow_html=True)

def load_js():
    st.markdown("""
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" 
       integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" 
       crossorigin="anonymous"></script>
       """,
        unsafe_allow_html=True
        )

    # methode 2
    jsoneditor_bundle = "https://cdn.jsdelivr.net/npm/@json-editor/json-editor@latest/dist/jsoneditor.min.js"
    components.html(
        f"""
            <script src="{jsoneditor_bundle}"></script>
            <div id="jsoneditor" style="height: 600px;"></div>
            <button onclick="loadJSON()">Load JSON</button>
            <script>
                function loadJSON() {{
                    console.log('test méthode 1')
                    const element = document.getElementById('jsoneditor');
                    const editor = new JSONEditor(element, options);
                    JSONEditor.defaults.options.theme = 'bootstrap4';

                }}
            </script>
            """
    )

    st.markdown("""
       <script src="https://cdn.jsdelivr.net/npm/@json-editor/json-editor@latest/dist/jsoneditor.min.js"></script>
       <div id="jsoneditor" style="height: 600px;"></div>
       <button onclick="loadJSON()">Load JSON</button>
            <script>
                function loadJSON() {{
                    console.log('test méthode 2')
                    const element = document.getElementById('jsoneditor');
                    const editor = new JSONEditor(element, options);
                    JSONEditor.defaults.options.theme = 'bootstrap4';
                    
                }}
            </script>
       """,
        unsafe_allow_html=True
        )




    with open('schema.json', 'r') as file:
        try:
            json_data = json.load(file)
            st.json(json_data)
        except json.JSONDecodeError:
            st.error("Invalid JSON file. Please provide a valid JSON file.")
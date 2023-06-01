import streamlit as st
import pageConfig
import database as db


def main():
    pageConfig.main()

    # Projetct
    projects = db.get_projects()

    st.header('Projects')
    for project in projects:
        col1, col2, buff = st.columns((1, 1, 6))
        col1.write(project)

        with buff:
            st.button(
                '🗑️',
                key=project,
                on_click=delete_project,
                args={project}
            )

def delete_project(project):
    db.drop_collections(project)


if __name__ == "__main__":
    main()
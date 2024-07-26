# Un script Python pour Streamlit qui utilise 'rembg' pour retirer l'arrière-plan d'une image.

from datetime import datetime, UTC
from io import BytesIO

import streamlit as st
from PIL import Image
from pydantic import FilePath
from rembg import remove

from src.config import settings


st.set_page_config(
    page_title=settings.APP_TITLE,
    initial_sidebar_state="collapsed",
    page_icon="random", layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title(body=settings.APP_TITLE)
st.write("## Retirer l'arrière-plan d'une image avec 'rembg'")
st.write("Uploader une image pour retirer l'arrière-plan avec 'rembg'")
st.sidebar.write("## Uploader")

first_column, second_column = st.columns(spec=settings.DEFAULT_PAGE_COLUMN)


def convert_image(image: FilePath):
    buf = BytesIO()
    image.save(buf, format='PNG')
    byte_io = buf.getvalue()

    return byte_io


def display_original_image(original_image: FilePath):
    first_column.write("Image originale")
    first_column.image(original_image)


def display_new_image(new_image: FilePath):
    remove_bg_img = remove(data=new_image)
    second_column.write("Image détourée")
    second_column.image(remove_bg_img)


def download_btn():
    st.download_button(
        label="Télécherger l'image",
        data=convert_image(image),
        file_name=f"result-{datetime.now(tz=UTC).timestamp()}.png",
        mime="image/png"
    )


def fix_image(image: FilePath = None):
    image = Image.open(upload_image)
    display_original_image(image)
    display_new_image(image)

    st.sidebar.markdown("\n")
    download_btn()


upload_image = st.sidebar.file_uploader(label="Choisissez une image", type=list(settings.IMAGE_TYPE))

if upload_image is not None:
    fix_image(image=upload_image)
else:
    pass

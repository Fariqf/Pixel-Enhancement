import streamlit as st
import replicate
import os
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("REPLICATE_API_TOKEN")  # Use the correct environment variable name

def enhance_image(img_path):
    # Set the API key as an environment variable
    os.environ["REPLICATE_API_TOKEN"] = API_KEY

    output = replicate.run(
        "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3",
        input={"img": open(img_path, "rb")}
    )
    return output

def main():
    st.title("Pixel Enhancement App")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Enhancing...")

        # Enhance image
        enhanced_image = enhance_image(uploaded_file.name)

        # Display enhanced image
        st.image(enhanced_image, caption="Enhanced Image.", use_column_width=True)

if __name__ == "__main__":
    main()




# import replicate
# from dotenv import load_dotenv
# load_dotenv()
# output = replicate.run(
#     "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3",
#     input={"img": open("images.jpg", "rb")}
# )
# print(output)

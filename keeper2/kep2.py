import os
import streamlit as st

# Function to get the list of files in a folder
def get_files_in_folder(folder_path):
    files = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            files.append(file_name)
    return files

# Main app
def main():
    st.title("โฟลเดอร์มองไฟล์ที่เก็บ")
    st.text("โปรดใส่ Path:")
    folder_path = st.text_input("", key="folder_path_input")

    if st.button("ส่งข้อมูล"):
        if not os.path.isdir(folder_path):
            st.error("Invalid folder path. Please provide a valid folder path.")
        else:
            files = get_files_in_folder(folder_path)
            if len(files) == 0:
                st.info("No files found in the specified folder.")
            else:
                st.info(f"Found {len(files)} files in the folder:")
                for file_name in files:
                    file_path = os.path.join(folder_path, file_name)
                    st.markdown(f"[{file_name}]({file_path})")

# Run the app
if __name__ == "__main__":
    main()

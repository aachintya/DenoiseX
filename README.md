# DenoiseX
Dim Light Image Enhancement

[Link to Google Collab](https://colab.research.google.com/drive/1HZsw3dJkc3qFsJtfoDLhRQD6ePiDPA7U?usp=sharing)

[Deployed Link](http://aachintya.streamlit.app/)
## 🚀 Features

- Upload low-light images in `.jpg`, `.jpeg`, or `.png` formats  
- Enhances images using a TensorFlow denoising model  
- View side-by-side before and after results  
- Download the enhanced image  

---

## 📦 Setup

### 1. Create and activate a virtual environment

```bash
# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment:
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate


# 2. Install dependencies

pip install -r requirements.txt


#3 Run the app

streamlit run streamlit_app.py


# 📁 Project Structure

.
├── .venv/                  # Virtual environment (optional, not pushed to Git)
├── streamlit_app.py        # Main application script
├── denoising_model.h5      # Pre-trained TensorFlow model (user-provided)
├── requirements.txt        # Dependency list
└── README.md               # This file






# DenoiseX
Dim Light Image Enhancement

[Deployed Link](http://aachintya.streamlit.app/) 
> Note: This model was an older version without U-Net Architecture and Attention Mechanisms

## 🚀 Features
- Upload low-light images in `.jpg`, `.jpeg`, or `.png` formats  
- Enhances images using a TensorFlow denoising model  
- View side-by-side before and after results  
- Download the enhanced image  

## 📦 Setup

Follow these steps to set up and run the Low-Light Image Enhancer app:

### ⚠️ Prerequisite: Install Python 3.11 (macOS)

TensorFlow is not currently compatible with Python 3.12 or 3.13. Please install Python 3.11 first:

```bash
brew install python@3.11
```

### Installation Steps

1. **Create and activate a virtual environment**
   ```bash
   # Create a virtual environment using Python 3.11
   /opt/homebrew/bin/python3.11 -m venv venv_tf
   
   # Activate the virtual environment
   source venv_tf/bin/activate
   ```

2. **Download the pre-trained model**  
   Download the model file (denoising_model.h5) from Google Drive:  
   [🔗 Download Model](https://drive.google.com/file/d/16G5xIEWgRQJ0GKabQkEusmIGXFJs1X1S/view?usp=sharing)  
   
   Place the downloaded file in the same directory as streamlit_app.py.

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Upload your image**  
   Upload a .jpg, .jpeg, or .png low-light image using the file uploader in the app interface.
   The model will enhance it, and you'll be able to view and download the result.

## 📁 Ideal Project Structure

```
.
├── .venv/                          # Virtual environment (optional, not pushed to Git)
├── streamlit_app.py                # Main application script
├── best_low_light_model.keras      # Pre-trained TensorFlow model (user-provided)
├── requirements.txt                # Dependency list
└── README.md                       # This file
```

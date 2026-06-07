# 1. Clone repository
git clone https://github.com/kalpo07/ml-projects-portfolio.git

# 2. Navigate to project
cd <your local path>/ml-projects-portfolio/multimodal-hate-speech-detector

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment (choose one based on OS)
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 5. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 6. Verify FFmpeg
ffmpeg -version

# 7. Start server (KEEP THIS TERMINAL OPEN)
python -m uvicorn app.main:app --reload

# In a NEW terminal window:

# 8. Navigate to project again
cd <your local path>/ml-projects-portfolio/multimodal-hate-speech-detector

# 9. Activate virtual environment
.\venv\Scripts\Activate.ps1  # or your OS version

# 10. Run tests
pytest -q

# 11. Verify in browser
# Open http://127.0.0.1:8000/
# Open http://127.0.0.1:8000/docs
# Open http://127.0.0.1:8000/text/health
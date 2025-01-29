**Resume ATS Score Checker**

This Streamlit application helps you evaluate how well your resume aligns with a specific job description using the Gemini Pro model from Google Generative AI. 

**Features:**

* **PDF Upload:** Upload your resume in PDF format.
* **Job Description Input:** Enter the job description text directly into the app.
* **AI-Powered Analysis:** The app utilizes the Gemini Pro model to analyze the resume and job description.
* **Comprehensive Feedback:** Receive detailed feedback on:
    * **ATS Score:** An overall score indicating the resume's suitability for the ATS.
    * **Strengths:** Areas where your resume excels in matching the job description.
    * **Weaknesses:** Areas where your resume lacks relevant keywords or information.
    * **Improvements:** Suggestions on how to improve your resume to increase its chances of passing through an ATS.
    * **Suggested Companies:** (Optional) Based on your resume and the job description, the app might suggest relevant companies near your location.

**Getting Started:**

1. **Install Requirements:**
   ```bash
   pip install streamlit PyPDF2 google-generativeai dotenv
   ```

2. **Create a `.env` file:**
   * Create a file named `.env` in the same directory as the script.
   * Add the following line to the `.env` file, replacing `YOUR_API_KEY` with your actual Google Cloud API key:
     ```
     GOOGLE_API_KEY=YOUR_API_KEY
     ```

3. **Run the App:**
   ```bash
   streamlit run app.py 
   ```
   or
   ```bash
    python -m streamlit run app.py
   ```

**Disclaimer:**

* This app provides an AI-generated assessment. 
* The accuracy of the ATS score and feedback may vary depending on the complexity of the job description and the quality of the resume.
* Always review and refine your resume based on your own professional judgment and career goals.

**Note:**

* This README assumes you have a basic understanding of Streamlit, Python, and how to obtain a Google Cloud API key. 

I hope this README provides a helpful overview of the Resume ATS Score Checker app!
****

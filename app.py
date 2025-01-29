import dotenv
import streamlit as st
import PyPDF2 as pdf
import google.generativeai as genai
import os

# load the dotenv
dotenv.load_dotenv()

# configure the gemini model

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = pdf.PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text()
    return text


def generate_ats_score(resume_text, jd_text):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Analyze this resume against the given job description and provide an ATS score out of 100.
    Also provide specific feedback on matching keywords and missing qualifications.

    Job Description:
    {jd_text}

    Resume:
    {resume_text}

    Format your response as:
    Score: /100
    Feedback:
    - Strengths: (bullet points)
    - Weaknesses: (bullet points)
    - improvements (bullet points)
    - suggested comapnies near his location: (bullet points)
    """

    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("Resume ATS Score Checker 🔍")
    st.write("This tool helps you evaluate the alignment between a resume and a job description using the Relevent Generative AI model.")

    resume_pdf = st.file_uploader("Upload Resumt [PDF]", type=["pdf"])
    jd_text = st.text_area("Enter your Job Description here", height=300)

    if st.button("Analyse Your Resume"):
        if resume_pdf and jd_text:
            with st.spinner("analyse your resume..."):
                # extract the text from the resume pdf and getting the results
                resume_text = extract_text_from_pdf(resume_pdf)
                # getting the ats score from the model
                analysis  = generate_ats_score(resume_text, jd_text)

                st.subheader("Analysing Result")
                st.write(analysis)
        else:
            st.error("Please upload a resume and enter your job description.")

if __name__ == "__main__":
    main()
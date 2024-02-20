from setuptools import find_packages,setup
setup(name="Bullet Point Generator",
      version="0.0.1",
      author="Kunal Saurabh",
      author_email="kunal.cimfr20@gmail.com",
      install_requires=["openai","langchain","streamlit","python-dotenv","pyPDF2","whisper","huggingsound","pytube"],
      packages=find_packages()
)
# translator-app-be
Here’s how to do it step by step:

1️⃣ Remove old venv (optional but recommended)

Since the old venv points to wrong paths:

rm -r venv


or just delete the venv folder from Explorer.

2️⃣ Create a new virtual environment

Inside your new backend folder:

python -m venv venv


This creates a new venv in translator-app-be.

3️⃣ Activate the new virtual environment

On Windows PowerShell:

venv\Scripts\Activate.ps1


You should see (venv) in the terminal prompt.

4️⃣ Install dependencies

Now install packages from requirements.txt:

//pip install --upgrade pip
python -m pip install --upgrade pip

pip install -r requirements.txt   --> this one is fine to run if not use below commnads manually to run one by one.


If requirements.txt is missing some packages, you can install manually:

pip install deep-translator
pip install gtts
pip install python-multipart

pip install fastapi uvicorn pydub speechrecognition requests

This should now work without the “Unable to create process” error.

5️⃣ Run your backend
uvicorn app:app --reload


Check that everything runs fine.

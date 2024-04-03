import os

# Clone the CodeFormer repository
os.system("git clone https://github.com/sczhou/CodeFormer")
os.chdir("CodeFormer")

# Create a new Anaconda environment
os.system("conda create -n codeformer python=3.8 -y")
os.system("conda activate codeformer")

# Install Python dependencies
os.system("pip3 install -r requirements.txt")
os.system("python basicsr/setup.py develop")

# Install dlib (Optional)
os.system("conda install -c conda-forge dlib")

print("Setup completed. You can now run CodeFormer.")

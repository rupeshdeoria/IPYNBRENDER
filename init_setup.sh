export _VERSION_=3.8
echo [$(date)]: "START"
echo [$(date)]: "Creating conda env"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "installing dev requirments"
pip install -r requirments_dev.txt
echo [$(date)]: "END"

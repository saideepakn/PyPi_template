echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.10" #change py version as per your need
conda create --prefix ./env python=3.10 -y
echo [$(date)]: "Activate Now"
source activate ./env
#echo [$(date)]: "installing dev requirements"
pip install -r requirements_dev.txt
#echo [$(date)]: "END"
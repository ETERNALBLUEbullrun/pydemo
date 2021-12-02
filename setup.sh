apt-get update && apt-get install python
pip install virtualenv
pip install --upgrade pip
pip install --upgrade $(pip list --outdated | awk '{print $1}' | tr '\n' ' ')


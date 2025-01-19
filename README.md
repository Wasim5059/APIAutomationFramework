# python API Automation Framework
# Hybrid Custom Framework to test the REST APIs

### Tech Stack
1. python 3.11
2. Requests - HTTP Requests
3. PyTest - Testing Framework
4. Reporting - Allure Report, PyTest HTML
5. Test Data - CSV, Excel, JSON
6. Parallel Execution - x distribute

### How to install Package
pip  install requests pytest pytes-html faker allure-pytest jsonschema

## To Freeze your package version
pip freeze > requirements.txt ''

## To Install the Freeze version
pip install -r requirements.txt

## To Install the pytest -xdist
pip install pytest-xdist

## to run the -xdist
pytest -n auto filename -s -v

## To work on the excel or csv file
##install the openpyxl
pip install openpyxl
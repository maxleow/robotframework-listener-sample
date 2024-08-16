*** Settings ***
Library    ../../lib/AutoPopupHandler.py

*** Keywords ***
login
    [Arguments]    ${name}    ${password}
    Log    ${name} ${password}

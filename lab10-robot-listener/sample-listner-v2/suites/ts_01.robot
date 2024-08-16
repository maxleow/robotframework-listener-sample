*** Settings ***
Resource    ../case/pulse/dummy1.resource
Resource    ../case/cla/dummy1.resource

*** Test Cases ***
TC_001
    login    smith    john88
    login 2


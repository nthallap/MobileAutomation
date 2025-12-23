*** Settings ***
Suite Setup     test suite


*** Keywords ***
test suite
    Log    I am suite setup

new keyword
    Log  Hellow world



*** Test Cases ***

Test1
    [Tags]   smoke1
    Log    hello world

Test2
    [Tags]   smoke2
    Log    hello world

Test3
    [Tags]   smoke3
    Log    hello world
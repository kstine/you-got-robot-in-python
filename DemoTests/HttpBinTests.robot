*** Comments ***
Don't forget to run docker container...
robot -d Results -L TRACE DemoTests/HttpBinTests.robot


*** Settings ***
Documentation       Example for scripts used as Robot Framework libaries

Library             Collections
Library             RequestsLibrary
Library             ../CustomLibraries/HttpBinLibrary/HttpBinLibrary.py

Suite Setup         Create HTTP Bin Session
Suite Teardown      Delete All Sessions


*** Variables ***
${EXPECTED_SERVER_INFORMATION}      gunicorn/19.9.0
${DELAY}                            2
${EXPECTED_URL}                     http://localhost:8086/delay/${DELAY}


*** Test Cases ***
Verify Get Request Header Contains Server Information
    [Documentation]    Calls a get method and verifies the server information
    ${response}    Get HTTP Method
    ${actual_server_information}    Get From Dictionary    ${response.headers}    Server
    Should Be Equal    ${EXPECTED_SERVER_INFORMATION}    ${actual_server_information}

Verify Post Dynamic Data Contains Url
    [Documentation]    Calls the post dynamic data and verifies the url key from the response
    ${response}    Post Dynamic Data    ${DELAY}
    ${actual_url}    Get From Dictionary    ${response.json()}    url
    Should Be Equal    ${EXPECTED_URL}    ${actual_url}

Verify Alias
    [Documentation]    Verify that session created by other library exists
    ${expected_alias}    HttpBinLibrary.Get HTTP Bin Alias
    ${is_alias}  RequestsLibrary.Session Exists    ${expected_alias}
    Should Be True    ${is_alias}

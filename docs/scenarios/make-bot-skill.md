# Miscellanous Bugs
| Date | Test Result|
|:-----|:-----------|
|4/28|[1](https://github.com/microsoft/BotFramework-Composer/issues/7456)|

# Dotnet Webapp scenarios
## Scenario 1: I want a local web app bot and I want to connect to a local web app skill

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26 | Fail| [1](https://github.com/microsoft/BotFramework-Composer/issues/7383) 
|4/27| Pass*| [1](https://github.com/microsoft/BotFramework-Composer/issues/7422)
| 4/28| Pass||

- create empty bot project for the skill
- add some echo trigger
- create provisioning profile & publish
- share bot as skill & publish
- copy manifest url
- create empty bot project for parent
- add -> open existing skill
- add trigger to connect to skill
- add app id & pw to parent and skill
- update parent app settings to have `["*"]` under skills -> allowedCallers
- start bots & send message



## Scenario 3: I want a local web app bot and I want to connect to a remote web app skill via intent recognition

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26| Pass||
|4/27| Pass||
|4/28|Pass||

- create empty bot project for the skill
- add some echo trigger
- create provisioning profile & publish
- share bot as skill & publish
- copy manifest url
- create empty bot project for parent
- add -> open existing skill
- add trigger to connect to skill
- add app id & pw to parent and skils
- update parent app settings to have `["*"]` under skills -> allowedCallers
- start bots 
- spin up ngrok with port replacement same as parent 
- replace parent skill host endpoint w/ ngrok url
- open emulator over the ngrok url
- test


## Scenario 5: I want a deployed web app  bot and I want to connect to a remote web app  skill via intent recognition

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26|Pass||
|4/27| Pass||
|4/28| Pass*| [1](https://github.com/microsoft/BotFramework-Composer/issues/7461)

- create empty bot project for the skill
- add some echo trigger
- create provisioning profile & publish
- share bot as skill & publish
- copy manifest url
- create empty bot project for parent
- add -> open existing skill
- add trigger to connect to skill via intent recognition
- add app id & pw to parent and skill
- update parent app settings to have `["*"]` under skills -> allowedCallers
- test bots in azure portal via test in web chat

Non P0 scenario ~~## Scenario 6: I want a deployed web app  bot and I want to connect to a remote skill chaining with web app via intent recognition ~~

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27|Fail|[1](https://github.com/microsoft/BotFramework-Composer/issues/7439)|

# Node Webapp scenarios
## Scenario 1: I want a local web app bot and I want to connect to a local web app  skill via manual connection to the skill

| Date | Test Result| Issues|
|:-----|:-----------|:------|


## Scenario 2: I want a web app  local bot and I want to connect to a local web app  skill via intent recognition wiring


| Date | Test Result| Issues|
|:-----|:-----------|:------|


## Scenario 3: I want a local web app bot and I want to connect to a remote web app skill via intent recognition
- Will need ngrok for skill host endpoint


| Date | Test Result| Issues|
|:-----|:-----------|:------|



## Scenario 5: I want a deployed web app  bot and I want to connect to a remote web app  skill via intent recognition

| Date | Test Result| Issues|
|:-----|:-----------|:------|


## Scenario 6: I want a deployed web app  bot and I want to connect to a remote skill chaining with web app via intent recognition 


| Date | Test Result| Issues|
|:-----|:-----------|:------|



# Dotnet Function Scenarios
## Scenario 1: I want a function app bot and I want to connect to a local function app  skill via manual connection to the skill


| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) | 


## Scenario 2: I want a function local bot and I want to connect to a local function skill via intent recognition wiring


| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) | 


## Scenario 3: I want a function app bot and I want to connect to a remote function skill via intent recognition


| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) | 

## Scenario 5: I want a deployed function  bot and I want to connect to a remote function  skill via intent recognition

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) | 

## Scenario 6: I want a deployed function bot and I want to connect to a remote skill chaining with function via intent recognition 
| Date | Test Result| Issues|
|:-----|:-----------|:------|


# Node Function Scenarios
## Scenario 1: I want a function app bot and I want to connect to a local function app  skill via manual connection to the skill


| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) [2](https://github.com/microsoft/BotFramework-Composer/issues/7433)| 


## Scenario 2: I want a function local bot and I want to connect to a local function skill via intent recognition wiring


| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) [2](https://github.com/microsoft/BotFramework-Composer/issues/7433)| 


## Scenario 3: I want a function app bot and I want to connect to a remote function skill via intent recognition


| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) [2](https://github.com/microsoft/BotFramework-Composer/issues/7433)| 

## Scenario 5: I want a deployed function  bot and I want to connect to a remote function  skill via intent recognition

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/27| **Blocked** | [1](https://github.com/microsoft/BotFramework-Composer/issues/7343) [2](https://github.com/microsoft/BotFramework-Composer/issues/7433)| 

## Scenario 6: I want a deployed function bot and I want to connect to a remote skill chaining with function via intent recognition 
| Date | Test Result| Issues|
|:-----|:-----------|:------|



# Web app & Function crossover


|  | .net web app parent| .net function parent | node web app parent | node function parent |
|:-----|:-----------|:------|:------|:------|
| .net web app skill| | | |
| .net function skill| | | |
| node web app skill| | | |
| node function skill| | | |


# Webapp scenarios
## Scenario 1: I want a local web app bot and I want to connect to a local web app  skill via manual connection to the skill
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Have the parent manually connect to the skill
- Start bots
- Test and should work

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26 | Fail| [1](https://github.com/microsoft/BotFramework-Composer/issues/7383) 


## Scenario 2: I want a web app  local bot and I want to connect to a local web app  skill via intent recognition wiring
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots
- Test and should work

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26 | Pass |  |


## Scenario 3: I want a local web app bot and I want to connect to a remote web app skill via intent recognition
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots
- Will need ngrok for skill host endpoint
- Test and should work

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26| Pass||


## Scenario 5: I want a deployed web app  bot and I want to connect to a remote web app  skill via intent recognition
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26|Pass||

## Scenario 6: I want a deployed web app  bot and I want to connect to a remote skill chaining with web app via intent recognition 
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots

| Date | Test Result| Issues|
|:-----|:-----------|:------|

# Function Scenarios
## Scenario 1: I want a function app bot and I want to connect to a local function app  skill via manual connection to the skill
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Have the parent manually connect to the skill
- Start bots
- Test and should work

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26 | Fail| [1](https://github.com/microsoft/BotFramework-Composer/issues/7383) 


## Scenario 2: I want a function local bot and I want to connect to a local function skill via intent recognition wiring
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots
- Test and should work

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26 | Pass |  |


## Scenario 3: I want a function app bot and I want to connect to a remote function skill via intent recognition
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots
- Will need ngrok for skill host endpoint
- Test and should work

| Date | Test Result| Issues|
|:-----|:-----------|:------|


## Scenario 5: I want a deployed function  bot and I want to connect to a remote function  skill via intent recognition
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots

| Date | Test Result| Issues|
|:-----|:-----------|:------|

## Scenario 6: I want a deployed function bot and I want to connect to a remote skill chaining with function via intent recognition 
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots

| Date | Test Result| Issues|
|:-----|:-----------|:------|

# Web app & Function crossover

## web app parent, function skill
| Date | Test Result| Issues|
|:-----|:-----------|:------|

## function parent, web app skill
| Date | Test Result| Issues|
|:-----|:-----------|:------|

## web app parent, function skill, web app skill 
| Date | Test Result| Issues|
|:-----|:-----------|:------|

## web app parent, web app skill, function skill
| Date | Test Result| Issues|
|:-----|:-----------|:------|

## function parent, function skill, web app skill
| Date | Test Result| Issues|
|:-----|:-----------|:------|

## function parent, web app skill, function skill
| Date | Test Result| Issues|
|:-----|:-----------|:------|

## Scenario 1: I want a local bot and I want to connect to a local skill via manual connection to the skill
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


## Scenario 2: I want a local bot and I want to connect to a local skill via intent recognition wiring
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots
- Will need ngrok for skill host endpoint
- Test and should work

| Date | Test Result| Issues|
|:-----|:-----------|:------|
|4/26 | Pass |  |


## Scenario 3: I want a local bot and I want to connect to a remote skill via intent recognition

| Date | Test Result| Issues|
|:-----|:-----------|:------|

## Scenario 4: I want a deployed bot and I want to connect to a remote skill via manual wiring

| Date | Test Result| Issues|
|:-----|:-----------|:------|

## Scenario 5: I want a deployed bot and I want to connect to a remote skill via intent recognition

| Date | Test Result| Issues|
|:-----|:-----------|:------|

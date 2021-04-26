## Scenario 1: I want a local bot and I want to connect to a local skill via manual connection to the skill
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Have the parent manually connect to the skill
- Start bots
- Test and should work


## Scenario 2: I want a local bot and I want to connect to a local skill via intent recognition wiring
- Make 2 bots via the templates
- In the parent, in the designer -> add -> open existing skill
- Add app IDs & Passwords to parent and skill
- Update parent manifest to allow all callers
- Start bots
- Test and should work

## Scenario 3: I want a local bot and I want to connect to a remote skill via manual connection to the skill
- Create, provision, and deploy a bot
- Make sure the skill also has the skill endpoint configured after deployment
- In the design window click the 3 dots -> share as skill
- Fill out forms
- go back to the publish window and click the "copy skill manifest url" -> save this for later
- create new local parent bot
- from design view click add -> connect to a remote skill
- enter manifest url saved earlier
- keep same LG keywords
- Go to bot settings
- make sure the skills -> allowedCallers's value is ["*"]
- add App id & PW to parent
- start parent
- send parent the message to connect to the skill

## Scenario 4: I want a local bot and I want to connect to a remote skill via intent recognition

## Scenario 5: I want a deployed bot and I want to connect to a remote skill via manual wiring

## Scenario 6: I want a deployed bot and I want to connect to a remote skill via intent recognition

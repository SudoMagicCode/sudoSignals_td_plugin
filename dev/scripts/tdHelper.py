popDialog = op.TDResources.op('popDialog')

def WarnNoProductId():
    buttons = ['Update', 'Cancel']

    # private function for dialog selection
    def dialogChoice(info):
        userText        = info.get('enteredText')
        details         = info.get('details')
        userButton      = info.get('button')

        if userButton == buttons[0]:
            print(userText)
            print(details)
            print(userButton)
        else:
            pass
    
    # opens the pop dialogue
    popDialog.OpenDefault(
        text    = "Woah there adventurer, you're missing a Signals ID",
        title   = "Missing Signals ID",
        callback = dialogChoice,
        details = op('tdHelper'),
        buttons = buttons,
        escButton = 2,
        enterButton = 1,
        escOnClickAway = True,
        textEntry = True
    )

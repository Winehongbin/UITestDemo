
ControlFocus("��","","Edit1")


WinWait("[CLASS:#32770]","",10)

ControlSetText("��","","Edit1",@ScriptDir&"\Email.xlsx")
Sleep(10000)


ControlClick("��","","Button1");
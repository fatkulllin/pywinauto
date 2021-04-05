from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import shutil
import os

def copy():
    localFolder = os.path.join('C:/Program Files/CSoft/tempFolderAcad')
    remoteFolder = os.path.join('//terminator/SAPR-PO/tempFolderAcad')
    liveFolder = os.path.exists(localFolder)

    if liveFolder == True:
        shutil.rmtree(localFolder)
        shutil.copytree(remoteFolder, localFolder)
    else:
        shutil.copytree(remoteFolder, localFolder)

    shutil.copy('//terminator/SAPR-PO/tempFolderAcad/patch_spds/temp/1/1.lic',
                'C:/Program Files/CSoft/СПДС GraphiCS 2021 x64 для AutoCAD/')
    
    print('Я закончил копирование')

def importAutocad():
    print('Открываю автокад')
    autocad = Application().start('"C:\Program Files\Autodesk\AutoCAD 2021\Acad.exe"')
    time.sleep(30)
    print('Нажимаю enter')
    send_keys('{ENTER}', with_spaces=True)
    time.sleep(30)
    print('Все закрыл иду дальше')
    os.system("TASKKILL /F /IM acad.exe")
    os.system("TASKKILL /F /IM AdskLicensingAgent.exe")
    time.sleep(5)

    #print(app.Импортпользовательскихнастроек.print_control_identifiers())
    # NewWindow = app.window(top_level_only=True, active_only=True)
    # NewWindow.AddressBandRoot.click_input()
    # NewWindow.AddressBandRoot.Edit.type_keys("C:\Program Files\CSoft\TempFolderAcad", with_spaces=True)

    print('Импорт пользователя')
    app = Application().start('"C:\Program Files\Autodesk\AutoCAD 2021\AdMigrator.exe" /i')
    address = app.Импортпользовательскихнастроек.child_window(class_name="Address Band Root").wrapper_object()
    address.click_input(coords=(5, 14))
    address.type_keys("C:\Program Files\CSoft\TempFolderAcad", with_spaces=True)
    send_keys('{ENTER}', with_spaces=True)
    app.Импортпользовательскихнастроек.Edit.type_keys("AutoCAD.zip", with_spaces=True)
    send_keys('{ENTER}', with_spaces=True)
    time.sleep(10)
    os.system("TASKKILL /F /IM AdMigrator.exe")

def crackSPDS():
    print('приступаем к спдс')
    spds = Application(backend="win32").start(r'C:\Program Files\CSoft\TempFolderAcad\patch_spds\patch_spds.bat /k',
                                             create_new_console=True, wait_for_idle=False)
    time.sleep(5)
    print('Нажимаю enter')
    send_keys('{ENTER}', with_spaces=True)
    time.sleep(5)
    print('Нажимаю enter')
    send_keys('{ENTER}', with_spaces=True)

def regWizard():
    print('перешёл к регвизард')
    RegWizard = Application().start('"C:\Program Files\CSoft\СПДС GraphiCS 2021 x64 для AutoCAD\RegWizard.exe"')
    time.sleep(2)
    send_keys('{DOWN}', with_spaces=True)
    time.sleep(2)
    print('Нажимаю enter')
    send_keys('{ENTER}', with_spaces=True)
    time.sleep(2)
    print('Нажимаю enter')
    send_keys('{ENTER}', with_spaces=True)
    time.sleep(2)
    print('Нажимаю enter')
    send_keys('{ENTER}', with_spaces=True)

def restart():
    os.system("shutdown /r /t 0")

copy();
time.sleep(5)
importAutocad()
time.sleep(5)
crackSPDS();
time.sleep(5)
regWizard();
time.sleep(5)
restart();
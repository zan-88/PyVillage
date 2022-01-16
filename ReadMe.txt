Thanks for downloading our YMCA Detector!
To get started, you'll have to follow a few steps. 
Please follow them closely, and if any steps fail, please re-read the instructions and try again.

1) The first, is install python. You may already have python installed on your computer.
You can check this by double clicking on the "Do I have Python?" file. 
    1.1) This is found in Installation/MACOS, or Installation/WINDOWS

2) If it spits out something along the lines of "Python 3.x.x" AND the second number is lower then 10, then proceed to the next step.
Otherwise, please go to this website, and download whichever version works for your machine:
https://www.python.org/downloads/release/python-397/ -- it is important you use 3.9.7 instead of 3.10.x, as 3.10 doesn't work yet

3) Next up, you'll need something called pip. If you already have pip, feel free to skip this step, otherwise follow along closely:
    3.1) If you're on macOS, open up Terminal, and if you're on Windows, open up Command Prompt.
    3.2) Type "cd" and then a space after, but don't press enter just yet.
    3.3) Drag the folder Installation/MACOS or Installation/WINDOWS into the Terminal/Command Prompt window, depending on which OS you use, and press enter.
    3.4) Drag the file "INSTALL PIP MACOS"/"INSTALL PIP WINDOWS" into the Terminal/Command Prompt window, and press enter.
        3.4.1) This may take a minute, so be patient.

4) Finally, you need to install a few packages. This is not the easiest, so you're going to want to follow these steps very carefully.
    4.1) If you're on macOS, open up Terminal. If you're on Windows, open up Command Prompt.
    4.2) You're going to want to type the letters "cd", and then add a space. Don't press enter just yet.
    4.3) Now, you need to drag the folder this file is contained in (PyVillage), into the Terminal/Command Prompt window, and then press enter.
    4.4) Now, hop into Installation/MACOS or Installation/WINDOWS, and drag MACOS or WINDOWS into the Terminal/Command Prompt window, and then press enter.
    4.5) If all went as planned, and it looks like everything got installed, congratulations, you're done, and can skip to step 5.
        Otherwise, continue to step 4.6.
    4.6) If something went wrong, it is likely because you are running the wrong version of python. Rerun the "Do I have python?" file, and it likely will not
        say "Python 3.x.x", with the first x being below 10. If that is the case, then you're going to want to google how to change python versions.
        If the first x is below 10, I have actually no idea, and am genuinely sorry you will not be able to use this. If you're determined to use it,
        please email petergelgor7@gmail.com, and I will be happy to help you out.

5) Now, drag either "Run MACOS" or "Run WINDOWS" into the Terminal/Command Prompt window, and press enter.
    5.1) You may get an error saying that terminal/command prompt doesn't have camera access, you will need to give it camera access to work. 
        5.1.1) If you're on macOS, you can do this by going to System Preferences > Security & Privacy > Privacy > Camera, and then clicking on the "Allow" button.
        5.1.1) If you're on Windows, you can do this by going to Control Panel > Security > Privacy > Camera, and then clicking on the "Allow" button.
    5.2) Finally, once that's done, you should repeat step 5, and it should work properly.

Enjoy!


TROUBLESHOOTING:
1) If the window after the main menu popped up, but nothing is showing, you'll need to follow these steps:
    1.1) Head into PyVillage/code/main.py
    1.2) Go to the line after all the imports, which is "cap = cv2.VideoCapture(0)"
    1.3) Change the number 0, to 1.
    1.4) Rerun the program, and if if doesn't work, keep increasing the number.
    1.5) If eventually it stops even loading and you get an error, you probably need to play with your camera settings.




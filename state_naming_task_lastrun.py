#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on April 30, 2025, at 12:33
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'state_naming_task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 960]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\josef\\OneDrive\\Desktop\\Filler Task for TOT Study\\state_naming_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Experiment loading, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('instruction_resp') is None:
        # initialise instruction_resp
        instruction_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instruction_resp',
        )
    if deviceManager.getDevice('instructions_resp_2') is None:
        # initialise instructions_resp_2
        instructions_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instructions_resp_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions_states_task" ---
    task_instructions = visual.TextStim(win=win, name='task_instructions',
        text='In this task, you will see a blank map of each U.S. state which will be displayed for 7 seconds. Your goal is to identify each state by providing a typed response within that 7 seconds. After identifying each U.S. state you will be presented with a blank map of various countries to label.\n\nThis task should take approximately 10 minutes to complete.\n\n\nPlease press "space" to begin this task.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instruction_resp = keyboard.Keyboard(deviceName='instruction_resp')
    
    # --- Initialize components for Routine "States_Naming_Task" ---
    stimuli_prompt = visual.TextStim(win=win, name='stimuli_prompt',
        text='What is the name of this U.S. State?',
        font='Arial',
        pos=(0, .4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    okay_state_pics = visual.ImageStim(
        win=win,
        name='okay_state_pics', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=True, size=(.6, .5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    us_state_response = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -.4), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='us_state_response',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "States_Naming_Task_2" ---
    stimuli_prompt_2 = visual.TextStim(win=win, name='stimuli_prompt_2',
        text='What is the name of this U.S. state?',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    wider_state_pics = visual.ImageStim(
        win=win,
        name='wider_state_pics', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.95, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    us_state_response_2 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.4), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='us_state_response_2',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "States_Naming_Task_3" ---
    stimuli_prompt_3 = visual.TextStim(win=win, name='stimuli_prompt_3',
        text='What is the name of this U.S. state?',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    taller_state_pics = visual.ImageStim(
        win=win,
        name='taller_state_pics', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.65),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    us_state_response_3 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.4), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='us_state_response_3',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "instructions_countries_task" ---
    task_instructions_2 = visual.TextStim(win=win, name='task_instructions_2',
        text='Now you will be identifying different countries. As with the previous task, you will have 7 seconds to type a response, and after 7 seconds have passed you will move onto the next country.\n\nPress "space" to begin.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instructions_resp_2 = keyboard.Keyboard(deviceName='instructions_resp_2')
    
    # --- Initialize components for Routine "Country_Naming_Task" ---
    stimuli_prompt_4 = visual.TextStim(win=win, name='stimuli_prompt_4',
        text='What is the name of this South American country?',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    country_response = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.4), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='country_response',
         depth=-1, autoLog=True,
    )
    okay_country_pics = visual.ImageStim(
        win=win,
        name='okay_country_pics', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.65),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "Country_Naming_Task_2" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='What is the name of this South American country?',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    tall_country_trials = visual.ImageStim(
        win=win,
        name='tall_country_trials', 
        image='south_america/Chile-Country-Outline.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(.22, .6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    textbox = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.6), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "Finish_Screen" ---
    text = visual.TextStim(win=win, name='text',
        text='You have now completed these two other tasks. Once this screen returns to the desktop, please notify the researcher that you have completed this part of the study.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instructions_states_task" ---
    # create an object to store info about Routine instructions_states_task
    instructions_states_task = data.Routine(
        name='instructions_states_task',
        components=[task_instructions, instruction_resp],
    )
    instructions_states_task.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instruction_resp
    instruction_resp.keys = []
    instruction_resp.rt = []
    _instruction_resp_allKeys = []
    # store start times for instructions_states_task
    instructions_states_task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_states_task.tStart = globalClock.getTime(format='float')
    instructions_states_task.status = STARTED
    thisExp.addData('instructions_states_task.started', instructions_states_task.tStart)
    instructions_states_task.maxDuration = None
    # keep track of which components have finished
    instructions_states_taskComponents = instructions_states_task.components
    for thisComponent in instructions_states_task.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_states_task" ---
    instructions_states_task.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_instructions* updates
        
        # if task_instructions is starting this frame...
        if task_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_instructions.frameNStart = frameN  # exact frame index
            task_instructions.tStart = t  # local t and not account for scr refresh
            task_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_instructions.started')
            # update status
            task_instructions.status = STARTED
            task_instructions.setAutoDraw(True)
        
        # if task_instructions is active this frame...
        if task_instructions.status == STARTED:
            # update params
            pass
        
        # *instruction_resp* updates
        waitOnFlip = False
        
        # if instruction_resp is starting this frame...
        if instruction_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_resp.frameNStart = frameN  # exact frame index
            instruction_resp.tStart = t  # local t and not account for scr refresh
            instruction_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_resp.started')
            # update status
            instruction_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruction_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruction_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_resp.status == STARTED and not waitOnFlip:
            theseKeys = instruction_resp.getKeys(keyList=["space"], ignoreKeys=["escape"], waitRelease=False)
            _instruction_resp_allKeys.extend(theseKeys)
            if len(_instruction_resp_allKeys):
                instruction_resp.keys = _instruction_resp_allKeys[-1].name  # just the last key pressed
                instruction_resp.rt = _instruction_resp_allKeys[-1].rt
                instruction_resp.duration = _instruction_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_states_task.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_states_task.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_states_task" ---
    for thisComponent in instructions_states_task.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_states_task
    instructions_states_task.tStop = globalClock.getTime(format='float')
    instructions_states_task.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_states_task.stopped', instructions_states_task.tStop)
    # check responses
    if instruction_resp.keys in ['', [], None]:  # No response was made
        instruction_resp.keys = None
    thisExp.addData('instruction_resp.keys',instruction_resp.keys)
    if instruction_resp.keys != None:  # we had a response
        thisExp.addData('instruction_resp.rt', instruction_resp.rt)
        thisExp.addData('instruction_resp.duration', instruction_resp.duration)
    thisExp.nextEntry()
    # the Routine "instructions_states_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    okay_states_trials = data.TrialHandler2(
        name='okay_states_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('states/loop_okay_states_trials.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(okay_states_trials)  # add the loop to the experiment
    thisOkay_states_trial = okay_states_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOkay_states_trial.rgb)
    if thisOkay_states_trial != None:
        for paramName in thisOkay_states_trial:
            globals()[paramName] = thisOkay_states_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisOkay_states_trial in okay_states_trials:
        currentLoop = okay_states_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisOkay_states_trial.rgb)
        if thisOkay_states_trial != None:
            for paramName in thisOkay_states_trial:
                globals()[paramName] = thisOkay_states_trial[paramName]
        
        # --- Prepare to start Routine "States_Naming_Task" ---
        # create an object to store info about Routine States_Naming_Task
        States_Naming_Task = data.Routine(
            name='States_Naming_Task',
            components=[stimuli_prompt, okay_state_pics, us_state_response],
        )
        States_Naming_Task.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        okay_state_pics.setOri(0.0)
        okay_state_pics.setImage(image_file)
        us_state_response.reset()
        # store start times for States_Naming_Task
        States_Naming_Task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        States_Naming_Task.tStart = globalClock.getTime(format='float')
        States_Naming_Task.status = STARTED
        thisExp.addData('States_Naming_Task.started', States_Naming_Task.tStart)
        States_Naming_Task.maxDuration = None
        # keep track of which components have finished
        States_Naming_TaskComponents = States_Naming_Task.components
        for thisComponent in States_Naming_Task.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "States_Naming_Task" ---
        # if trial has changed, end Routine now
        if isinstance(okay_states_trials, data.TrialHandler2) and thisOkay_states_trial.thisN != okay_states_trials.thisTrial.thisN:
            continueRoutine = False
        States_Naming_Task.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 7.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimuli_prompt* updates
            
            # if stimuli_prompt is starting this frame...
            if stimuli_prompt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stimuli_prompt.frameNStart = frameN  # exact frame index
                stimuli_prompt.tStart = t  # local t and not account for scr refresh
                stimuli_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimuli_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_prompt.started')
                # update status
                stimuli_prompt.status = STARTED
                stimuli_prompt.setAutoDraw(True)
            
            # if stimuli_prompt is active this frame...
            if stimuli_prompt.status == STARTED:
                # update params
                pass
            
            # if stimuli_prompt is stopping this frame...
            if stimuli_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimuli_prompt.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimuli_prompt.tStop = t  # not accounting for scr refresh
                    stimuli_prompt.tStopRefresh = tThisFlipGlobal  # on global time
                    stimuli_prompt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimuli_prompt.stopped')
                    # update status
                    stimuli_prompt.status = FINISHED
                    stimuli_prompt.setAutoDraw(False)
            
            # *okay_state_pics* updates
            
            # if okay_state_pics is starting this frame...
            if okay_state_pics.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                okay_state_pics.frameNStart = frameN  # exact frame index
                okay_state_pics.tStart = t  # local t and not account for scr refresh
                okay_state_pics.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(okay_state_pics, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'okay_state_pics.started')
                # update status
                okay_state_pics.status = STARTED
                okay_state_pics.setAutoDraw(True)
            
            # if okay_state_pics is active this frame...
            if okay_state_pics.status == STARTED:
                # update params
                pass
            
            # if okay_state_pics is stopping this frame...
            if okay_state_pics.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > okay_state_pics.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    okay_state_pics.tStop = t  # not accounting for scr refresh
                    okay_state_pics.tStopRefresh = tThisFlipGlobal  # on global time
                    okay_state_pics.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'okay_state_pics.stopped')
                    # update status
                    okay_state_pics.status = FINISHED
                    okay_state_pics.setAutoDraw(False)
            
            # *us_state_response* updates
            
            # if us_state_response is starting this frame...
            if us_state_response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                us_state_response.frameNStart = frameN  # exact frame index
                us_state_response.tStart = t  # local t and not account for scr refresh
                us_state_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(us_state_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'us_state_response.started')
                # update status
                us_state_response.status = STARTED
                us_state_response.setAutoDraw(True)
            
            # if us_state_response is active this frame...
            if us_state_response.status == STARTED:
                # update params
                pass
            
            # if us_state_response is stopping this frame...
            if us_state_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > us_state_response.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    us_state_response.tStop = t  # not accounting for scr refresh
                    us_state_response.tStopRefresh = tThisFlipGlobal  # on global time
                    us_state_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'us_state_response.stopped')
                    # update status
                    us_state_response.status = FINISHED
                    us_state_response.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                States_Naming_Task.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in States_Naming_Task.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "States_Naming_Task" ---
        for thisComponent in States_Naming_Task.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for States_Naming_Task
        States_Naming_Task.tStop = globalClock.getTime(format='float')
        States_Naming_Task.tStopRefresh = tThisFlipGlobal
        thisExp.addData('States_Naming_Task.stopped', States_Naming_Task.tStop)
        okay_states_trials.addData('us_state_response.text',us_state_response.text)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if States_Naming_Task.maxDurationReached:
            routineTimer.addTime(-States_Naming_Task.maxDuration)
        elif States_Naming_Task.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'okay_states_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    wider_states_trials = data.TrialHandler2(
        name='wider_states_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('states/loop_wider_states_trials.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(wider_states_trials)  # add the loop to the experiment
    thisWider_states_trial = wider_states_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWider_states_trial.rgb)
    if thisWider_states_trial != None:
        for paramName in thisWider_states_trial:
            globals()[paramName] = thisWider_states_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisWider_states_trial in wider_states_trials:
        currentLoop = wider_states_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisWider_states_trial.rgb)
        if thisWider_states_trial != None:
            for paramName in thisWider_states_trial:
                globals()[paramName] = thisWider_states_trial[paramName]
        
        # --- Prepare to start Routine "States_Naming_Task_2" ---
        # create an object to store info about Routine States_Naming_Task_2
        States_Naming_Task_2 = data.Routine(
            name='States_Naming_Task_2',
            components=[stimuli_prompt_2, wider_state_pics, us_state_response_2],
        )
        States_Naming_Task_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        wider_state_pics.setImage(image_file)
        us_state_response_2.reset()
        # store start times for States_Naming_Task_2
        States_Naming_Task_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        States_Naming_Task_2.tStart = globalClock.getTime(format='float')
        States_Naming_Task_2.status = STARTED
        thisExp.addData('States_Naming_Task_2.started', States_Naming_Task_2.tStart)
        States_Naming_Task_2.maxDuration = None
        # keep track of which components have finished
        States_Naming_Task_2Components = States_Naming_Task_2.components
        for thisComponent in States_Naming_Task_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "States_Naming_Task_2" ---
        # if trial has changed, end Routine now
        if isinstance(wider_states_trials, data.TrialHandler2) and thisWider_states_trial.thisN != wider_states_trials.thisTrial.thisN:
            continueRoutine = False
        States_Naming_Task_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 7.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimuli_prompt_2* updates
            
            # if stimuli_prompt_2 is starting this frame...
            if stimuli_prompt_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stimuli_prompt_2.frameNStart = frameN  # exact frame index
                stimuli_prompt_2.tStart = t  # local t and not account for scr refresh
                stimuli_prompt_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimuli_prompt_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_prompt_2.started')
                # update status
                stimuli_prompt_2.status = STARTED
                stimuli_prompt_2.setAutoDraw(True)
            
            # if stimuli_prompt_2 is active this frame...
            if stimuli_prompt_2.status == STARTED:
                # update params
                pass
            
            # if stimuli_prompt_2 is stopping this frame...
            if stimuli_prompt_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimuli_prompt_2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimuli_prompt_2.tStop = t  # not accounting for scr refresh
                    stimuli_prompt_2.tStopRefresh = tThisFlipGlobal  # on global time
                    stimuli_prompt_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimuli_prompt_2.stopped')
                    # update status
                    stimuli_prompt_2.status = FINISHED
                    stimuli_prompt_2.setAutoDraw(False)
            
            # *wider_state_pics* updates
            
            # if wider_state_pics is starting this frame...
            if wider_state_pics.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                wider_state_pics.frameNStart = frameN  # exact frame index
                wider_state_pics.tStart = t  # local t and not account for scr refresh
                wider_state_pics.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wider_state_pics, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wider_state_pics.started')
                # update status
                wider_state_pics.status = STARTED
                wider_state_pics.setAutoDraw(True)
            
            # if wider_state_pics is active this frame...
            if wider_state_pics.status == STARTED:
                # update params
                pass
            
            # if wider_state_pics is stopping this frame...
            if wider_state_pics.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wider_state_pics.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    wider_state_pics.tStop = t  # not accounting for scr refresh
                    wider_state_pics.tStopRefresh = tThisFlipGlobal  # on global time
                    wider_state_pics.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wider_state_pics.stopped')
                    # update status
                    wider_state_pics.status = FINISHED
                    wider_state_pics.setAutoDraw(False)
            
            # *us_state_response_2* updates
            
            # if us_state_response_2 is starting this frame...
            if us_state_response_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                us_state_response_2.frameNStart = frameN  # exact frame index
                us_state_response_2.tStart = t  # local t and not account for scr refresh
                us_state_response_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(us_state_response_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'us_state_response_2.started')
                # update status
                us_state_response_2.status = STARTED
                us_state_response_2.setAutoDraw(True)
            
            # if us_state_response_2 is active this frame...
            if us_state_response_2.status == STARTED:
                # update params
                pass
            
            # if us_state_response_2 is stopping this frame...
            if us_state_response_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > us_state_response_2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    us_state_response_2.tStop = t  # not accounting for scr refresh
                    us_state_response_2.tStopRefresh = tThisFlipGlobal  # on global time
                    us_state_response_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'us_state_response_2.stopped')
                    # update status
                    us_state_response_2.status = FINISHED
                    us_state_response_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                States_Naming_Task_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in States_Naming_Task_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "States_Naming_Task_2" ---
        for thisComponent in States_Naming_Task_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for States_Naming_Task_2
        States_Naming_Task_2.tStop = globalClock.getTime(format='float')
        States_Naming_Task_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('States_Naming_Task_2.stopped', States_Naming_Task_2.tStop)
        wider_states_trials.addData('us_state_response_2.text',us_state_response_2.text)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if States_Naming_Task_2.maxDurationReached:
            routineTimer.addTime(-States_Naming_Task_2.maxDuration)
        elif States_Naming_Task_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'wider_states_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    taller_states_trials = data.TrialHandler2(
        name='taller_states_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('states/loop_taller_states_trials.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(taller_states_trials)  # add the loop to the experiment
    thisTaller_states_trial = taller_states_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTaller_states_trial.rgb)
    if thisTaller_states_trial != None:
        for paramName in thisTaller_states_trial:
            globals()[paramName] = thisTaller_states_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTaller_states_trial in taller_states_trials:
        currentLoop = taller_states_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTaller_states_trial.rgb)
        if thisTaller_states_trial != None:
            for paramName in thisTaller_states_trial:
                globals()[paramName] = thisTaller_states_trial[paramName]
        
        # --- Prepare to start Routine "States_Naming_Task_3" ---
        # create an object to store info about Routine States_Naming_Task_3
        States_Naming_Task_3 = data.Routine(
            name='States_Naming_Task_3',
            components=[stimuli_prompt_3, taller_state_pics, us_state_response_3],
        )
        States_Naming_Task_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        taller_state_pics.setImage(image_file)
        us_state_response_3.reset()
        # store start times for States_Naming_Task_3
        States_Naming_Task_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        States_Naming_Task_3.tStart = globalClock.getTime(format='float')
        States_Naming_Task_3.status = STARTED
        thisExp.addData('States_Naming_Task_3.started', States_Naming_Task_3.tStart)
        States_Naming_Task_3.maxDuration = None
        # keep track of which components have finished
        States_Naming_Task_3Components = States_Naming_Task_3.components
        for thisComponent in States_Naming_Task_3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "States_Naming_Task_3" ---
        # if trial has changed, end Routine now
        if isinstance(taller_states_trials, data.TrialHandler2) and thisTaller_states_trial.thisN != taller_states_trials.thisTrial.thisN:
            continueRoutine = False
        States_Naming_Task_3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 7.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimuli_prompt_3* updates
            
            # if stimuli_prompt_3 is starting this frame...
            if stimuli_prompt_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stimuli_prompt_3.frameNStart = frameN  # exact frame index
                stimuli_prompt_3.tStart = t  # local t and not account for scr refresh
                stimuli_prompt_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimuli_prompt_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_prompt_3.started')
                # update status
                stimuli_prompt_3.status = STARTED
                stimuli_prompt_3.setAutoDraw(True)
            
            # if stimuli_prompt_3 is active this frame...
            if stimuli_prompt_3.status == STARTED:
                # update params
                pass
            
            # if stimuli_prompt_3 is stopping this frame...
            if stimuli_prompt_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimuli_prompt_3.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimuli_prompt_3.tStop = t  # not accounting for scr refresh
                    stimuli_prompt_3.tStopRefresh = tThisFlipGlobal  # on global time
                    stimuli_prompt_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimuli_prompt_3.stopped')
                    # update status
                    stimuli_prompt_3.status = FINISHED
                    stimuli_prompt_3.setAutoDraw(False)
            
            # *taller_state_pics* updates
            
            # if taller_state_pics is starting this frame...
            if taller_state_pics.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                taller_state_pics.frameNStart = frameN  # exact frame index
                taller_state_pics.tStart = t  # local t and not account for scr refresh
                taller_state_pics.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taller_state_pics, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'taller_state_pics.started')
                # update status
                taller_state_pics.status = STARTED
                taller_state_pics.setAutoDraw(True)
            
            # if taller_state_pics is active this frame...
            if taller_state_pics.status == STARTED:
                # update params
                pass
            
            # if taller_state_pics is stopping this frame...
            if taller_state_pics.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taller_state_pics.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    taller_state_pics.tStop = t  # not accounting for scr refresh
                    taller_state_pics.tStopRefresh = tThisFlipGlobal  # on global time
                    taller_state_pics.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taller_state_pics.stopped')
                    # update status
                    taller_state_pics.status = FINISHED
                    taller_state_pics.setAutoDraw(False)
            
            # *us_state_response_3* updates
            
            # if us_state_response_3 is starting this frame...
            if us_state_response_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                us_state_response_3.frameNStart = frameN  # exact frame index
                us_state_response_3.tStart = t  # local t and not account for scr refresh
                us_state_response_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(us_state_response_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'us_state_response_3.started')
                # update status
                us_state_response_3.status = STARTED
                us_state_response_3.setAutoDraw(True)
            
            # if us_state_response_3 is active this frame...
            if us_state_response_3.status == STARTED:
                # update params
                pass
            
            # if us_state_response_3 is stopping this frame...
            if us_state_response_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > us_state_response_3.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    us_state_response_3.tStop = t  # not accounting for scr refresh
                    us_state_response_3.tStopRefresh = tThisFlipGlobal  # on global time
                    us_state_response_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'us_state_response_3.stopped')
                    # update status
                    us_state_response_3.status = FINISHED
                    us_state_response_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                States_Naming_Task_3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in States_Naming_Task_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "States_Naming_Task_3" ---
        for thisComponent in States_Naming_Task_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for States_Naming_Task_3
        States_Naming_Task_3.tStop = globalClock.getTime(format='float')
        States_Naming_Task_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('States_Naming_Task_3.stopped', States_Naming_Task_3.tStop)
        taller_states_trials.addData('us_state_response_3.text',us_state_response_3.text)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if States_Naming_Task_3.maxDurationReached:
            routineTimer.addTime(-States_Naming_Task_3.maxDuration)
        elif States_Naming_Task_3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'taller_states_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instructions_countries_task" ---
    # create an object to store info about Routine instructions_countries_task
    instructions_countries_task = data.Routine(
        name='instructions_countries_task',
        components=[task_instructions_2, instructions_resp_2],
    )
    instructions_countries_task.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instructions_resp_2
    instructions_resp_2.keys = []
    instructions_resp_2.rt = []
    _instructions_resp_2_allKeys = []
    # store start times for instructions_countries_task
    instructions_countries_task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_countries_task.tStart = globalClock.getTime(format='float')
    instructions_countries_task.status = STARTED
    thisExp.addData('instructions_countries_task.started', instructions_countries_task.tStart)
    instructions_countries_task.maxDuration = None
    # keep track of which components have finished
    instructions_countries_taskComponents = instructions_countries_task.components
    for thisComponent in instructions_countries_task.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_countries_task" ---
    instructions_countries_task.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_instructions_2* updates
        
        # if task_instructions_2 is starting this frame...
        if task_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_instructions_2.frameNStart = frameN  # exact frame index
            task_instructions_2.tStart = t  # local t and not account for scr refresh
            task_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_instructions_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_instructions_2.started')
            # update status
            task_instructions_2.status = STARTED
            task_instructions_2.setAutoDraw(True)
        
        # if task_instructions_2 is active this frame...
        if task_instructions_2.status == STARTED:
            # update params
            pass
        
        # *instructions_resp_2* updates
        waitOnFlip = False
        
        # if instructions_resp_2 is starting this frame...
        if instructions_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_resp_2.frameNStart = frameN  # exact frame index
            instructions_resp_2.tStart = t  # local t and not account for scr refresh
            instructions_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_resp_2.started')
            # update status
            instructions_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructions_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructions_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructions_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = instructions_resp_2.getKeys(keyList=["space"], ignoreKeys=["escape"], waitRelease=False)
            _instructions_resp_2_allKeys.extend(theseKeys)
            if len(_instructions_resp_2_allKeys):
                instructions_resp_2.keys = _instructions_resp_2_allKeys[-1].name  # just the last key pressed
                instructions_resp_2.rt = _instructions_resp_2_allKeys[-1].rt
                instructions_resp_2.duration = _instructions_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_countries_task.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_countries_task.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_countries_task" ---
    for thisComponent in instructions_countries_task.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_countries_task
    instructions_countries_task.tStop = globalClock.getTime(format='float')
    instructions_countries_task.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_countries_task.stopped', instructions_countries_task.tStop)
    # check responses
    if instructions_resp_2.keys in ['', [], None]:  # No response was made
        instructions_resp_2.keys = None
    thisExp.addData('instructions_resp_2.keys',instructions_resp_2.keys)
    if instructions_resp_2.keys != None:  # we had a response
        thisExp.addData('instructions_resp_2.rt', instructions_resp_2.rt)
        thisExp.addData('instructions_resp_2.duration', instructions_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "instructions_countries_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    okay_country_trials = data.TrialHandler2(
        name='okay_country_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('south_america/okay_south_america.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(okay_country_trials)  # add the loop to the experiment
    thisOkay_country_trial = okay_country_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOkay_country_trial.rgb)
    if thisOkay_country_trial != None:
        for paramName in thisOkay_country_trial:
            globals()[paramName] = thisOkay_country_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisOkay_country_trial in okay_country_trials:
        currentLoop = okay_country_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisOkay_country_trial.rgb)
        if thisOkay_country_trial != None:
            for paramName in thisOkay_country_trial:
                globals()[paramName] = thisOkay_country_trial[paramName]
        
        # --- Prepare to start Routine "Country_Naming_Task" ---
        # create an object to store info about Routine Country_Naming_Task
        Country_Naming_Task = data.Routine(
            name='Country_Naming_Task',
            components=[stimuli_prompt_4, country_response, okay_country_pics],
        )
        Country_Naming_Task.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        country_response.reset()
        okay_country_pics.setImage(image_file)
        # store start times for Country_Naming_Task
        Country_Naming_Task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Country_Naming_Task.tStart = globalClock.getTime(format='float')
        Country_Naming_Task.status = STARTED
        thisExp.addData('Country_Naming_Task.started', Country_Naming_Task.tStart)
        Country_Naming_Task.maxDuration = None
        # keep track of which components have finished
        Country_Naming_TaskComponents = Country_Naming_Task.components
        for thisComponent in Country_Naming_Task.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Country_Naming_Task" ---
        # if trial has changed, end Routine now
        if isinstance(okay_country_trials, data.TrialHandler2) and thisOkay_country_trial.thisN != okay_country_trials.thisTrial.thisN:
            continueRoutine = False
        Country_Naming_Task.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 7.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimuli_prompt_4* updates
            
            # if stimuli_prompt_4 is starting this frame...
            if stimuli_prompt_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stimuli_prompt_4.frameNStart = frameN  # exact frame index
                stimuli_prompt_4.tStart = t  # local t and not account for scr refresh
                stimuli_prompt_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimuli_prompt_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_prompt_4.started')
                # update status
                stimuli_prompt_4.status = STARTED
                stimuli_prompt_4.setAutoDraw(True)
            
            # if stimuli_prompt_4 is active this frame...
            if stimuli_prompt_4.status == STARTED:
                # update params
                pass
            
            # if stimuli_prompt_4 is stopping this frame...
            if stimuli_prompt_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimuli_prompt_4.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimuli_prompt_4.tStop = t  # not accounting for scr refresh
                    stimuli_prompt_4.tStopRefresh = tThisFlipGlobal  # on global time
                    stimuli_prompt_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimuli_prompt_4.stopped')
                    # update status
                    stimuli_prompt_4.status = FINISHED
                    stimuli_prompt_4.setAutoDraw(False)
            
            # *country_response* updates
            
            # if country_response is starting this frame...
            if country_response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                country_response.frameNStart = frameN  # exact frame index
                country_response.tStart = t  # local t and not account for scr refresh
                country_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(country_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'country_response.started')
                # update status
                country_response.status = STARTED
                country_response.setAutoDraw(True)
            
            # if country_response is active this frame...
            if country_response.status == STARTED:
                # update params
                pass
            
            # if country_response is stopping this frame...
            if country_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > country_response.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    country_response.tStop = t  # not accounting for scr refresh
                    country_response.tStopRefresh = tThisFlipGlobal  # on global time
                    country_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'country_response.stopped')
                    # update status
                    country_response.status = FINISHED
                    country_response.setAutoDraw(False)
            
            # *okay_country_pics* updates
            
            # if okay_country_pics is starting this frame...
            if okay_country_pics.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                okay_country_pics.frameNStart = frameN  # exact frame index
                okay_country_pics.tStart = t  # local t and not account for scr refresh
                okay_country_pics.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(okay_country_pics, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'okay_country_pics.started')
                # update status
                okay_country_pics.status = STARTED
                okay_country_pics.setAutoDraw(True)
            
            # if okay_country_pics is active this frame...
            if okay_country_pics.status == STARTED:
                # update params
                pass
            
            # if okay_country_pics is stopping this frame...
            if okay_country_pics.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > okay_country_pics.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    okay_country_pics.tStop = t  # not accounting for scr refresh
                    okay_country_pics.tStopRefresh = tThisFlipGlobal  # on global time
                    okay_country_pics.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'okay_country_pics.stopped')
                    # update status
                    okay_country_pics.status = FINISHED
                    okay_country_pics.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Country_Naming_Task.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Country_Naming_Task.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Country_Naming_Task" ---
        for thisComponent in Country_Naming_Task.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Country_Naming_Task
        Country_Naming_Task.tStop = globalClock.getTime(format='float')
        Country_Naming_Task.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Country_Naming_Task.stopped', Country_Naming_Task.tStop)
        okay_country_trials.addData('country_response.text',country_response.text)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Country_Naming_Task.maxDurationReached:
            routineTimer.addTime(-Country_Naming_Task.maxDuration)
        elif Country_Naming_Task.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'okay_country_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Country_Naming_Task_2" ---
    # create an object to store info about Routine Country_Naming_Task_2
    Country_Naming_Task_2 = data.Routine(
        name='Country_Naming_Task_2',
        components=[text_2, tall_country_trials, textbox],
    )
    Country_Naming_Task_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # store start times for Country_Naming_Task_2
    Country_Naming_Task_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Country_Naming_Task_2.tStart = globalClock.getTime(format='float')
    Country_Naming_Task_2.status = STARTED
    thisExp.addData('Country_Naming_Task_2.started', Country_Naming_Task_2.tStart)
    Country_Naming_Task_2.maxDuration = None
    # keep track of which components have finished
    Country_Naming_Task_2Components = Country_Naming_Task_2.components
    for thisComponent in Country_Naming_Task_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Country_Naming_Task_2" ---
    Country_Naming_Task_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 7.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *tall_country_trials* updates
        
        # if tall_country_trials is starting this frame...
        if tall_country_trials.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            tall_country_trials.frameNStart = frameN  # exact frame index
            tall_country_trials.tStart = t  # local t and not account for scr refresh
            tall_country_trials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tall_country_trials, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tall_country_trials.started')
            # update status
            tall_country_trials.status = STARTED
            tall_country_trials.setAutoDraw(True)
        
        # if tall_country_trials is active this frame...
        if tall_country_trials.status == STARTED:
            # update params
            pass
        
        # if tall_country_trials is stopping this frame...
        if tall_country_trials.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tall_country_trials.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                tall_country_trials.tStop = t  # not accounting for scr refresh
                tall_country_trials.tStopRefresh = tThisFlipGlobal  # on global time
                tall_country_trials.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tall_country_trials.stopped')
                # update status
                tall_country_trials.status = FINISHED
                tall_country_trials.setAutoDraw(False)
        
        # *textbox* updates
        
        # if textbox is starting this frame...
        if textbox.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            # update status
            textbox.status = STARTED
            textbox.setAutoDraw(True)
        
        # if textbox is active this frame...
        if textbox.status == STARTED:
            # update params
            pass
        
        # if textbox is stopping this frame...
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.tStopRefresh = tThisFlipGlobal  # on global time
                textbox.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.stopped')
                # update status
                textbox.status = FINISHED
                textbox.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Country_Naming_Task_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Country_Naming_Task_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Country_Naming_Task_2" ---
    for thisComponent in Country_Naming_Task_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Country_Naming_Task_2
    Country_Naming_Task_2.tStop = globalClock.getTime(format='float')
    Country_Naming_Task_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Country_Naming_Task_2.stopped', Country_Naming_Task_2.tStop)
    thisExp.addData('textbox.text',textbox.text)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Country_Naming_Task_2.maxDurationReached:
        routineTimer.addTime(-Country_Naming_Task_2.maxDuration)
    elif Country_Naming_Task_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.500000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Finish_Screen" ---
    # create an object to store info about Routine Finish_Screen
    Finish_Screen = data.Routine(
        name='Finish_Screen',
        components=[text],
    )
    Finish_Screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Finish_Screen
    Finish_Screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Finish_Screen.tStart = globalClock.getTime(format='float')
    Finish_Screen.status = STARTED
    thisExp.addData('Finish_Screen.started', Finish_Screen.tStart)
    Finish_Screen.maxDuration = None
    # keep track of which components have finished
    Finish_ScreenComponents = Finish_Screen.components
    for thisComponent in Finish_Screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Finish_Screen" ---
    Finish_Screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.tStopRefresh = tThisFlipGlobal  # on global time
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Finish_Screen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Finish_Screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Finish_Screen" ---
    for thisComponent in Finish_Screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Finish_Screen
    Finish_Screen.tStop = globalClock.getTime(format='float')
    Finish_Screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Finish_Screen.stopped', Finish_Screen.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Finish_Screen.maxDurationReached:
        routineTimer.addTime(-Finish_Screen.maxDuration)
    elif Finish_Screen.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

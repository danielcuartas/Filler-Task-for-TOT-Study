/************************** 
 * State_Naming_Task *
 **************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'state_naming_task';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructions_states_taskRoutineBegin());
flowScheduler.add(instructions_states_taskRoutineEachFrame());
flowScheduler.add(instructions_states_taskRoutineEnd());
const okay_states_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(okay_states_trialsLoopBegin(okay_states_trialsLoopScheduler));
flowScheduler.add(okay_states_trialsLoopScheduler);
flowScheduler.add(okay_states_trialsLoopEnd);


const wider_states_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(wider_states_trialsLoopBegin(wider_states_trialsLoopScheduler));
flowScheduler.add(wider_states_trialsLoopScheduler);
flowScheduler.add(wider_states_trialsLoopEnd);


const taller_states_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(taller_states_trialsLoopBegin(taller_states_trialsLoopScheduler));
flowScheduler.add(taller_states_trialsLoopScheduler);
flowScheduler.add(taller_states_trialsLoopEnd);


flowScheduler.add(instructions_countries_taskRoutineBegin());
flowScheduler.add(instructions_countries_taskRoutineEachFrame());
flowScheduler.add(instructions_countries_taskRoutineEnd());
const okay_country_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(okay_country_trialsLoopBegin(okay_country_trialsLoopScheduler));
flowScheduler.add(okay_country_trialsLoopScheduler);
flowScheduler.add(okay_country_trialsLoopEnd);


flowScheduler.add(Country_Naming_Task_2RoutineBegin());
flowScheduler.add(Country_Naming_Task_2RoutineEachFrame());
flowScheduler.add(Country_Naming_Task_2RoutineEnd());
flowScheduler.add(Finish_ScreenRoutineBegin());
flowScheduler.add(Finish_ScreenRoutineEachFrame());
flowScheduler.add(Finish_ScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'states/loop_okay_states_trials.xlsx', 'path': 'states/loop_okay_states_trials.xlsx'},
    {'name': 'states/Arizona-Outline-Map.jpg', 'path': 'states/Arizona-Outline-Map.jpg'},
    {'name': 'states/Arkansas-Outline-Map.jpg', 'path': 'states/Arkansas-Outline-Map.jpg'},
    {'name': 'states/California-Outline-Map.jpg', 'path': 'states/California-Outline-Map.jpg'},
    {'name': 'states/Colorado-Outline-Map.jpg', 'path': 'states/Colorado-Outline-Map.jpg'},
    {'name': 'states/Connecticut-Outline-Map.jpg', 'path': 'states/Connecticut-Outline-Map.jpg'},
    {'name': 'states/Delaware-Outline-Map.jpg', 'path': 'states/Delaware-Outline-Map.jpg'},
    {'name': 'states/Florida-Outline-Map.jpg', 'path': 'states/Florida-Outline-Map.jpg'},
    {'name': 'states/Hawaii-Outline-Map.jpg', 'path': 'states/Hawaii-Outline-Map.jpg'},
    {'name': 'states/Idaho-Outline-Map.jpg', 'path': 'states/Idaho-Outline-Map.jpg'},
    {'name': 'states/Indiana-Outline-Map.jpg', 'path': 'states/Indiana-Outline-Map.jpg'},
    {'name': 'states/Iowa-Outline-Map.jpg', 'path': 'states/Iowa-Outline-Map.jpg'},
    {'name': 'states/Kansas-Outline-Map.jpg', 'path': 'states/Kansas-Outline-Map.jpg'},
    {'name': 'states/Louisiana-Outline-Map.jpg', 'path': 'states/Louisiana-Outline-Map.jpg'},
    {'name': 'states/Maine-Outline-Map.jpg', 'path': 'states/Maine-Outline-Map.jpg'},
    {'name': 'states/Massachusetts-Outline-Map.jpg', 'path': 'states/Massachusetts-Outline-Map.jpg'},
    {'name': 'states/Michigan-Outline-Map.jpg', 'path': 'states/Michigan-Outline-Map.jpg'},
    {'name': 'states/Minnesota-Outline-Map.jpg', 'path': 'states/Minnesota-Outline-Map.jpg'},
    {'name': 'states/Missouri-Outline-Map.jpg', 'path': 'states/Missouri-Outline-Map.jpg'},
    {'name': 'states/Montana-Outline-Map.jpg', 'path': 'states/Montana-Outline-Map.jpg'},
    {'name': 'states/New-Jersey-Outline-Map.jpg', 'path': 'states/New-Jersey-Outline-Map.jpg'},
    {'name': 'states/New-Mexico-Outline-Map.jpg', 'path': 'states/New-Mexico-Outline-Map.jpg'},
    {'name': 'states/New-York-Outline-Map.jpg', 'path': 'states/New-York-Outline-Map.jpg'},
    {'name': 'states/North-Dakota-Outline-Map.jpg', 'path': 'states/North-Dakota-Outline-Map.jpg'},
    {'name': 'states/Ohio-Outline-Map.jpg', 'path': 'states/Ohio-Outline-Map.jpg'},
    {'name': 'states/Oregon-Outline-Map.jpg', 'path': 'states/Oregon-Outline-Map.jpg'},
    {'name': 'states/Pennsylvania-Outline-Map.jpg', 'path': 'states/Pennsylvania-Outline-Map.jpg'},
    {'name': 'states/Rhode-Island-Outline-Map.jpg', 'path': 'states/Rhode-Island-Outline-Map.jpg'},
    {'name': 'states/South-Carolina-Outline-Map.jpg', 'path': 'states/South-Carolina-Outline-Map.jpg'},
    {'name': 'states/Texas-Outline-Map.jpg', 'path': 'states/Texas-Outline-Map.jpg'},
    {'name': 'states/Utah-Outline-Map.jpg', 'path': 'states/Utah-Outline-Map.jpg'},
    {'name': 'states/Vermont-Outline-Map.jpg', 'path': 'states/Vermont-Outline-Map.jpg'},
    {'name': 'states/Washington-Outline-Map.jpg', 'path': 'states/Washington-Outline-Map.jpg'},
    {'name': 'states/West-Virginia-Outline-Map.jpg', 'path': 'states/West-Virginia-Outline-Map.jpg'},
    {'name': 'states/Wisconsin-Outline-Map.jpg', 'path': 'states/Wisconsin-Outline-Map.jpg'},
    {'name': 'states/Wyoming-Outline-Map.jpg', 'path': 'states/Wyoming-Outline-Map.jpg'},
    {'name': 'states/loop_wider_states_trials.xlsx', 'path': 'states/loop_wider_states_trials.xlsx'},
    {'name': 'states/Alaska-Outline-Map.jpg', 'path': 'states/Alaska-Outline-Map.jpg'},
    {'name': 'states/Kentucky-Outline-Map.jpg', 'path': 'states/Kentucky-Outline-Map.jpg'},
    {'name': 'states/Nebraska-Outline-Map.jpg', 'path': 'states/Nebraska-Outline-Map.jpg'},
    {'name': 'states/North-Carolina-Outline-Map.jpg', 'path': 'states/North-Carolina-Outline-Map.jpg'},
    {'name': 'states/Oklahoma-Outline-Map.jpg', 'path': 'states/Oklahoma-Outline-Map.jpg'},
    {'name': 'states/South-Dakota-Outline-Map.jpg', 'path': 'states/South-Dakota-Outline-Map.jpg'},
    {'name': 'states/Virginia-Outline-Map.jpg', 'path': 'states/Virginia-Outline-Map.jpg'},
    {'name': 'states/Maryland-Outline-Map.jpg', 'path': 'states/Maryland-Outline-Map.jpg'},
    {'name': 'states/Tennessee-Outline-Map.jpg', 'path': 'states/Tennessee-Outline-Map.jpg'},
    {'name': 'states/loop_taller_states_trials.xlsx', 'path': 'states/loop_taller_states_trials.xlsx'},
    {'name': 'states/Alabama-Outline-Map.jpg', 'path': 'states/Alabama-Outline-Map.jpg'},
    {'name': 'states/Georgia-Outline-Map.jpg', 'path': 'states/Georgia-Outline-Map.jpg'},
    {'name': 'states/Illinois-Outline-Map.jpg', 'path': 'states/Illinois-Outline-Map.jpg'},
    {'name': 'states/Nevada-Outline-Map.jpg', 'path': 'states/Nevada-Outline-Map.jpg'},
    {'name': 'states/New-Hampshire-Outline-Map.jpg', 'path': 'states/New-Hampshire-Outline-Map.jpg'},
    {'name': 'states/Mississippi-Outline-Map.jpg', 'path': 'states/Mississippi-Outline-Map.jpg'},
    {'name': 'south_america/okay_south_america.xlsx', 'path': 'south_america/okay_south_america.xlsx'},
    {'name': 'south_america/Argentina-Country-Outline.jpg', 'path': 'south_america/Argentina-Country-Outline.jpg'},
    {'name': 'south_america/Bolivia-Country-Outline.jpg', 'path': 'south_america/Bolivia-Country-Outline.jpg'},
    {'name': 'south_america/Brazil-Country-Outline.jpg', 'path': 'south_america/Brazil-Country-Outline.jpg'},
    {'name': 'south_america/Colombia-Country-Outline.jpg', 'path': 'south_america/Colombia-Country-Outline.jpg'},
    {'name': 'south_america/Ecuador-Country-Outline.jpg', 'path': 'south_america/Ecuador-Country-Outline.jpg'},
    {'name': 'south_america/Guyana-Country-Outline.jpg', 'path': 'south_america/Guyana-Country-Outline.jpg'},
    {'name': 'south_america/Paraguay-Country-Outline.jpg', 'path': 'south_america/Paraguay-Country-Outline.jpg'},
    {'name': 'south_america/Peru-Country-Outline.jpg', 'path': 'south_america/Peru-Country-Outline.jpg'},
    {'name': 'south_america/Suriname-Country-Outline.jpg', 'path': 'south_america/Suriname-Country-Outline.jpg'},
    {'name': 'south_america/Uruguay-Country-Outline.jpg', 'path': 'south_america/Uruguay-Country-Outline.jpg'},
    {'name': 'south_america/Venezuela-Country-Outline.jpg', 'path': 'south_america/Venezuela-Country-Outline.jpg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'south_america/Chile-Country-Outline.jpg', 'path': 'south_america/Chile-Country-Outline.jpg'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var instructions_states_taskClock;
var task_instructions;
var instruction_resp;
var States_Naming_TaskClock;
var stimuli_prompt;
var okay_state_pics;
var us_state_response;
var States_Naming_Task_2Clock;
var stimuli_prompt_2;
var wider_state_pics;
var us_state_response_2;
var States_Naming_Task_3Clock;
var stimuli_prompt_3;
var taller_state_pics;
var us_state_response_3;
var instructions_countries_taskClock;
var task_instructions_2;
var instructions_resp_2;
var Country_Naming_TaskClock;
var stimuli_prompt_4;
var country_response;
var okay_country_pics;
var Country_Naming_Task_2Clock;
var text_2;
var tall_country_trials;
var textbox;
var Finish_ScreenClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instructions_states_task"
  instructions_states_taskClock = new util.Clock();
  task_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'task_instructions',
    text: 'In this task, you will see a blank map of each U.S. state which will be displayed for 7 seconds. Your goal is to identify each state by providing a typed response within that 7 seconds. After identifying each U.S. state you will be presented with a blank map of various countries to label.\n\nThis task should take approximately 10 minutes to complete.\n\n\nPlease press "space" to begin this task.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  instruction_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "States_Naming_Task"
  States_Naming_TaskClock = new util.Clock();
  stimuli_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'stimuli_prompt',
    text: 'What is the name of this U.S. State?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  okay_state_pics = new visual.ImageStim({
    win : psychoJS.window,
    name : 'okay_state_pics', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: true,
    size : [0.6, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  us_state_response = new visual.TextBox({
    win: psychoJS.window,
    name: 'us_state_response',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.4)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Initialize components for Routine "States_Naming_Task_2"
  States_Naming_Task_2Clock = new util.Clock();
  stimuli_prompt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'stimuli_prompt_2',
    text: 'What is the name of this U.S. state?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  wider_state_pics = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wider_state_pics', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.95, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  us_state_response_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'us_state_response_2',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.4)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Initialize components for Routine "States_Naming_Task_3"
  States_Naming_Task_3Clock = new util.Clock();
  stimuli_prompt_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'stimuli_prompt_3',
    text: 'What is the name of this U.S. state?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  taller_state_pics = new visual.ImageStim({
    win : psychoJS.window,
    name : 'taller_state_pics', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.65],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  us_state_response_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'us_state_response_3',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.4)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Initialize components for Routine "instructions_countries_task"
  instructions_countries_taskClock = new util.Clock();
  task_instructions_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'task_instructions_2',
    text: 'Now you will be identifying different countries. As with the previous task, you will have 7 seconds to type a response, and after 7 seconds have passed you will move onto the next country.\n\nPress "space" to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  instructions_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Country_Naming_Task"
  Country_Naming_TaskClock = new util.Clock();
  stimuli_prompt_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'stimuli_prompt_4',
    text: 'What is the name of this South American country?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  country_response = new visual.TextBox({
    win: psychoJS.window,
    name: 'country_response',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.4)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  okay_country_pics = new visual.ImageStim({
    win : psychoJS.window,
    name : 'okay_country_pics', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.65],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Country_Naming_Task_2"
  Country_Naming_Task_2Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'What is the name of this South American country?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  tall_country_trials = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tall_country_trials', units : undefined, 
    image : 'south_america/Chile-Country-Outline.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.6],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.6)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'bottom-center',
    depth: -2.0 
  });
  
  // Initialize components for Routine "Finish_Screen"
  Finish_ScreenClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'You have now completed these two other tasks. Once this screen returns to the desktop, please notify the researcher that you have completed this part of the study.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var instructions_states_taskMaxDurationReached;
var _instruction_resp_allKeys;
var instructions_states_taskMaxDuration;
var instructions_states_taskComponents;
function instructions_states_taskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_states_task' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instructions_states_taskClock.reset();
    routineTimer.reset();
    instructions_states_taskMaxDurationReached = false;
    // update component parameters for each repeat
    instruction_resp.keys = undefined;
    instruction_resp.rt = undefined;
    _instruction_resp_allKeys = [];
    psychoJS.experiment.addData('instructions_states_task.started', globalClock.getTime());
    instructions_states_taskMaxDuration = null
    // keep track of which components have finished
    instructions_states_taskComponents = [];
    instructions_states_taskComponents.push(task_instructions);
    instructions_states_taskComponents.push(instruction_resp);
    
    for (const thisComponent of instructions_states_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_states_taskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_states_task' ---
    // get current time
    t = instructions_states_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *task_instructions* updates
    if (t >= 0.0 && task_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_instructions.tStart = t;  // (not accounting for frame time here)
      task_instructions.frameNStart = frameN;  // exact frame index
      
      task_instructions.setAutoDraw(true);
    }
    
    
    // *instruction_resp* updates
    if (t >= 0.0 && instruction_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_resp.tStart = t;  // (not accounting for frame time here)
      instruction_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruction_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruction_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruction_resp.clearEvents(); });
    }
    
    if (instruction_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruction_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instruction_resp_allKeys = _instruction_resp_allKeys.concat(theseKeys);
      if (_instruction_resp_allKeys.length > 0) {
        instruction_resp.keys = _instruction_resp_allKeys[_instruction_resp_allKeys.length - 1].name;  // just the last key pressed
        instruction_resp.rt = _instruction_resp_allKeys[_instruction_resp_allKeys.length - 1].rt;
        instruction_resp.duration = _instruction_resp_allKeys[_instruction_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_states_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_states_taskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_states_task' ---
    for (const thisComponent of instructions_states_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructions_states_task.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instruction_resp.corr, level);
    }
    psychoJS.experiment.addData('instruction_resp.keys', instruction_resp.keys);
    if (typeof instruction_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruction_resp.rt', instruction_resp.rt);
        psychoJS.experiment.addData('instruction_resp.duration', instruction_resp.duration);
        routineTimer.reset();
        }
    
    instruction_resp.stop();
    // the Routine "instructions_states_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var okay_states_trials;
function okay_states_trialsLoopBegin(okay_states_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    okay_states_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'states/loop_okay_states_trials.xlsx',
      seed: undefined, name: 'okay_states_trials'
    });
    psychoJS.experiment.addLoop(okay_states_trials); // add the loop to the experiment
    currentLoop = okay_states_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisOkay_states_trial of okay_states_trials) {
      snapshot = okay_states_trials.getSnapshot();
      okay_states_trialsLoopScheduler.add(importConditions(snapshot));
      okay_states_trialsLoopScheduler.add(States_Naming_TaskRoutineBegin(snapshot));
      okay_states_trialsLoopScheduler.add(States_Naming_TaskRoutineEachFrame());
      okay_states_trialsLoopScheduler.add(States_Naming_TaskRoutineEnd(snapshot));
      okay_states_trialsLoopScheduler.add(okay_states_trialsLoopEndIteration(okay_states_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function okay_states_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(okay_states_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function okay_states_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var wider_states_trials;
function wider_states_trialsLoopBegin(wider_states_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    wider_states_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'states/loop_wider_states_trials.xlsx',
      seed: undefined, name: 'wider_states_trials'
    });
    psychoJS.experiment.addLoop(wider_states_trials); // add the loop to the experiment
    currentLoop = wider_states_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisWider_states_trial of wider_states_trials) {
      snapshot = wider_states_trials.getSnapshot();
      wider_states_trialsLoopScheduler.add(importConditions(snapshot));
      wider_states_trialsLoopScheduler.add(States_Naming_Task_2RoutineBegin(snapshot));
      wider_states_trialsLoopScheduler.add(States_Naming_Task_2RoutineEachFrame());
      wider_states_trialsLoopScheduler.add(States_Naming_Task_2RoutineEnd(snapshot));
      wider_states_trialsLoopScheduler.add(wider_states_trialsLoopEndIteration(wider_states_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function wider_states_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(wider_states_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function wider_states_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var taller_states_trials;
function taller_states_trialsLoopBegin(taller_states_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    taller_states_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'states/loop_taller_states_trials.xlsx',
      seed: undefined, name: 'taller_states_trials'
    });
    psychoJS.experiment.addLoop(taller_states_trials); // add the loop to the experiment
    currentLoop = taller_states_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTaller_states_trial of taller_states_trials) {
      snapshot = taller_states_trials.getSnapshot();
      taller_states_trialsLoopScheduler.add(importConditions(snapshot));
      taller_states_trialsLoopScheduler.add(States_Naming_Task_3RoutineBegin(snapshot));
      taller_states_trialsLoopScheduler.add(States_Naming_Task_3RoutineEachFrame());
      taller_states_trialsLoopScheduler.add(States_Naming_Task_3RoutineEnd(snapshot));
      taller_states_trialsLoopScheduler.add(taller_states_trialsLoopEndIteration(taller_states_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function taller_states_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(taller_states_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function taller_states_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var okay_country_trials;
function okay_country_trialsLoopBegin(okay_country_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    okay_country_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'south_america/okay_south_america.xlsx',
      seed: undefined, name: 'okay_country_trials'
    });
    psychoJS.experiment.addLoop(okay_country_trials); // add the loop to the experiment
    currentLoop = okay_country_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisOkay_country_trial of okay_country_trials) {
      snapshot = okay_country_trials.getSnapshot();
      okay_country_trialsLoopScheduler.add(importConditions(snapshot));
      okay_country_trialsLoopScheduler.add(Country_Naming_TaskRoutineBegin(snapshot));
      okay_country_trialsLoopScheduler.add(Country_Naming_TaskRoutineEachFrame());
      okay_country_trialsLoopScheduler.add(Country_Naming_TaskRoutineEnd(snapshot));
      okay_country_trialsLoopScheduler.add(okay_country_trialsLoopEndIteration(okay_country_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function okay_country_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(okay_country_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function okay_country_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var States_Naming_TaskMaxDurationReached;
var States_Naming_TaskMaxDuration;
var States_Naming_TaskComponents;
function States_Naming_TaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'States_Naming_Task' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    States_Naming_TaskClock.reset(routineTimer.getTime());
    routineTimer.add(7.500000);
    States_Naming_TaskMaxDurationReached = false;
    // update component parameters for each repeat
    okay_state_pics.setOri(0.0);
    okay_state_pics.setImage(image_file);
    us_state_response.setText('');
    us_state_response.refresh();
    psychoJS.experiment.addData('States_Naming_Task.started', globalClock.getTime());
    States_Naming_TaskMaxDuration = null
    // keep track of which components have finished
    States_Naming_TaskComponents = [];
    States_Naming_TaskComponents.push(stimuli_prompt);
    States_Naming_TaskComponents.push(okay_state_pics);
    States_Naming_TaskComponents.push(us_state_response);
    
    for (const thisComponent of States_Naming_TaskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function States_Naming_TaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'States_Naming_Task' ---
    // get current time
    t = States_Naming_TaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimuli_prompt* updates
    if (t >= 0.5 && stimuli_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli_prompt.tStart = t;  // (not accounting for frame time here)
      stimuli_prompt.frameNStart = frameN;  // exact frame index
      
      stimuli_prompt.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (stimuli_prompt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimuli_prompt.setAutoDraw(false);
    }
    
    
    // *okay_state_pics* updates
    if (t >= 0.5 && okay_state_pics.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      okay_state_pics.tStart = t;  // (not accounting for frame time here)
      okay_state_pics.frameNStart = frameN;  // exact frame index
      
      okay_state_pics.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (okay_state_pics.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      okay_state_pics.setAutoDraw(false);
    }
    
    
    // *us_state_response* updates
    if (t >= 0.5 && us_state_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      us_state_response.tStart = t;  // (not accounting for frame time here)
      us_state_response.frameNStart = frameN;  // exact frame index
      
      us_state_response.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (us_state_response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      us_state_response.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of States_Naming_TaskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function States_Naming_TaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'States_Naming_Task' ---
    for (const thisComponent of States_Naming_TaskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('States_Naming_Task.stopped', globalClock.getTime());
    psychoJS.experiment.addData('us_state_response.text',us_state_response.text)
    if (States_Naming_TaskMaxDurationReached) {
        States_Naming_TaskClock.add(States_Naming_TaskMaxDuration);
    } else {
        States_Naming_TaskClock.add(7.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var States_Naming_Task_2MaxDurationReached;
var States_Naming_Task_2MaxDuration;
var States_Naming_Task_2Components;
function States_Naming_Task_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'States_Naming_Task_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    States_Naming_Task_2Clock.reset(routineTimer.getTime());
    routineTimer.add(7.500000);
    States_Naming_Task_2MaxDurationReached = false;
    // update component parameters for each repeat
    wider_state_pics.setImage(image_file);
    us_state_response_2.setText('');
    us_state_response_2.refresh();
    psychoJS.experiment.addData('States_Naming_Task_2.started', globalClock.getTime());
    States_Naming_Task_2MaxDuration = null
    // keep track of which components have finished
    States_Naming_Task_2Components = [];
    States_Naming_Task_2Components.push(stimuli_prompt_2);
    States_Naming_Task_2Components.push(wider_state_pics);
    States_Naming_Task_2Components.push(us_state_response_2);
    
    for (const thisComponent of States_Naming_Task_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function States_Naming_Task_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'States_Naming_Task_2' ---
    // get current time
    t = States_Naming_Task_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimuli_prompt_2* updates
    if (t >= 0.5 && stimuli_prompt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli_prompt_2.tStart = t;  // (not accounting for frame time here)
      stimuli_prompt_2.frameNStart = frameN;  // exact frame index
      
      stimuli_prompt_2.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (stimuli_prompt_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimuli_prompt_2.setAutoDraw(false);
    }
    
    
    // *wider_state_pics* updates
    if (t >= 0.5 && wider_state_pics.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wider_state_pics.tStart = t;  // (not accounting for frame time here)
      wider_state_pics.frameNStart = frameN;  // exact frame index
      
      wider_state_pics.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (wider_state_pics.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wider_state_pics.setAutoDraw(false);
    }
    
    
    // *us_state_response_2* updates
    if (t >= 0.5 && us_state_response_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      us_state_response_2.tStart = t;  // (not accounting for frame time here)
      us_state_response_2.frameNStart = frameN;  // exact frame index
      
      us_state_response_2.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (us_state_response_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      us_state_response_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of States_Naming_Task_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function States_Naming_Task_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'States_Naming_Task_2' ---
    for (const thisComponent of States_Naming_Task_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('States_Naming_Task_2.stopped', globalClock.getTime());
    psychoJS.experiment.addData('us_state_response_2.text',us_state_response_2.text)
    if (States_Naming_Task_2MaxDurationReached) {
        States_Naming_Task_2Clock.add(States_Naming_Task_2MaxDuration);
    } else {
        States_Naming_Task_2Clock.add(7.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var States_Naming_Task_3MaxDurationReached;
var States_Naming_Task_3MaxDuration;
var States_Naming_Task_3Components;
function States_Naming_Task_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'States_Naming_Task_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    States_Naming_Task_3Clock.reset(routineTimer.getTime());
    routineTimer.add(7.500000);
    States_Naming_Task_3MaxDurationReached = false;
    // update component parameters for each repeat
    taller_state_pics.setImage(image_file);
    us_state_response_3.setText('');
    us_state_response_3.refresh();
    psychoJS.experiment.addData('States_Naming_Task_3.started', globalClock.getTime());
    States_Naming_Task_3MaxDuration = null
    // keep track of which components have finished
    States_Naming_Task_3Components = [];
    States_Naming_Task_3Components.push(stimuli_prompt_3);
    States_Naming_Task_3Components.push(taller_state_pics);
    States_Naming_Task_3Components.push(us_state_response_3);
    
    for (const thisComponent of States_Naming_Task_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function States_Naming_Task_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'States_Naming_Task_3' ---
    // get current time
    t = States_Naming_Task_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimuli_prompt_3* updates
    if (t >= 0.5 && stimuli_prompt_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli_prompt_3.tStart = t;  // (not accounting for frame time here)
      stimuli_prompt_3.frameNStart = frameN;  // exact frame index
      
      stimuli_prompt_3.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (stimuli_prompt_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimuli_prompt_3.setAutoDraw(false);
    }
    
    
    // *taller_state_pics* updates
    if (t >= 0.5 && taller_state_pics.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      taller_state_pics.tStart = t;  // (not accounting for frame time here)
      taller_state_pics.frameNStart = frameN;  // exact frame index
      
      taller_state_pics.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (taller_state_pics.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      taller_state_pics.setAutoDraw(false);
    }
    
    
    // *us_state_response_3* updates
    if (t >= 0.5 && us_state_response_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      us_state_response_3.tStart = t;  // (not accounting for frame time here)
      us_state_response_3.frameNStart = frameN;  // exact frame index
      
      us_state_response_3.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (us_state_response_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      us_state_response_3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of States_Naming_Task_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function States_Naming_Task_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'States_Naming_Task_3' ---
    for (const thisComponent of States_Naming_Task_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('States_Naming_Task_3.stopped', globalClock.getTime());
    psychoJS.experiment.addData('us_state_response_3.text',us_state_response_3.text)
    if (States_Naming_Task_3MaxDurationReached) {
        States_Naming_Task_3Clock.add(States_Naming_Task_3MaxDuration);
    } else {
        States_Naming_Task_3Clock.add(7.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructions_countries_taskMaxDurationReached;
var _instructions_resp_2_allKeys;
var instructions_countries_taskMaxDuration;
var instructions_countries_taskComponents;
function instructions_countries_taskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_countries_task' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instructions_countries_taskClock.reset();
    routineTimer.reset();
    instructions_countries_taskMaxDurationReached = false;
    // update component parameters for each repeat
    instructions_resp_2.keys = undefined;
    instructions_resp_2.rt = undefined;
    _instructions_resp_2_allKeys = [];
    psychoJS.experiment.addData('instructions_countries_task.started', globalClock.getTime());
    instructions_countries_taskMaxDuration = null
    // keep track of which components have finished
    instructions_countries_taskComponents = [];
    instructions_countries_taskComponents.push(task_instructions_2);
    instructions_countries_taskComponents.push(instructions_resp_2);
    
    for (const thisComponent of instructions_countries_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_countries_taskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_countries_task' ---
    // get current time
    t = instructions_countries_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *task_instructions_2* updates
    if (t >= 0.0 && task_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_instructions_2.tStart = t;  // (not accounting for frame time here)
      task_instructions_2.frameNStart = frameN;  // exact frame index
      
      task_instructions_2.setAutoDraw(true);
    }
    
    
    // *instructions_resp_2* updates
    if (t >= 0.0 && instructions_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_resp_2.tStart = t;  // (not accounting for frame time here)
      instructions_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_resp_2.clearEvents(); });
    }
    
    if (instructions_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _instructions_resp_2_allKeys = _instructions_resp_2_allKeys.concat(theseKeys);
      if (_instructions_resp_2_allKeys.length > 0) {
        instructions_resp_2.keys = _instructions_resp_2_allKeys[_instructions_resp_2_allKeys.length - 1].name;  // just the last key pressed
        instructions_resp_2.rt = _instructions_resp_2_allKeys[_instructions_resp_2_allKeys.length - 1].rt;
        instructions_resp_2.duration = _instructions_resp_2_allKeys[_instructions_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_countries_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_countries_taskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_countries_task' ---
    for (const thisComponent of instructions_countries_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructions_countries_task.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructions_resp_2.corr, level);
    }
    psychoJS.experiment.addData('instructions_resp_2.keys', instructions_resp_2.keys);
    if (typeof instructions_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_resp_2.rt', instructions_resp_2.rt);
        psychoJS.experiment.addData('instructions_resp_2.duration', instructions_resp_2.duration);
        routineTimer.reset();
        }
    
    instructions_resp_2.stop();
    // the Routine "instructions_countries_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Country_Naming_TaskMaxDurationReached;
var Country_Naming_TaskMaxDuration;
var Country_Naming_TaskComponents;
function Country_Naming_TaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Country_Naming_Task' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Country_Naming_TaskClock.reset(routineTimer.getTime());
    routineTimer.add(7.500000);
    Country_Naming_TaskMaxDurationReached = false;
    // update component parameters for each repeat
    country_response.setText('');
    country_response.refresh();
    okay_country_pics.setImage(image_file);
    psychoJS.experiment.addData('Country_Naming_Task.started', globalClock.getTime());
    Country_Naming_TaskMaxDuration = null
    // keep track of which components have finished
    Country_Naming_TaskComponents = [];
    Country_Naming_TaskComponents.push(stimuli_prompt_4);
    Country_Naming_TaskComponents.push(country_response);
    Country_Naming_TaskComponents.push(okay_country_pics);
    
    for (const thisComponent of Country_Naming_TaskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Country_Naming_TaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Country_Naming_Task' ---
    // get current time
    t = Country_Naming_TaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimuli_prompt_4* updates
    if (t >= 0.5 && stimuli_prompt_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli_prompt_4.tStart = t;  // (not accounting for frame time here)
      stimuli_prompt_4.frameNStart = frameN;  // exact frame index
      
      stimuli_prompt_4.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (stimuli_prompt_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimuli_prompt_4.setAutoDraw(false);
    }
    
    
    // *country_response* updates
    if (t >= 0.5 && country_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      country_response.tStart = t;  // (not accounting for frame time here)
      country_response.frameNStart = frameN;  // exact frame index
      
      country_response.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (country_response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      country_response.setAutoDraw(false);
    }
    
    
    // *okay_country_pics* updates
    if (t >= 0.5 && okay_country_pics.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      okay_country_pics.tStart = t;  // (not accounting for frame time here)
      okay_country_pics.frameNStart = frameN;  // exact frame index
      
      okay_country_pics.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (okay_country_pics.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      okay_country_pics.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Country_Naming_TaskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Country_Naming_TaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Country_Naming_Task' ---
    for (const thisComponent of Country_Naming_TaskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Country_Naming_Task.stopped', globalClock.getTime());
    psychoJS.experiment.addData('country_response.text',country_response.text)
    if (Country_Naming_TaskMaxDurationReached) {
        Country_Naming_TaskClock.add(Country_Naming_TaskMaxDuration);
    } else {
        Country_Naming_TaskClock.add(7.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Country_Naming_Task_2MaxDurationReached;
var Country_Naming_Task_2MaxDuration;
var Country_Naming_Task_2Components;
function Country_Naming_Task_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Country_Naming_Task_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Country_Naming_Task_2Clock.reset(routineTimer.getTime());
    routineTimer.add(7.500000);
    Country_Naming_Task_2MaxDurationReached = false;
    // update component parameters for each repeat
    textbox.setText('');
    textbox.refresh();
    psychoJS.experiment.addData('Country_Naming_Task_2.started', globalClock.getTime());
    Country_Naming_Task_2MaxDuration = null
    // keep track of which components have finished
    Country_Naming_Task_2Components = [];
    Country_Naming_Task_2Components.push(text_2);
    Country_Naming_Task_2Components.push(tall_country_trials);
    Country_Naming_Task_2Components.push(textbox);
    
    for (const thisComponent of Country_Naming_Task_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Country_Naming_Task_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Country_Naming_Task_2' ---
    // get current time
    t = Country_Naming_Task_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.5 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    
    
    // *tall_country_trials* updates
    if (t >= 0.5 && tall_country_trials.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tall_country_trials.tStart = t;  // (not accounting for frame time here)
      tall_country_trials.frameNStart = frameN;  // exact frame index
      
      tall_country_trials.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (tall_country_trials.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tall_country_trials.setAutoDraw(false);
    }
    
    
    // *textbox* updates
    if (t >= 0.5 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textbox.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textbox.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Country_Naming_Task_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Country_Naming_Task_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Country_Naming_Task_2' ---
    for (const thisComponent of Country_Naming_Task_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Country_Naming_Task_2.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox.text',textbox.text)
    if (Country_Naming_Task_2MaxDurationReached) {
        Country_Naming_Task_2Clock.add(Country_Naming_Task_2MaxDuration);
    } else {
        Country_Naming_Task_2Clock.add(7.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Finish_ScreenMaxDurationReached;
var Finish_ScreenMaxDuration;
var Finish_ScreenComponents;
function Finish_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Finish_Screen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Finish_ScreenClock.reset(routineTimer.getTime());
    routineTimer.add(10.000000);
    Finish_ScreenMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Finish_Screen.started', globalClock.getTime());
    Finish_ScreenMaxDuration = null
    // keep track of which components have finished
    Finish_ScreenComponents = [];
    Finish_ScreenComponents.push(text);
    
    for (const thisComponent of Finish_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Finish_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Finish_Screen' ---
    // get current time
    t = Finish_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Finish_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Finish_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Finish_Screen' ---
    for (const thisComponent of Finish_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Finish_Screen.stopped', globalClock.getTime());
    if (Finish_ScreenMaxDurationReached) {
        Finish_ScreenClock.add(Finish_ScreenMaxDuration);
    } else {
        Finish_ScreenClock.add(10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

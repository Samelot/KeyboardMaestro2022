var beatEffectArray = {
	"1": 1, // Delay
	"2": 7, // Echo
	"3": null, // Ping Pong
	"4": 13, // Spiral
	"5": 24, // Reverb
	"6": 45, // Trans
	"7": 60, // Filter
	"8": 69, // Flanger
	"9": 75, // Phaser
	"10": 103, // Pitch
	"11": 80, // Slip Roll
	"12": 86, // Roll
	"13": null, // Vinyl Brake
	"14": null // Helix
};

var beatSizeArray = {
	"1/16": null,
	"1/8": 1,
	"1/4": 2,
	"1/2": 3,
	"3/4": 4,
	"1": 5,
	"2": 6,
	"4": 7
};

function KMWindow() {
	return "SCREEN(Main,Left,80%),SCREEN(Main,Top,80%),500, 800";	//JMU CHG 420, 700
}

function KMInit() {
	document.getElementById('ignored').value = window.KeyboardMaestro.Calculate('10,32*12');
}

function update(id) {
	  id.innerHTML = "nothing again";
}

/*
function updateFromButton() {
	var sel = document.querySelector('input[name="ASRadio"]:checked').value;
	var triggerValue = (beatEffects[sel] === null) ? false : beatEffects[sel];
	if (triggerValue == false) {
		triggerValue = triggerValue.toString()
		document.getElementById('kmvar').innerHTML = "No Such Effect In Rekordbox";
		window.KeyboardMaestro.Trigger( "Update Effect", triggerValue );
	} else {
		triggerValue = triggerValue.toString()
		document.getElementById('kmvar').innerHTML = triggerValue;
		window.KeyboardMaestro.Trigger( "Update Effect", triggerValue );
	}
}

function updateBeat() {
	var sel = document.querySelector('input[name="Beat"]:checked').value;
	var triggerValue = (beatSize[sel] === null) ? false : beatSize[sel]
	if (triggerValue == false) {
		triggerValue = triggerValue.toString()
		document.getElementById('kmvar').innerHTML = " No Need To Change Beat Size / No Such Beat Size In Rekordbox";
		window.KeyboardMaestro.Trigger( "Update Beat", triggerValue );
	} else {
		triggerValue = triggerValue.toString()
		document.getElementById('kmvar').innerHTML = triggerValue;
		window.KeyboardMaestro.Trigger( "Update Beat", triggerValue );
	}
}
*/

function inputEventHandler(i) {

}

function changeEventHandler(i) {
	var triggerValue = i.value;
	var beatEffect = (beatEffectArray[triggerValue] === null) ? false : beatEffectArray[triggerValue];

	if (beatEffect == false) {
		beatEffect = beatEffect.toString()
		document.getElementById('kmvar').innerHTML = " No Need To Change Beat Size / No Such Beat Size In Rekordbox";
		window.KeyboardMaestro.Trigger( "Update Beat", beatEffect );
	} else {
		beatEffect = beatEffect.toString()
		document.getElementById('kmvar').innerHTML = triggerValue;
		window.KeyboardMaestro.Trigger( "Update Beat", beatEffect );
	}	
}

/*
$(document).ready(function() {
    $("input.input-knob").val(2);
});
*/
### Custom Keyboard Maestro Plug-in
#### NAME
- Activate an Application by Name

#### VERSION
- 0.1

#### SYNOPSIS
- Activates a specific application by its name, which can be specified at run-time, for example from a KM variable.
- Offers the same set of options as the built-in **Activate a Specific Application** action


#### REQUIREMENTS
- Yosemite
	- The core script `activatedApp.sh` is mainly written in Javascript for Applications
	
#### OPTIONS
- Name of Application
	- Full application name, for example `Google Chrome` rather than just `Chrome`, or `Microsoft Excel` rather than just `Excel`.
	- If the name is not correctly spelled, or the named application is not installed, the action will give a brief notification, using the system `Sosumi` sound.
- All windows ?  (checkbox)
- Reopen initial windows ? (checkbox)
- If already at the front:
	- leave it at the front
	- switch to last application
	- hide the application
	- quit the application
- Results
	- If the application is found, the results (which can be ignored, displayed or captured in variable or clipboard) will consist of the **Keyboard Maestro XML** (as in a .kmactions or .kmmacros file) corresponding to this action and set of options.
	- This XML can be pasted into code and executed by the Keyboard Maestro Engine .doScript() function.
	- **Menu of result-handling options**
		- Ignore results
		- Display results in a window
		- Display results briefly
		- Save results to variable
		- Save results to clipboard
	
#### INSTALLATION
- Drag the .zip file onto the Keyboard Maestro icon in the OS X toolbar.
- (if updating a previous version of the action, first manually remove the previous copy from the custom actions folder)
	- `~/Library/Application Support/Keyboard Maestro/Keyboard Maestro Actions`

#### CONTACT
- Rob Trew – Twitter @ComplexPoint – Aug 2015
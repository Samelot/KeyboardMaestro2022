// Activate named application
// Custom action plugin for Keyboard Maestro 7 on OS X 10.10+
// Rob Trew twitter: @ComplexPoint 2015

(function (strAppName, strAll, strReopen, strAlready) {
	strAppName = strAppName || "Finder";
	strAlready = strAlready || "leave it at the front";


	// ITS BUNDLE ID, AND APP FILE PATH ?
	var fnHotAppDetails = function (strAppName) {
			// running app ...
			var procs = Application(
					"System Events"
				).applicationProcesses.where({
					name: strAppName
				}),
				procApp = procs.length ? procs[0] : null;

			return procApp ? {
				id: procApp.bundleIdentifier(),
				path: procApp.file.posixPath().toString()
			} : null
		},

		fnColdAppDetails = function (strAppName) {
			// unlaunched app ...
			var a = Application.currentApplication(),
				sa = (a.includeStandardAdditions = true, a),
				lst;

			try {
				lst = sa.doShellScript(
					[
						'osascript <<AS_END 2>/dev/null',
						'set strID to id of application "' + strAppName + '"',
						'tell application "Finder"',
						'	set strPath to POSIX path of (application file id strID as alias)',
						'end tell',
						'strID & linefeed & strPath',
						'AS_END'
					].join('\n')
				).split(/[\r\n]+/);
			} catch (e) {
				lst = [];
			}

			return (lst.length > 1) ? {
				id: lst[0],
				path: lst[1]
			} : null;
		},

		fnDoAction = function (dctAction) {
			// XML FOR KM ACTION DICTIONARY
			var dctXMLfn = {
					array: function (a) {
						return a.length ? "<array>" + a.reduce(function (a, c) {
							return a + dctXMLfn[typeof c](c);
						}, "") + "</array>" : "<array/>";
					},
					boolean: function (a) {
						return a ? "<true/>" : "<false/>";
					},
					dict: function (a) {
						var b = Object.keys(a);
						return "<dict>" + (b.sort() && b).reduce(function (c, b) {
							var d = a[b];
							return c + "<key>" + b + "</key>" + dctXMLfn[typeof d](d);
						}, "") + "</dict>";
					},
					number: function (a) {
						return "<real>" + (a ? a : "0.0") + "</real>";
					},
					object: function (a) {
						return dctXMLfn[a instanceof Array ? "array" : "dict"](a);
					},
					string: function (a) {
						return "<string>" + a + "</string>";
					}
				},
				strXML = dctXMLfn['dict'](dctAction);

			return Application("Keyboard Maestro Engine").doScript(
				strXML
			) || strXML;
		},

		dctApp = fnHotAppDetails(
			strAppName
		) || fnColdAppDetails(
			strAppName
		),
		strID = dctApp ? dctApp.id : null;

	return fnDoAction(
		strID ? {
			"AllWindows": (strAll === '1'),
			"AlreadyActivatedActionType": ({
				'leave it at the front': 'Normal',
				'switch to last application': 'SwitchToLast',
				'hide the application': 'Hide',
				'quit the application': 'Quit'
			})[strAlready],
			"Application": {
				"BundleIdentifier": strID,
				"Name": strAppName,
				"NewFile": dctApp.path
			},
			MacroActionType: "ActivateApplication",
			ReopenWindows: (strReopen === '1')
		} : {
			'MacroActionType': 'Notification',
			'SoundName': 'Sosumi',
			'Subtitle': 'Application not found as spelled',
			'Text': 'Custom KM Action: Activate application by name',
			'Title': '"' + strAppName + '"'
		}
	);

})(
	"$KMPARAM_Activate",
	"$KMPARAM_All_windows",
	"$KMPARAM_Reopen_initial_windows",
	"$KMPARAM_If_already_at_the_front"
);
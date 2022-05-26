const chokidar = require('chokidar');
const fs = require('fs');

var watcher = chokidar.watch('./save games', {ignored: /^\./, persistent: true, awaitWriteFinish: true, ignoreInitial: true});
var index = 0;
watcher
  .on('add', function(path) {
	  index += 1;
	  console.log('File', path, 'has been added');
	  let baseDestination = path.split(/[\\/]/).pop().split(".")[0];
	  let destination = './savesWatcher/' + baseDestination + "_" + index + ".eu4";

	  fs.copyFile(path, destination, fs.constants.COPYFILE_FICLONE, (err) => {
		  if (err) {
			console.log("Error Found:", err);
		  }
		  else {
			console.log("Copied", path, "to", destination)
		  }
		});
  });
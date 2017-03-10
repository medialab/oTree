const {app, BrowserWindow} = require('electron');

let win;

const closedHandler = () => win = null;

const createWin = () => {
  const win = new BrowserWindow({
    width: 200,
    height: 200,
    autoHideMenuBar: true,
    useContentSize: true,
    resizable: false
  });

  win.loadURL(require('url').format({
    pathname: require('path').join(__dirname, './index.html'),
    protocol: 'file',
    slashes: true
  }));

  //win.webContents.openDevTools();
  win.on('closed', closedHandler);

  return win;
};

app.on('window-all-closed', app.quit);
app.on('activate', () => {
  if (!win) win = createWin();
});
app.on('ready', () => {
  win = createWin();
})

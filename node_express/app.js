const express = require('express');
const chalk = require('chalk');
const debug = require('debug')('app');
const morgan = require('morgan');

const app = express();
const port = process.env.PORT || 3000;

app.use(morgan('tiny'));
app.get('/', (req, res) => {
  res.send('Hello world.');
});

app.listen(port, () => {
  debug(`Listening to port ${chalk.green(port)}`);
});

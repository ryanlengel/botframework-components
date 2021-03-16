// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

'use strict';
const BotGenerator = require('@microsoft/generator-microsoft-bot-adaptive/generators/app/botGenerator');

module.exports = class extends BotGenerator {
  constructor(args, opts) {
    super(args, opts);

    this.argument('botName', { type: String, required: true });
  }

  initializing() {
    this.composeWith(
      require.resolve('@microsoft/generator-microsoft-bot-adaptive/generators/app'),
      {
        arguments: this.args,
        packageReferences: [],
        applicationSettingsDirectory: 'settings'
      }
    );
  }
  
  writing() {
    const filePaths = this.selectTemplateFilePaths('**', '*');
    this.log('File Paths: ' + filePaths.join(', '));

    this.fs.copyTpl(
      this.templatePath(),
      this.destinationPath(this.options.botName),
      {
        botName: this.options.botName
      }
    );
  }
};

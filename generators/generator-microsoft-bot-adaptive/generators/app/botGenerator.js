// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

'use strict';
const Generator = require('yeoman-generator');
const globby = require('globby');

module.exports = class BotGenerator extends Generator {
    constructor(args, opts) {
        super(args, opts);
    }

    selectTemplateFilePaths(...path) {
        const pattern = /\\/gi;
        const options = {
            nodir: true
        };

        return globby.sync(
            this.templatePath(...path).replace(pattern, '/'),
            options);
    }
};

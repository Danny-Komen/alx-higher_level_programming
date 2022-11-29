#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length < 3) {
    console.log('No argument')
}
if (argv === 3) {
    console.log('Agument found')
}
else {
    console.log('Arguments found')
}

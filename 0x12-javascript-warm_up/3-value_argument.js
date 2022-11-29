#!/usr/bin/node
import { argv } from 'node: process';

if (argv.length < 3) {
    console.log('No argument');
}
else {
    argv.every((val, index) => {
        if (index === 0 | index == 1) {
            return false;
        }
        console.log(`${val}`);
        return true;
    });
}

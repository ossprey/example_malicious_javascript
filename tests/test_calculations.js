const assert = require('assert');
const { add, subtract, multiply, divide } = require('../mathlib/calculations');

describe('Calculations', function () {
    describe('add', function () {
        it('should add two numbers', function () {
            assert.strictEqual(add(1, 2), 3);
            assert.strictEqual(add(-1, 1), 0);
            assert.strictEqual(add(-1, -1), -2);
        });
    });

    describe('subtract', function () {
        it('should subtract two numbers', function () {
            assert.strictEqual(subtract(5, 3), 2);
            assert.strictEqual(subtract(0, 5), -5);
            assert.strictEqual(subtract(-1, -1), 0);
        });
    });

    describe('multiply', function () {
        it('should multiply two numbers', function () {
            assert.strictEqual(multiply(3, 7), 21);
            assert.strictEqual(multiply(-1, 1), -1);
            assert.strictEqual(multiply(-1, -1), 1);
        });
    });

    describe('divide', function () {
        it('should divide two numbers', function () {
            assert.strictEqual(divide(10, 2), 5);
            assert.strictEqual(divide(5, 0), "Cannot divide by zero");
            assert.strictEqual(divide(-10, -2), 5);
        });
    });
});
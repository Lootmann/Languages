const std = @import("std");
const print = @import("std").debug.print;
const expect = @import("std").testing.expect;

fn addFive(x: u32) u32 {
    return x + 5;
}

test "function addFive" {
    const y = addFive(10);

    try expect(@TypeOf(y) == u32);
    try expect(y == 15);
}

fn fib(n: u32) u32 {
    if (n == 0 or n == 1) return n;
    return fib(n - 1) + fib(n - 2);
}

test "function fib" {
    try expect(fib(0) == 0);
    try expect(fib(1) == 1);
    try expect(fib(2) == 1);
    try expect(fib(3) == 2);
    try expect(fib(4) == 3);
    try expect(fib(5) == 5);
    try expect(fib(6) == 8);
    try expect(fib(7) == 13);
    try expect(fib(8) == 21);
}

test "test defet test" {
    var n: u32 = 10;

    {
        defer n += 10;
        try expect(n == 10);
    }
    try expect(n == 20);
}

const std = @import("std");
const print = @import("std").debug.print;

pub fn fib(n: u16) u16 {
    if (n == 0 or n == 1) return n;
    return fib(n - 1) + fib(n - 2);
}

pub fn main() void {
    //
    // Assignment
    //
    std.debug.print("Hello, {s}!\n", .{"World"});

    const constant: i32 = 5;
    var variable: u32 = 5000;

    const inferred_constant = @as(i32, 5);
    const inferred_variable = @as(i32, 5);

    print("{d}\n", .{constant});
    print("{d}\n", .{variable});

    print("{d}\n", .{inferred_constant});
    print("{d}\n", .{inferred_variable});

    // Arrays
    const char_array = [5]u8{ 'h', 'e', 'l', 'l', 'o' };
    print("a.len = {d}\n", .{char_array.len});

    // for
    for (char_array) |character, index| {
        print("{c}, {d}\n", .{ character, index });
    }

    // if
    if (true) {
        variable += 1;
    }
    print("{d}\n", .{variable});

    // while
    var i: u8 = 1;
    while (i < 100) {
        print("i = {d}\n", .{i});
        i *= 2;
    }
    print("i = {d}\n", .{i});

    // recursion
    print("{d}\n", .{fib(12)});

    // switch
    var x: i8 = 10;
    switch (x) {
        -1...1 => {
            print("{s}", .{"-1 ... 1"});
        },
        2...10 => {
            print("{s}", .{"2...10"});
        },
        else => {
            print("{s}", .{"NOT -1...10"});
        },
    }
}
